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
    #print("No se encontro")
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
        'detectOrientation ': 'true',
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

