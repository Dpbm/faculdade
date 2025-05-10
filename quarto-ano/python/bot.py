import pandas as pd
import requests
import os
import re

# === CONFIGURAÇÕES ===
caminho_arquivo = 'a.xlsx'  # Ex: 'imagens.xlsx'
pasta_destino = 'imagens_baixadas'

# === CRIA A PASTA DE DESTINO SE NÃO EXISTIR ===
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# === LÊ A PLANILHA ===
df = pd.read_excel(caminho_arquivo)

# === LIMPA TEXTO PARA USO EM NOMES DE ARQUIVOS ===
def limpar_nome(nome):
    nome = str(nome).strip()
    nome = re.sub(r'[\\/*?:"<>|]', '_', nome)
    return nome

# === PROCESSA LINHA A LINHA ===
for index, row in df.iterrows():
    valor_base = row.iloc[0]  # Coluna 0

    if pd.isna(valor_base):  # Encerra o loop ao encontrar primeira célula vazia
        print(f"[!] Fim da leitura: linha {index+1} vazia na coluna 0.")
        break

    nome_base = limpar_nome(valor_base)

    for col_idx in range(2, 19):  # Colunas de índice 2 até 18
        link = row.iloc[col_idx]
        if pd.isna(link) or not isinstance(link, str) or not link.startswith('http'):
            continue
        try:
            response = requests.get(link, stream=True, timeout=10)
            if response.status_code == 200:
                extensao = link.split('.')[-1].split('?')[0].split('&')[0]
                if len(extensao) > 5 or '/' in extensao:
                    extensao = 'jpg'  # fallback
                nome_arquivo = f"{nome_base}_col{col_idx+1}.{extensao}"
                caminho_img = os.path.join(pasta_destino, nome_arquivo)
                with open(caminho_img, 'wb') as f:
                    f.write(response.content)
                print(f"[✓] Baixada: {nome_arquivo}")
            else:
                print(f"[✗] Link inválido na linha {index+1}, coluna {col_idx+1}")
        except Exception as e:
            print(f"[!] Erro ao baixar na linha {index+1}, coluna {col_idx+1}: {e}")
