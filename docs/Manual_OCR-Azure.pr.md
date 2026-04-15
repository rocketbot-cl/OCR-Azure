



# OCR Azure
  
Módulo para aplicar OCR em uma imagem da web ou arquivo  

*Read this in other languages: [English](Manual_OCR-Azure.md), [Português](Manual_OCR-Azure.pr.md), [Español](Manual_OCR-Azure.es.md)*
  
![banner](imgs/Azure-OCR.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  



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
- result:
 Variavel do Rocketbot onde a saida e armazenada.

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
-
 region: Regiao do recurso no Azure.
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

## Descrição do comando

### OCR azure converter imagem
  
Extrai texto de uma imagem.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Imagem||Archivo de Imagen o URL|
|Insira sua chave||API Key|
|Selecione a Região|||
|Resultado||{resultado}|

### Computer Vision READ
  
Extrai texto de uma imagem de forma mais moderna e precisa que o OCR tradicional.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Imagem|Caminho do arquivo ou url da imagem|Archivo de Imagen o URL|
|Insira sua chave|Obtenha sua chave em https//portal.azure.com|Chave da API|
|Selecione a Região|Selecione a região||
|Idioma|Idioma do texto a reconhecer. Deixe vazio para detecção automática quando aplicável.|en|
|Tempo máximo de espera|Tempo máximo de espera para que a operação seja concluída.|60|
|Intervalo de consulta|Número de segundos entre cada verificação do estado da análise.|1|
|Resultado|Variável onde o resultado é armazenado sem {}|{resultado}|

### Inteligência de Documentos
  
Analisa documentos completos.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Documento|Caminho local ou URL do documento a ser analisado. Pode ser PDF ou imagem.|C:/files/fatura.pdf ou https://...|
|Insira sua chave|Chave API do recurso Azure Document Intelligence.|Chave API|
|Selecione a Região|Selecione a região onde o recurso Azure Document Intelligence foi criado.||
|Modelo|ID do modelo a ser utilizado. Pode ser um modelo prebuilt ou um modelo personalizado. Os modelos prebuilt incluem 'prebuilt-read' para OCR, 'prebuilt-layout' para análise de layout, e 'prebuilt-document' para análise geral de documentos.|prebuilt-read|
|Versão da API|Versão da API de Intelligence de Documentos. Se deixado vazio, o valor padrão do módulo será usado.|2023-07-31|
|Páginas|Páginas a serem analisadas. Você pode indicar uma única página, várias ou um intervalo. Por exemplo '1', '1,3,5' ou '1-5'. Se deixado vazio, todas as páginas serão analisadas.|1-3|
|Configuração regional|Configuração regional do documento. Útil para melhorar a interpretação com base no idioma ou formato.|pt-BR|
|Tempo máximo de espera|Tempo máximo de espera para que a operação seja concluída.|60|
|Intervalo de consulta|Quantidade de segundos entre cada verificação do status da análise.|1|
|Resultado|Variável onde o resultado é armazenado sem {}|{resultado}|
