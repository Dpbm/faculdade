import os
import requests
import pandas as pd

TARGET_FOLDER = os.path.join(".", "images")
is_excel = lambda x : x.endswith(".xlsx")

def download_image(url, file_path):
    try:
        response = requests.get(url, stream=True, timeout=10)
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"[✓] Baixada: {file_path}")
    except Exception as error:
            print(f"[!] Erro ao baixar: {error}")

def get_excel(file_path, download_folder):
    try:
        df = pd.read_excel(file_path)

        for i,row in df.iterrows():
            name = row.iloc[0].strip().lower()
            total_cols = len(row)
            for column in range(2, total_cols):
               value = row.iloc[column]
               if(pd.isna(value)):
                 continue
               filename = f'{name}_{column-1}.png'
               file_path = os.path.join(download_folder, filename)

               download_image(value,file_path)
    except Exception as error:
        print(f"[!] Falha ao manipular o arquivo: {file_path}")
        print(f"[!] Erro: {error}")

def create_path(path):
    if not os.path.exists(path):
        print(f"[*] Criando caminho:{path}")
        os.makedirs(path)

if __name__ == "__main__":
    create_path(TARGET_FOLDER)

    current_dir_files = os.listdir(".")
    excel_files = list(filter(is_excel, current_dir_files))
    print(f"[*] Arquivos encontrados: {excel_files}")

    for excel_file in excel_files:

        print(f"[!] Testando arquivo {excel_file}")

        new_folder_name = excel_file.replace(".xlsx", "")
        new_folder_path = os.path.join(TARGET_FOLDER, new_folder_name)
        create_path(new_folder_path)

        get_excel(excel_file, new_folder_path)


