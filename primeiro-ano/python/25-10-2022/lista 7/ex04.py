arq_name = input("Nome do arquivo: ")
word     = input("Uma palavra: ")
with open(arq_name, "r") as arq:
    text_file = arq.read()
    total_count = text_file.count(word)

    print(f"A palavra {word} apareceu {total_count} vezes no arquivo {arq_name}")