## How to use this module
Before using this module, you need an Azure account: https://portal.azure.com

This module supports 3 operations:
1. GetOCR (Computer Vision OCR v1.0)
2. GetReadOCR (Computer Vision Read v3.2)
3. AnalyzeDocument (Azure Document Intelligence)

### 1) Azure setup

#### A. For GetOCR and GetReadOCR (Computer Vision)
1. Go to Azure Portal.
2. Create a Computer Vision (or Azure AI Vision) resource.
3. Save these values:
   - API Key
   - Region
   - Endpoint

#### B. For AnalyzeDocument (Document Intelligence)
1. Go to Azure Portal.
2. Create a Document Intelligence resource.
3. Save these values:
   - API Key
   - Region
   - Endpoint

### 2) Rocketbot command configuration

#### GetOCR
Use this command to extract text from an image URL or local image path using classic OCR.

Required fields:
- image_path: Local image path or URL.
- api_key: Computer Vision API key.
- region: Azure region of the resource.
- result: Rocketbot variable where output is stored.

Output:
- The result variable stores the full JSON response.
- textAnnotation contains extracted plain text.

#### GetReadOCR
Use this command to extract text from image URL or local image path using async Read API.

Required fields:
- image_path: Local image path or URL.
- api_key: Computer Vision API key.
- region: Azure region of the resource.
- result: Rocketbot variable where output is stored.

Optional fields:
- language: Language hint (example: en, es).
- timeout: Max wait time in seconds (default: 60).
- poll_interval: Polling interval in seconds (default: 1).

Output:
- The result variable stores the operation JSON.
- textAnnotation contains extracted plain text from lines.

#### AnalyzeDocument
Use this command to analyze PDF/image documents with Document Intelligence.

Required fields:
- source: Local file path or URL (PDF or image).
- api_key: Document Intelligence API key.
- region: Azure region of the resource.
- model_id: Model ID (example: prebuilt-read, prebuilt-layout, prebuilt-document).
- result: Rocketbot variable where output is stored.

Optional fields:
- api_version: API version (default: 2023-07-31).
- pages: Pages to analyze (example: 1, 1-3, 1,3,5).
- locale: Locale hint (example: en-US, es-ES, pt-BR).
- timeout: Max wait time in seconds (default: 60).
- poll_interval: Polling interval in seconds (default: 1).

Output:
- The result variable stores the operation JSON.
- textAnnotation contains full extracted text when available.

### 3) Notes and recommendations
- Verify that region and key belong to the same Azure resource.
- For local files, make sure Rocketbot can access the file path.
- If you get timeout errors, increase timeout and/or poll_interval.
- For PDFs and structured documents, prefer AnalyzeDocument.

---

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
- region: Region del recurso en Azure.
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
- api_key: API key de Document Intelligence.
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

---

## Como usar este modulo
Antes de usar este modulo, voce precisa de uma conta Azure: https://portal.azure.com

Este modulo suporta 3 operacoes:
1. GetOCR (Computer Vision OCR v1.0)
2. GetReadOCR (Computer Vision Read v3.2)
3. AnalyzeDocument (Azure Document Intelligence)

### 1) Configuracao no Azure

#### A. Para GetOCR e GetReadOCR (Computer Vision)
1. Acesse o portal do Azure.
2. Crie um recurso de Computer Vision (ou Azure AI Vision).
3. Salve estes dados:
   - API Key
   - Region
   - Endpoint

#### B. Para AnalyzeDocument (Document Intelligence)
1. Acesse o portal do Azure.
2. Crie um recurso de Document Intelligence.
3. Salve estes dados:
   - API Key
   - Region
   - Endpoint

### 2) Configuracao dos comandos no Rocketbot

#### GetOCR
Use este comando para extrair texto de URL de imagem ou caminho local usando OCR classico.

Campos obrigatorios:
- image_path: Caminho local da imagem ou URL.
- api_key: API key do Computer Vision.
- region: Regiao do recurso no Azure.
- result: Variavel do Rocketbot onde a saida e armazenada.

Saida:
- A variavel de resultado armazena o JSON completo.
- textAnnotation contem o texto plano extraido.

#### GetReadOCR
Use este comando para extrair texto de URL de imagem ou caminho local com a API Read assincrona.

Campos obrigatorios:
- image_path: Caminho local da imagem ou URL.
- api_key: API key do Computer Vision.
- region: Regiao do recurso no Azure.
- result: Variavel do Rocketbot onde a saida e armazenada.

Campos opcionais:
- language: Idioma sugerido (exemplo: en, es).
- timeout: Tempo maximo de espera em segundos (padrao: 60).
- poll_interval: Intervalo de consulta em segundos (padrao: 1).

Saida:
- A variavel de resultado armazena o JSON da operacao.
- textAnnotation contem o texto extraido por linhas.

#### AnalyzeDocument
Use este comando para analisar documentos PDF/imagem com Document Intelligence.

Campos obrigatorios:
- source: Caminho local ou URL (PDF ou imagem).
- api_key: API key do Document Intelligence.
- region: Regiao do recurso no Azure.
- model_id: ID do modelo (exemplo: prebuilt-read, prebuilt-layout, prebuilt-document).
- result: Variavel do Rocketbot onde a saida e armazenada.

Campos opcionais:
- api_version: Versao da API (padrao: 2023-07-31).
- pages: Paginas para analisar (exemplo: 1, 1-3, 1,3,5).
- locale: Configuracao regional sugerida (exemplo: en-US, es-ES, pt-BR).
- timeout: Tempo maximo de espera em segundos (padrao: 60).
- poll_interval: Intervalo de consulta em segundos (padrao: 1).

Saida:
- A variavel de resultado armazena o JSON da operacao.
- textAnnotation contem o texto completo extraido quando disponivel.

### 3) Notas e recomendacoes
- Verifique se region e key pertencem ao mesmo recurso Azure.
- Para arquivos locais, valide se o Rocketbot tem acesso ao caminho.
- Se ocorrer timeout, aumente timeout e/ou poll_interval.
- Para PDFs e documentos estruturados, prefira AnalyzeDocument.
