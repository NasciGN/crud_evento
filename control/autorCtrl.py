import locale

from kivy.uix.button import Button
from kivy.uix.label import Label

from model.models import Autor


class AutorCtrl:

    def __init__(self):
        self._lista = []


    def salvarAutor(self, id=None, nome=None, instituicao=None, email=None):
        try:
            if id:
                autor = Autor.get_by_id(id)
                autor.nome = nome
                autor.instituicao = instituicao
                autor.email = email
            else:
                autor = Autor(nome=nome, instituicao=instituicao, email=email)
            autor.save()
            return "O resgistro do autor foi salvo com sucesso!"
        except Exception as E:
            print(E)
            return "Não foi possível salvar o registro do autor!"


    def excluirAutor(self, id):
        try:
            autor = Autor.get_by_id(id)
            autor.delete_instance()
            return "O registro do autor foi excluído com sucesso!"
        except Exception as E:
            print(E)
            return "Não foi possível excluir o registro do autor!"


    def buscar_por_id(self, id):
        self._lista = []
        try:
            autor = Autor.get_by_id(id)
            self._lista.append(self._montar_autor(autor.id, autor.nome, autor.instituicao, autor.email))
            return self._lista
        except Exception as e:
            return None


    def buscar_todas(self):
        try:
            AS = Autor.select()
            self._lista = []
            for A in AS:
                self._lista.append(self._montar_autor(A.id, A.nome, A.instituicao, A.email))
            return self._lista
        except Exception as e:
            return None


    def _montar_autor(self, id, nome, instituicao, email):
        mostraautor = {
            'lblId': self._criarLabel(id, 0.2),
            'lblNome': self._criarLabel(nome, 0.3),
            'lblInstituicao': self._criarLabel(instituicao, 0.4),
            'lblEmail': self._criarLabel(email, 0.4),
            'btAtualizar': self._criarBotao("Atualizar"),
            'btExcluir': self._criarBotao("Excluir")
        }
        return mostraautor

    def _criarLabel(self, texto, tam):
        label = Label()
        label.text = str(texto)
        label.size_hint_y = None
        label.size_hint_x = tam
        label.height = '30dp'
        return label

    def _criarBotao(self, texto):
        botao = Button(text=texto,
                       font_size='10sp',
                       size_hint_y = None,
                       height='30dp',
                       size_hint_x = .1)
        return botao










