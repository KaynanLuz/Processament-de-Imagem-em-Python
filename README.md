# Pacote de Processamento de Imagem Simples

Este é um pacote Python simples para processamento básico de imagens, que permite redimensionar, converter para tons de cinza e aplicar desfoque a imagens. Ele foi criado utilizando a biblioteca **Pillow**.

## Funcionalidades

- **Redimensionar imagens**: Redimensiona a imagem para qualquer dimensão especificada.
- **Converter para tons de cinza**: Converte a imagem para uma versão em preto e branco.
- **Aplicar desfoque**: Aplica um filtro de desfoque Gaussian à imagem.
- **Salvar e exibir imagens**: As imagens processadas podem ser salvas ou visualizadas diretamente.

## Requisitos

- Python 3.x
- Biblioteca [Pillow](https://pillow.readthedocs.io/) para manipulação de imagens

## Instalação

1. Clone este repositório ou baixe os arquivos do projeto.

   ```bash
   git clone <URL_DO_REPOSITORIO>

2. cd caminho/para/o/diretorio/projeto
pip install .

## Como Usar
Depois de instalar o pacote, você pode utilizá-lo para processar imagens. Aqui está um exemplo básico:

No seu script Python, importe a classe ImageProcessor do pacote:

python

from imagem_simples_processamento import ImageProcessor


python
processor = ImageProcessor("imagem_test.jpg")

Redimensionar, converter para tons de cinza e salvar
processor.resize(300, 300).grayscale().save("imagem_processada.jpg")


Redimensionar, converter para tons de cinza e salvar
processor.resize(300, 300).grayscale().save("imagem_processada.jpg")

## Exemplo Completo
python
from imagem_simples_processamento import ImageProcessor

# Carregar uma imagem de exemplo
processor = ImageProcessor("imagem_test.jpg")

# Aplicar algumas manipulações e salvar
processor.resize(300, 300).grayscale().save("imagem_processada.jpg")


Este exemplo redimensiona a imagem para 300x300 pixels, converte para tons de cinza e salva o resultado em imagem_processada.jpg.