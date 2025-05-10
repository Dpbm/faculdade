import pandas as pd
import requests
import os
import re

# === CONFIGURAÇÕES ===
caminho_arquivo = 'a.xlsx'  # Ex: 'imagens.xlsx'
colunas_links = ['A', 'BB']  # col1 até col19
pasta_destino = 'imagens_baixadas'

# === CRIA A PASTA DE DESTINO SE NÃO EXISTIR ===
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# === LÊ A PLANILHA ===
df = pd.read_excel(caminho_arquivo)

# === LIMPA O TEXTO PARA USAR COMO NOME DE ARQUIVO ===
def limpar_nome(nome):
    nome = str(nome).strip()
    nome = re.sub(r'[\\/*?:"<>|]', '_', nome)  # Remove caracteres inválidos
    return nome

# === VERIFICA E BAIXA LINKS ===
for index, row in df.iterrows():
    nome_base = limpar_nome(row.iloc[0])  # Texto da primeira coluna da linha
    img_count = 1

    for coluna in colunas_links:
        link = row.get(coluna)
        if pd.isna(link) or not isinstance(link, str) or not link.startswith('http'):
            continue
        try:
            response = requests.get(link, stream=True, timeout=10)
            if response.status_code == 200:
                extensao = link.split('.')[-1].split('?')[0].split('&')[0]
                if len(extensao) > 5 or '/' in extensao:
                    extensao = 'jpg'  # fallback
                nome_arquivo = f"{nome_base}_img{img_count}.{extensao}"
                caminho_img = os.path.join(pasta_destino, nome_arquivo)
                with open(caminho_img, 'wb') as f:
                    f.write(response.content)
                print(f"[✓] Baixada: {nome_arquivo}")
                img_count += 1
            else:
                print(f"[✗] Link inválido em {coluna}, linha {index+1}")
        except Exception as e:
            print(f"[!] Erro em {coluna}, linha {index+1}: {e}")
