from functools import partial

from kivy.uix.label import Label
from kivy.uix.popup import Popup

from control.autorCtrl import AutorCtrl


class ViewAutor:

    def __init__(self, gerenc_tela):
        self._gt = gerenc_tela
        self._telacad = self._gt.get_screen("CadastroAutor")
        self._telalistar = self._gt.get_screen("ListarAutores")

    def cad_atual_autor(self):
        result = ""
        try:
            id_autor = self._telacad.lbl_id_autor.text
            nome = self._telacad.txi_nome.text
            instituicao = self._telacad.txi_instituicao.text
            email = self._telacad.txi_email.text
            control = AutorCtrl()
            if self._telacad.bt_cad_atual.text == "Excluir":
                result = control.excluirAutor(id_autor)
                self.busca_autores()
                self._gt.current = "ListarAutores"
            else:
                result = control.salvarAutor(nome=nome, instituicao=instituicao, id=id_autor, email=email)
            self._popJanela(result)
            self._limparTela()

        except Exception as e:
            print(e)
            self._telacad._popJanela(f"Não foi possível {self._telacad.bt_cad_atual.text} o registro do autor!")

    def montarTelaAt(self, id=None, botao=None):
        control = AutorCtrl()
        autor = None
        if id:
            autor = control.buscar_por_id(id)
        if autor:
            for A in autor:
                print(A)
                self._telacad.lbl_id_autor.text = A['lblId'].text
                self._telacad.txi_nome.text = A['lblNome'].text
                self._telacad.txi_instituicao.text = A['lblInstituicao'].text
                self._telacad.txi_email.text = A['lblEmail'].text
                self._telacad.bt_cad_atual.text = botao.text

    def _limparTela(self):
        self._telacad.lbl_id_autor.text = ""
        self._telacad.txi_nome.text = ""
        self._telacad.txi_instituicao.text = ""
        self._telacad.txi_email.text = ""
        self._telacad.bt_cad_atual.text = "Cadastrar"

    def _popJanela(self, texto=""):
        popup = Popup(title='Informação', content=Label(text=texto), auto_dismiss=True)
        popup.size_hint = (0.98, 0.4)
        popup.open()


    def _limpar_tela_listar(self):
        cabecalho = [
            self._telalistar.col_id,
            self._telalistar.col_nome,
            self._telalistar.col_instituicao,
            self._telalistar.col_email,
            self._telalistar.lbl_atualizar,
            self._telalistar.lbl_excluir
        ]
        self._telalistar.grid_lista.clear_widgets()
        for c in cabecalho:
            self._telalistar.grid_lista.add_widget(c)

    def busca_autores(self):
        try:
            control = AutorCtrl()
            idPesq = self._telalistar.id_autor.text
            if idPesq:
                resultado = control.buscar_por_id(idPesq)
            else:
                resultado = control.buscar_todas()
            print(f"Testando a funcao de busca_autores: {resultado[0]}")
            self._limpar_tela_listar()
            for res in resultado:
                res['btAtualizar'].bind(on_release=partial(self._gt.tela_cadastro_autor, res['lblId'].text))
                res['btExcluir'].bind(on_release=partial(self._gt.tela_cadastro_autor, res['lblId'].text))
                self._telalistar.grid_lista.add_widget(res['lblId'])
                self._telalistar.grid_lista.add_widget(res['lblNome'])
                self._telalistar.grid_lista.add_widget(res['lblInstituicao'])
                self._telalistar.grid_lista.add_widget(res['lblEmail'])
                self._telalistar.grid_lista.add_widget(res['btAtualizar'])
                self._telalistar.grid_lista.add_widget(res['btExcluir'])
        except Exception as e:
            print(e)


