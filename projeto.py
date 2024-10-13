import xmltodict 
import os
import pandas as pd

# Função que extrai informações dos arquivos XML
def pegar_infos(nome_arquivo, valores):
    #print(f"Pegou as informações {nome_arquivo}")
    with open(f'nfs/{nome_arquivo}', "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)
        #print(json.dumps(dic_arquivo, indent=4))
        if "NFe" in dic_arquivo:
            infos_nf = dic_arquivo["NFe"]["infNFe"]
        else:    
            infos_nf = dic_arquivo["nfeProc"]["NFe"]["infNFe"]
        numero_nota = infos_nf["@Id"]
        empresa_emissora = infos_nf["emit"]["xNome"]
        nome_cliente = infos_nf["dest"]["xNome"]
        endereco = infos_nf["dest"]["enderDest"]
        if "vol" in infos_nf["transp"]:
            peso = infos_nf["transp"]["vol"]["pesoB"]
        else:
            peso = "Não informado."

        # Adiciona as informações à lista 'valores'    
        valores.append([numero_nota,empresa_emissora,nome_cliente,endereco,peso])

# Lista os arquivos XML na pasta 'nfs'
lista_arquivos = os.listdir("nfs")    

# Define os nomes das colunas
colunas = ["numero_nota","empresa_emissora","nome_cliente","endereco","peso"]

# Lista que irá armazenar os dados extraídos
valores =[]

# Extrai as informações de cada arquivo XML
for arquivo in lista_arquivos:
    pegar_infos(arquivo, valores)

# Cria o DataFrame com os dados extraídos
tabela = pd.DataFrame(columns=colunas, data=valores)   

# Exporta o DataFrame para um arquivo Excel
tabela.to_excel("NotasFiscais.xlsx", index=False)