
import pandas as pd
import requests
import os

# === CONFIGURAÇÕES ===
caminho_arquivo = 'a.xlsx'  # Ex: 'imagens.xlsx'
colunas_links = ['links','links2']  # Exemplo: col1, col2, ..., col16
pasta_destino = 'imagens_baixadas'

# === CRIA A PASTA DE DESTINO SE NÃO EXISTIR ===
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# === LÊ A PLANILHA ===
df = pd.read_excel(caminho_arquivo)

# === VERIFICA E BAIXA LINKS ===
for index, row in df.iterrows():
    for coluna in colunas_links:
        link = row.get(coluna)
        if pd.isna(link) or not isinstance(link, str) or not link.startswith('http'):
            continue
        try:
            response = requests.get(link, stream=True, timeout=10)
            if response.status_code == 200:
                extensao = link.split('.')[-1].split('?')[0]
                nome_arquivo = f"img_linha{index+1}_{coluna}.{extensao}"
                caminho_img = os.path.join(pasta_destino, nome_arquivo)
                with open(caminho_img, 'wb') as f:
                    f.write(response.content)
                print(f"[✓] Baixada: {nome_arquivo}")
            else:
                print(f"[✗] Erro no link ({coluna}, linha {index+1})")
        except Exception as e:
            print(f"[!] Falha em {coluna}, linha {index+1}: {e}")

