arq_name = input("Nome do arquivo: ")
with open(arq_name, "r") as arq:
    total_lines = len(arq.readlines())
    print(f"O arquivo {arq_name} possui {total_lines} linhas")