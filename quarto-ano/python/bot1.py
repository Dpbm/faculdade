import pandas as pd
import requests
import os

caminho_arquivo = 'a.xlsx'  # Ex: 'imagens.xlsx'
nome_coluna_links = 'links'  # Nome da coluna onde estão os links
pasta_destino = 'imagens_baixadas'  # Pasta onde as imagens serão salvas

# === CRIA A PASTA DE DESTINO SE NÃO EXISTIR ===
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# === LÊ A PLANILHA ===
df = pd.read_excel(caminho_arquivo)
print(df)

# === BAIXA AS IMAGENS ===
for i, link in enumerate(df[nome_coluna_links]):
    if pd.isna(link):
        continue
    try:
        response = requests.get(link, stream=True, timeout=10)
        if response.status_code == 200:
            extensao = link.split('.')[-1].split('?')[0]
            nome_arquivo = f"imagem_{i+1}.{extensao}"
            caminho_arquivo_img = os.path.join(pasta_destino, nome_arquivo)
            with open(caminho_arquivo_img, 'wb') as f:
                f.write(response.content)
            print(f"[✓] Baixada: {nome_arquivo}")
        else:
            print(f"[✗] Erro no link ({i+1}): {link}")
    except Exception as e:
        print(f"[!] Falha ao baixar a imagem {i+1}: {e}")

