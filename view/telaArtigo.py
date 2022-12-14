from functools import partial

from kivy.uix.label import Label
from kivy.uix.popup import Popup

from control.artigoCtrl import ArtigoCtrl



class ViewArtigo:

    def __init__(self, gerenc_tela):
        self._gt = gerenc_tela
        self._telacad = self._gt.get_screen("CadastroArtigo")
        self._telalistar = self._gt.get_screen("ListarArtigos")

    def cad_atual_artigo(self):
        control = ArtigoCtrl()
        try:
            id_artigo = self._telacad.lbl_id_artigo.text
            nome_artigo = self._telacad.txi_titulo.text
            palavras_chave = self._telacad.txi_palavras_chave.text
            autor = self._telacad.sp_autor.text
            if self._telacad.bt_cad_atual.text == "Excluir":
                result = control.excluirArtigo(id_artigo)
                self.busca_artigos()
                self._gt.current = "ListarArtigos"
            else:
                result = control.salvarArtigo(id=id_artigo,
                                                        titulo=nome_artigo,
                                                        palavras_chave=palavras_chave,
                                                        autor=autor)
            self._popJanela(result)
            self._limpar_tela()
            self._telacad.txi_titulo.focus = True
        except Exception as e:
            print(str(e))
            self._popJanela(f"Não foi possível {self._telacad.bt_cad_atual.text} o registro do artigo!")

    def _limpar_tela_listar(self):
        self._telalistar.txi_pesq_nome.text = ""
        cabecalho = [
            self._telalistar.ids.col_id,
            self._telalistar.ids.col_titulo,
            self._telalistar.ids.col_palavras_chave,
            self._telalistar.ids.col_autor,
            self._telalistar.ids.lbl_atual,
            self._telalistar.ids.lbl_excluir
        ]
        self._telalistar.layout_lista_artigos.clear_widgets()
        for c in cabecalho:
            self._telalistar.layout_lista_artigos.add_widget(c)

    def busca_artigos(self, nome=""):
        try:
            control = ArtigoCtrl()
            resultado = control.buscar_artigo(titulo=nome)
            self._limpar_tela_listar()
            for res in resultado:
                res['btAtualizar'].bind(on_release=partial(self._gt.tela_cadastro_artigo, res['lblId'].text))
                res['btExcluir'].bind(on_release=partial(self._gt.tela_cadastro_artigo, res['lblId'].text))
                self._telalistar.layout_lista_artigos.add_widget(res['lblId'])
                self._telalistar.layout_lista_artigos.add_widget(res['lblTitulo'])
                self._telalistar.layout_lista_artigos.add_widget(res['lblPlCh'])
                self._telalistar.layout_lista_artigos.add_widget(res['lblAutor'])
                self._telalistar.layout_lista_artigos.add_widget(res['btAtualizar'])
                self._telalistar.layout_lista_artigos.add_widget(res['btExcluir'])
        except Exception as e:
            print(e)

    def montar_tela_at(self, id_artigo="", botao=None):
        control = ArtigoCtrl()
        self._montar_spinner()
        artigos = []
        if id_artigo:
            artigos = control.buscar_artigo(id=id_artigo)
        if artigos:
            for a in artigos:
                self._telacad.lbl_id_artigo.text = a["lblId"].text
                self._telacad.txi_titulo.text = a["lblTitulo"].text
                self._telacad.txi_palavras_chave.text = a["lblPlCh"].text
                self._telacad.sp_autor.text = a["lblAutor"].text
                self._telacad.bt_cad_atual.text = botao.text

    def _montar_spinner(self):
        lista_valores = self._buscar_autores_tela()
        self._telacad.sp_autor.values = lista_valores


    def _buscar_autores_tela(self):
        control = ArtigoCtrl()
        autores = control.buscarAutores()
        nomesAutores =[]
        for autor in autores:
            nomesAutores.append(autor['nome'])
        return tuple(nomesAutores)

    def _limpar_tela(self):
        self._telacad.lbl_id_artigo.text = ""
        self._telacad.txi_titulo.text = ""
        self._telacad.txi_palavras_chave.text = ""
        self._telacad.sp_autor.text = "Selecione..."
        self._telacad.bt_cad_atual.text = "Cadastrar"

    def _popJanela(self, texto=""):
        popup = Popup(title='Informação', content=Label(text=texto), auto_dismiss=True)
        popup.size_hint = (0.98, 0.4)
        popup.open()
