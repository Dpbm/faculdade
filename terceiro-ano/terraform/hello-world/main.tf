resource  "local_file" "arquivos_curso"{
  count = 12
  content = "Hello, World!"
  filename = "${var.nome_arquivo}${count.index}.txt"
}
