# conversor_xml_nf

# Conversão de XML de Notas Fiscais para Excel

Este projeto tem como objetivo automatizar a extração de informações de arquivos XML de notas fiscais eletrônicas (NFe) e convertê-las para uma planilha Excel. O script percorre todos os arquivos XML de uma pasta específica, extrai dados relevantes (número da nota, empresa emissora, nome do cliente, endereço e peso) e gera uma planilha organizada contendo essas informações.

## Funcionalidades

- Leitura de arquivos XML de notas fiscais em massa.
- Extração de informações como número da nota, nome da empresa emissora, nome do cliente, endereço e peso.
- Criação de uma planilha Excel com os dados extraídos.
- Exportação da planilha Excel para o arquivo `NotasFiscais.xlsx`.

## Estrutura do Projeto

- `nfs/`: Diretório onde os arquivos XML estão armazenados.
- `script.py`: Script Python que realiza a extração e conversão dos dados.
- `NotasFiscais.xlsx`: Arquivo gerado com os dados das notas fiscais em formato Excel.

## Dependências

Este projeto utiliza as seguintes bibliotecas:

- `xmltodict`: Para leitura e conversão de arquivos XML para dicionários Python.
- `os`: Para manipulação de arquivos e diretórios.
- `pandas`: Para criar e manipular dataframes e gerar o arquivo Excel.

### Instalação das dependências

Para instalar as dependências, execute:

```bash
pip install xmltodict pandas
