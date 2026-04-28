# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import requests
import urllib.parse
import json
import time
from time import sleep


def _is_url(s: str) -> bool:
    return isinstance(s, str) and s.lower().startswith(("http://", "https://"))


def _poll_operation(op_url: str, headers: dict, timeout_sec: int = 60, poll_interval: float = 1.0) -> dict:
    t0 = time.time()
    last = None
    while True:
        r = requests.get(op_url, headers=headers)
        r.raise_for_status()
        last = r.json()
        status = (last.get("status") or "").lower()

        if status in ("succeeded", "failed"):
            return last

        if time.time() - t0 > timeout_sec:
            raise TimeoutError(f"Timeout polling operation. Last status={status}")

        sleep(poll_interval)


def _extract_text_from_vision_read(result_json: dict) -> str:
    """
    Azure Vision Read v3.2:
      analyzeResult -> readResults -> lines -> text
    """
    out = []
    analyze = result_json.get("analyzeResult") or {}
    pages = analyze.get("readResults") or []
    for p in pages:
        for line in (p.get("lines") or []):
            txt = line.get("text")
            if txt:
                out.append(txt)
    return "\n".join(out).strip()


def _extract_text_from_di(result_json: dict) -> str:
    """
    Document Intelligence:
      analyzeResult -> content (cuando aplica)
    """
    analyze = result_json.get("analyzeResult") or {}
    content = analyze.get("content")
    if isinstance(content, str):
        return content.strip()
    return ""

def busqueda(key,tree):
    if isinstance(tree,(list,tuple)): # This is the tree
        for element in tree: # Search each "node" for our item
            rst = busqueda(key,element)
            if rst:
                return rst
    elif isinstance(tree,dict): # This is a child
        for element in tree.keys():
            if element == key:
                return tree[element]
            else:
                rst = busqueda(key,tree[element])
                if rst:
                    return rst
    elif isinstance(tree,str):
        if tree == key:
            return tree
    return ""

module = GetParams("module")

if module == "GetOCR":
    image_path = GetParams("image_path")
    api_key = GetParams("api_key")
    region = GetParams("region")
    result = GetParams("result")

    print("region", region)

    if image_path.startswith("http"):
        headers = {
            # Request headers
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': api_key
        }
        data = {"url": image_path}
        data = json.dumps(data)
        
    else:
        with open(image_path, 'rb') as f:
            data = f.read()
        
        headers = {
            # Request headers
            "Content-Type": "application/octet-stream",
            "Ocp-Apim-Subscription-Key": api_key
        }
        
    params = urllib.parse.urlencode({
        # Request parameters
        'language': 'unk',
        'detectOrientation': 'true',
    })

    try:
        response = requests.post("https://{reg}.api.cognitive.microsoft.com/vision/v1.0/ocr?{prm}".format(reg=region, prm=params), headers=headers, data=data)
        json_resp = response.json()
        if result:
            texto = ""
            print(json_resp)
            if len(json_resp["regions"]):
                for region in json_resp["regions"]:
                    lines = region["lines"]
                    for line in lines:
                        words = line["words"]
                        for word in words:
                            texto += word["text"] + " "
                        texto += "\n"
        json_resp["textAnnotation"] = texto
        SetVar(result, json_resp)
    except Exception as e:
        PrintException()
        raise e

# NUEVO: Computer Vision READ v3.2

if module == "GetReadOCR":
    image_path = GetParams("image_path")   # URL o ruta local
    api_key = GetParams("api_key")
    region = GetParams("region")
    result = GetParams("result")

    # opcionales (si no existen en forms, quedan None)
    language = GetParams("language")            # ej: "es", "en"
    timeout = GetParams("timeout")              # ej: 60
    poll_interval = GetParams("poll_interval")  # ej: 1

    timeout_sec = int(timeout) if timeout else 60
    poll_interval_sec = float(poll_interval) if poll_interval else 1.0

    try:
        base = f"https://{region}.api.cognitive.microsoft.com"
        url = f"{base}/vision/v3.2/read/analyze"

        headers = {
            "Ocp-Apim-Subscription-Key": api_key
        }

        params = {}
        if language:
            params["language"] = language

        if _is_url(image_path):
            headers["Content-Type"] = "application/json"
            payload = {"url": image_path}
            resp = requests.post(url, headers=headers, params=params, json=payload)
        else:
            headers["Content-Type"] = "application/octet-stream"
            with open(image_path, "rb") as f:
                data = f.read()
            resp = requests.post(url, headers=headers, params=params, data=data)

        resp.raise_for_status()

        op_url = resp.headers.get("Operation-Location")
        if not op_url:
            raise Exception("Operation-Location header not found (Vision Read).")

        op_headers = {"Ocp-Apim-Subscription-Key": api_key}
        op_json = _poll_operation(op_url, op_headers, timeout_sec=timeout_sec, poll_interval=poll_interval_sec)

        op_json["textAnnotation"] = _extract_text_from_vision_read(op_json)

        SetVar(result, op_json)

    except Exception as e:
        PrintException()
        raise e

# NUEVO: Azure Document Intelligence (Form Recognizer)

if module == "AnalyzeDocument":
    source = GetParams("source")          # URL o ruta local (PDF/imagen)
    api_key = GetParams("api_key")
    region = GetParams("region")
    model_id = GetParams("model_id")      # ej: "prebuilt-read"
    result = GetParams("result")

    # opcionales
    api_version = GetParams("api_version")        # ej: "2023-07-31"
    pages = GetParams("pages")                    # ej: "1-3"
    locale = GetParams("locale")                  # ej: "es-ES"
    timeout = GetParams("timeout")
    poll_interval = GetParams("poll_interval")

    api_version = api_version or "2023-07-31"
    timeout_sec = int(timeout) if timeout else 60
    poll_interval_sec = float(poll_interval) if poll_interval else 1.0

    try:
        base = f"https://{region}.api.cognitive.microsoft.com"
        analyze_url = f"{base}/formrecognizer/documentModels/{model_id}:analyze"

        params = {"api-version": api_version}
        if pages:
            params["pages"] = pages
        if locale:
            params["locale"] = locale

        headers = {
            "Ocp-Apim-Subscription-Key": api_key
        }

        if _is_url(source):
            headers["Content-Type"] = "application/json"
            payload = {"urlSource": source}
            resp = requests.post(analyze_url, headers=headers, params=params, json=payload)
        else:
            headers["Content-Type"] = "application/octet-stream"
            with open(source, "rb") as f:
                data = f.read()
            resp = requests.post(analyze_url, headers=headers, params=params, data=data)

        resp.raise_for_status()

        op_url = resp.headers.get("Operation-Location")
        if not op_url:
            raise Exception("Operation-Location header not found (Document Intelligence).")

        op_headers = {"Ocp-Apim-Subscription-Key": api_key}
        op_json = _poll_operation(op_url, op_headers, timeout_sec=timeout_sec, poll_interval=poll_interval_sec)

        # texto completo (cuando venga)
        op_json["textAnnotation"] = _extract_text_from_di(op_json)

        SetVar(result, op_json)

    except Exception as e:
        PrintException()
        raise e