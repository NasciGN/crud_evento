from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.screenmanager import Screen, ScreenManager

from telaAutor import ViewAutor
from telaArtigo import ViewArtigo


class TelaInicial(Screen):
    pass


class CadastroAutor(Screen):
    lbl_id_autor = ObjectProperty(None)
    txi_nome = ObjectProperty(None)
    txi_instituicao = ObjectProperty(None)
    txi_email = ObjectProperty(None)
    bt_cad_atual: ObjectProperty(None)


class ListarAutores(Screen):
    id_autor = ObjectProperty(None)
    col_id = ObjectProperty(None)
    col_nome = ObjectProperty(None)
    col_instituicao = ObjectProperty(None)
    col_email = ObjectProperty(None)
    grid_lista = ObjectProperty(None)


class CadastroArtigo(Screen):
    lbl_id: NumericProperty()
    txi_nome: StringProperty()
    txi_palavras_chave: StringProperty()
    sp_autor: ObjectProperty()


class ListarArtigos(Screen):
    txi_pesq_nome: StringProperty()
    gl_pesquisa_nome: ObjectProperty()
    layout_pesq_id: ObjectProperty()
    layout_pesq_nome: ObjectProperty()
    layout_lista_artigos: ObjectProperty()
    pesq = ObjectProperty()


class GerenciaTelas(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._tela_autor = ViewAutor(self)
        self._tela_artigo = ViewArtigo(self)

    def tela_inicial(self):
        self.current = "TelaInicial"

    def tela_cadastro_autor(self, id=None, botao=None):
        self.current = 'CadastroAutor'
        self._tela_autor.montarTelaAt(id, botao)

    def tela_listar_autor(self):
        self.current = "ListarAutores"
        self._tela_autor._limpar_tela_listar()

    def cadastrar_atualizar_autor(self):
        self._tela_autor.cad_atual_autor()

    def buscar_autores(self):
        self._tela_autor.busca_autores()

    def tela_cadastro_artigo(self, id="", botao='None'):
        self.current = "CadastroArtigo"
        self._tela_artigo.montar_tela_at(id, botao)

    def tela_listar_artigos(self):
        self.current = "ListarArtigos"
        self._tela_artigo._limpar_tela_listar()

    def cadastrar_atualizar_artigo(self):
        self._tela_artigo.cad_atual_artigo()

    def buscar_artigos(self):
        self._tela_artigo.busca_artigos()

    def buscar_artigos_nome(self, nome=""):
        self._tela_artigo.busca_artigos(nome)

