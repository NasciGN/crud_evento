import locale

from kivy.uix.button import Button
from kivy.uix.label import Label
from peewee import ModelSelect

from model.models import Autor, Artigo


class ArtigoCtrl:

    def salvarArtigo(self, id=None, titulo=None, palavras_chave=None, autor=None):
        try:
            A = Autor.get(nome=autor)
            if id:
                artigo = Artigo.get_by_id(id)
                artigo.titulo = titulo
                artigo.palavras_chave = palavras_chave
                artigo.autor = A.id

            else:
                artigo = Artigo(titulo=titulo, palavras_chave=palavras_chave, autor=A.id)
            artigo.save()
            return "O artigo foi salvo com sucesso!"
        except Exception as e:
            print(e)
            return "Não foi possível salvar o registro do artigo!"

    def excluirArtigo(self, id):
        try:
            artigo = Artigo.get_by_id(id)
            artigo.delete_instance()
            return "Artigo excluído com sucesso!"
        except Exception as e:
            print(e)
            return "Não foi possível excluir o Artigo!"

    def buscar_artigo(self, id=None, titulo=None):
        try:
            if id:
                artigo = Artigo.get_by_id(id)
            elif titulo:
                artigo = Artigo.select().where(Artigo.titulo % f'%{titulo}%')
            else:
                artigo = Artigo.select()
        except Exception as e:
            print(e)
            return None
        itens = []
        if type(artigo) is Artigo:
            itens.append(self._montar_artigo(artigo.id, artigo.titulo, artigo.palavras_chave, artigo.autor.nome))
        elif type(artigo) is ModelSelect:
            for a in artigo:
                itens.append(self._montar_artigo(a.id, a.titulo, a.palavras_chave, a.autor.nome))
        return itens

    def _montar_artigo(self, id, titulo, palavras_chave, autor):
        meuartigo = {
            'lblId': self._criarLabel(id, 0.1),
            'lblTitulo': self._criarLabel(titulo, 0.4),
            'lblPlCh': self._criarLabel(palavras_chave, 0.1),
            'lblAutor': self._criarLabel(autor,0.1),
            'btAtualizar': self._criarBotao("Atualizar"),
            'btExcluir': self._criarBotao("Excluir")
        }
        return meuartigo

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

    def buscarAutores(self):
        autoresbanco = Autor.select()
        autores = []
        for autor in autoresbanco:
            autores.append({"id": autor.id, "nome": autor.nome})
        return autores
