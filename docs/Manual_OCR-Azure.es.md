



# OCR Azure
  
Modulo para aplicar OCR sobre una imagen web o archivo  

*Read this in other languages: [English](Manual_OCR-Azure.md), [Português](Manual_OCR-Azure.pr.md), [Español](Manual_OCR-Azure.es.md)*
  
![banner](imgs/Azure-OCR.jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  



## Como usar este modulo
Antes de usar este modulo, necesitas una cuenta de Azure: https://portal.azure.com

Este modulo soporta 3 operaciones:
1. GetOCR (Computer Vision OCR v1.0)
2. GetReadOCR (Computer Vision Read v3.2)
3. AnalyzeDocument (Azure Document Intelligence)

### 1) Configuracion en Azure

#### A. Para GetOCR y GetReadOCR (Computer Vision)
1. Ingresa al portal de Azure.
2. Crea un recurso de Computer Vision (o Azure AI Vision).
3. Guarda estos datos:
   - API Key
   - Region
   - Endpoint

#### B. Para AnalyzeDocument (Document Intelligence)
1. Ingresa al portal de Azure.
2. Crea un recurso de Document Intelligence.
3. Guarda estos datos:
   - API Key
   - Region
   - Endpoint

### 2) Configuracion de comandos en Rocketbot

#### GetOCR
Usa este comando para extraer texto desde una URL de imagen o ruta local de imagen usando OCR clasico.

Campos obligatorios:
- image_path: Ruta local de imagen o URL.
- api_key: API key de Computer Vision.
- region: Region del recurso en 
Azure.
- result: Variable de Rocketbot donde se guarda la salida.

Salida:
- La variable de resultado guarda la respuesta JSON completa.
- textAnnotation contiene el texto plano extraido.

#### GetReadOCR
Usa este comando para extraer texto desde URL de imagen o ruta local con la API Read asincrona.

Campos obligatorios:
- image_path: Ruta local de imagen o URL.
- api_key: API key de Computer Vision.
- region: Region del recurso en Azure.
- result: Variable de Rocketbot donde se guarda la salida.

Campos opcionales:
- language: Idioma sugerido (ejemplo: en, es).
- timeout: Tiempo maximo de espera en segundos (default: 60).
- poll_interval: Intervalo de consulta en segundos (default: 1).

Salida:
- La variable de resultado guarda el JSON de la operacion.
- textAnnotation contiene el texto extraido por lineas.

#### AnalyzeDocument
Usa este comando para analizar documentos PDF/imagen con Document Intelligence.

Campos obligatorios:
- source: Ruta local o URL (PDF o imagen).
- api_key: 
API key de Document Intelligence.
- region: Region del recurso en Azure.
- model_id: ID del modelo (ejemplo: prebuilt-read, prebuilt-layout, prebuilt-document).
- result: Variable de Rocketbot donde se guarda la salida.

Campos opcionales:
- api_version: Version de API (default: 2023-07-31).
- pages: Paginas a analizar (ejemplo: 1, 1-3, 1,3,5).
- locale: Configuracion regional sugerida (ejemplo: en-US, es-ES, pt-BR).
- timeout: Tiempo maximo de espera en segundos (default: 60).
- poll_interval: Intervalo de consulta en segundos (default: 1).

Salida:
- La variable de resultado guarda el JSON de la operacion.
- textAnnotation contiene el texto completo extraido cuando esta disponible.

### 3) Notas y recomendaciones
- Verifica que region y key correspondan al mismo recurso de Azure.
- Para archivos locales, valida que Rocketbot tenga acceso a la ruta.
- Si recibes timeout, aumenta timeout y/o poll_interval.
- Para PDFs y documentos estructurados, usa preferentemente AnalyzeDocument.


## Descripción de los comandos

### OCR azure convertir imagen
  
Extrae texto de una imagen.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Imagen||Archivo de Imagen o URL|
|Ingrese su key||API Key|
|Seleccione Región|||
|Resultado||{resultado}|

### Computer Vision READ
  
Extrae texto de una imagen de forma mas moderna y precisa que el OCR clasico.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Imagen|Ruta o url de la imagen|Archivo de Imagen o URL|
|Ingrese su key|Busque su key en https//portal.azure.com |API Key|
|Seleccione Región|Seleccione la región ||
|Idioma|Idioma del texto a reconocer. Déjelo vacío para detección automática cuando aplique.|en|
|Tiempo máximo de espera|Tiempo máximo de espera para que se complete la operación.|60|
|Intervalo de consulta|Cantidad de segundos entre cada consulta del estado del análisis.|1|
|Resultado|Variable donde se almacena el resultado sin {}|{resultado}|

### Inteligencia de Documentos
  
Analiza documentos completos.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Documento|Ruta local o URL del documento a analizar. Puede ser PDF o imagen.|C:/files/factura.pdf o https://...|
|Ingrese su key|API Key del recurso Azure Document Intelligence.|API Key|
|Seleccione Región|Seleccione la región donde fue creado el recurso de Azure Document Intelligence.||
|Modelo|ID del modelo a utilizar. Puede ser un modelo prebuilt o un modelo personalizado. Los modelos prebuilt incluyen 'prebuilt-read' para OCR, 'prebuilt-layout' para análisis de layout, y 'prebuilt-document' para análisis general de documentos.|prebuilt-read|
|Versión de la API|Versión de la API de Document Intelligence. Si se deja vacío, se usa el valor por defecto del módulo.|2023-07-31|
|Páginas|Páginas a analizar. Puede indicar una sola página, varias o un rango. Por ejemplo '1', '1,3,5' o '1-5'. Si se deja vacío, se analizarán todas las páginas.|1-3|
|Configuración regional|Configuración regional del documento. Útil para mejorar la interpretación según idioma o formato.|es-ES|
|Tiempo máximo de espera|Tiempo máximo de espera para que se complete la operación.|60|
|Intervalo de consulta|Cantidad de segundos entre cada consulta del estado del análisis.|1|
|Resultado|Variable donde se almacena el resultado sin {}|{resultado}|
