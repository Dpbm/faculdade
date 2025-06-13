class TextoEditor:
    def __init__(self):
        self._conteudo = ""

    def escrever(self, texto):
        self._conteudo += texto

    def mostrar_conteudo(self):
        print(self._conteudo)

    def apagar_ultimo(self, texto):
        if self._conteudo.endswith(texto):
            self._conteudo = self._conteudo[:-len(texto)]

class ComandoTexto:
    def executar(self):
        pass

    def desfazer(self):
        pass

class EscreverTexto(ComandoTexto):
    def __init__(self, editor, texto):
        self.editor = editor
        self.texto = texto

    def executar(self):
        self.editor.escrever(self.texto)

    def desfazer(self):
        self.editor.apagar_ultimo(self.texto)

class Historico:
    def __init__(self, editor):
        self._editor = editor
        self._historico = []
        self._comandos = []
        self._desfazer_comandos = []

    def _add_historico(self, comando, texto):
        self._historico.append(f"""
        --------------------------
        [{comando}]
        texto: {texto}
        """
        )

    def executar_comando(self, comando):
        self._comandos.append(comando)
        self._desfazer_comandos.clear()
        comando.executar()
        self._add_historico(comando.__class__.__name__, self._editor._conteudo)


    def desfazer(self):
        if self._comandos:
            comando = self._comandos.pop()
            comando.desfazer()
            self._desfazer_comandos.append(comando)
            self._add_historico("desfazer", self._editor._conteudo)

    def refazer(self):
        if self._desfazer_comandos:
            comando = self._desfazer_comandos.pop()
            comando.executar()
            self._comandos.append(comando)
            self._add_historico("refazer", self._editor._conteudo)
    
    def mostrar_historico(self):
        for step in self._historico:
            print(step)
    


if __name__ == "__main__":
    editor = TextoEditor()
    historico = Historico(editor)

    comando1 = EscreverTexto(editor, "Olá, mundo mundo")
    comando2 = EscreverTexto(editor, "Olá, ")
    comando3 = EscreverTexto(editor, "mundo!")
    historico.executar_comando(comando1)
    historico.executar_comando(comando2)
    historico.executar_comando(comando3)

    editor.mostrar_conteudo() 

    historico.desfazer()
    historico.desfazer()
    historico.desfazer()
    historico.refazer()

    historico.mostrar_historico()