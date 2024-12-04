from pathlib import Path
import pandas as pd 


def carregar_dados(caminho_arquivo):
    # Função que lê e retorna os dados necessários
    df = pd.read_excel(caminho_arquivo)
    return df[['codigo', 'quantidade']]

#colunas_selecionadas = df[['codigo', 'quantidade']]
#print(colunas_selecionadas)

#for index, row in colunas_selecionadas.iterrows():
    #print(f"Código: {row['codigo']}, Quantidade: {row['quantidade']}")


