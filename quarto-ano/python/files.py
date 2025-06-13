URLS=['https://www.inf.ufpr.br/aurora/disciplinas/topicosia2/aulas/1-s2.0-S0957417416000543-main.pdf', 'https://www.inf.ufpr.br/aurora/disciplinas/topicosia2/aulas/10.1007%40978-3-319-55453-2.pdf', 'https://www.inf.ufpr.br/aurora/disciplinas/topicosia2/aulas/Algoritmos%20Gen%E9ticos.pptx', 'https://www.inf.ufpr.br/aurora/disciplinas/topicosia2/aulas/Apresenta%E7%E3o1.pptx', 'https://www.inf.ufpr.br/aurora/disciplinas/topicosia2/aulas/ILS.ppt', 'https://www.inf.ufpr.br/aurora/disciplinas/topicosia2/aulas/PATH-RELINKING.pptx', 'https://www.inf.ufpr.br/aurora/disciplinas/topicos…2C%20ACIIDS%202016%2C%20Da%20Nang%2C%20Vietna.pdf', 'https://www.inf.ufpr.br/aurora/disciplinas/topicosia2/aulas/aco.ppt', 'https://www.inf.ufpr.br/aurora/disciplinas/topicosia2/aulas/aula1.pdf', 'https://www.inf.ufpr.br/aurora/disciplinas/topicosia2/aulas/aula2.pptx', 'https://www.inf.ufpr.br/aurora/disciplinas/topicosia2/aulas/aula3.pptx', 'https://www.inf.ufpr.br/aurora/disciplinas/topicosia2/aulas/aula4.pptx', 'https://www.inf.ufpr.br/aurora/disciplinas/topicosia2/aulas/aula5.pptx', 'https://www.inf.ufpr.br/aurora/disciplinas/topicosia2/aulas/aula6.pptx', 'https://www.inf.ufpr.br/aurora/disciplinas/topicosia2/aulas/aula8.ppt', 'https://www.inf.ufpr.br/aurora/disciplinas/topicosia2/aulas/lista.pdf', 'https://www.inf.ufpr.br/aurora/disciplinas/topicosia2/aulas/lista1.pdf', 'https://www.inf.ufpr.br/aurora/disciplinas/topicosia2/aulas/lista2.pdf', 'https://www.inf.ufpr.br/aurora/disciplinas/topicosia2/aulas/mobilityrecom.pdf', 'https://www.inf.ufpr.br/aurora/disciplinas/topicosia2/aulas/pso.pptx', 'https://www.inf.ufpr.br/aurora/disciplinas/topicosia2/aulas/trab.pptx']

import requests as req
import os

os.makedirs("files", exists_ok=True)
os.chdir("files")

for url in URLS:
    parts = url.split("/")
    filename = parts[-1]
    i = -1
    while not filename:
        i -= 1
        filename = parts[i]

	#print("Downloading file: ", file)
	try:
		res = req.get(url, stream=True)
		with open(file, "wb") as file:
			file.write(res.content)
	except Exception as error:
		print("error: ", error)
