import peewee
from playhouse.mysql_ext import MySQLConnectorDatabase


class BaseE(peewee.Model):

    class Meta:
        database = MySQLConnectorDatabase('evento_ads',
                                          user='root',
                                          password='',
                                          host='localhost',
                                          port=3306,
                                          charset='utf8mb4')


class Autor(BaseE):
    nome = peewee.CharField()
    instituicao = peewee.CharField()
    email = peewee.CharField()

class Artigo(BaseE):
    titulo = peewee.CharField()
    palavras_chave = peewee.CharField()
    autor = peewee.ForeignKeyField(model=Autor, on_delete="CASCADE", backref="autor")

class Categoria(BaseE):
    nome = peewee.CharField(40)

class Comite(BaseE):
    nome = peewee.CharField(50)
    descricao = peewee.CharField(200)

class Convidado(BaseE):
    nome = peewee.CharField(50)
    formacao = peewee.CharField(40)
    data_Chegada = peewee.DateField()
    Data_Saida = peewee.TimeField()
    data_Voo_Chegada = peewee.DateField()
    data_Voo_Saida = peewee.DateField()
    hora_Voo_Chegada = peewee.TimeField()
    hora_Voo_Saida = peewee.TimeField()

class Evento(BaseE):
    recursos = peewee.CharField(400, null=True)
    tipo_evento = peewee.CharField(1)
    valor_inscricao = peewee.FloatField()

class Membro(BaseE):
    nome = peewee.CharField(50)
    instituicao = peewee.CharField(50, null = True)
    area_Espec = peewee.CharField(40)
    email = peewee.CharField(80)
    endereco_CEP = peewee.CharField(9)
    endereco_Numero = peewee.CharField(4)
    telefone = peewee.CharField(14)
    fax = peewee.CharField(15)

class Minicurso(BaseE):
    titulo = peewee.CharField(40)
    instituicao = peewee.CharField(100)
    tema = peewee.CharField(60)
    tipo = peewee.CharField(1)
    convidado = peewee.ForeignKeyField(model=Convidado, on_delete="CASCADE", backref="convidado")

class Palestras(BaseE):
    tema = peewee.CharField(60)
    titulo = peewee.CharField(40)
    instituicao = peewee.CharField(100)
    tipo = peewee.CharField(1)
    convidado = peewee.ForeignKeyField(model=Convidado, on_delete="CASCADE", backref="convidado")

class Participante(BaseE):
    nome = peewee.CharField(50)
    instituicao = peewee.CharField(100)
    endereco_cep = peewee.CharField(9)
    endereco_numero = peewee.CharField(4)
    email = peewee.CharField(80)
    categoria = peewee.ForeignKeyField(model=Categoria, on_delete="CASCADE", backref="categoria")

class Sala_auditorio(BaseE):
    nome = peewee.CharField(50)
    capacidade = peewee.IntegerField(4)

class SessoesTec(BaseE):
    descricao = peewee.CharField(200)
    tipo = peewee.CharField(1)
    autor_id = peewee.ForeignKeyField(model=Autor, on_delete="CASCADE", backref="autor")

class Tipo_Evento(BaseE):
    evento = peewee.ForeignKeyField(model=Evento, on_delete="CASCADE", backref="evento")
    sessoes_tecnicas = peewee.ForeignKeyField(model=SessoesTec, on_delete="NO ACTION", backref="sessoes tecnicas")
    palestras = peewee.ForeignKeyField(model=Palestras, on_delete="NO ACTION", backref="palestras")
    minicurso = peewee.ForeignKeyField(model=Minicurso, on_delete="NO ACTION", backref="minicursos")

class Agendar_local(BaseE):
    data = peewee.DateField()
    hora = peewee.TimeField()
    evento = peewee.ForeignKeyField(model=Evento, on_delete="CASCADE", backref="evento")
    membro = peewee.ForeignKeyField(model=Membro, on_delete="CASCADE", backref="membro")
    local = peewee.ForeignKeyField(model=Sala_auditorio, on_delete="CASCADE", backref="local")

class Analise_artigo(BaseE):
    comite = peewee.ForeignKeyField(model=Comite, on_delete="CASCADE", backref="comite")
    membro = peewee.ForeignKeyField(model=Membro, on_delete="CASCADE", backref="membro")
    artigo = peewee.ForeignKeyField(model=Artigo, on_delete="CASCADE", backref="artigo")
    nota = peewee.FloatField(4)
    selecionado = peewee.BooleanField(default=False)
    arquivo_final = peewee.BooleanField(default=False)
    data = peewee.DateField()
    hora = peewee.TimeField()

class Inscricao(BaseE):
    evento = peewee.ForeignKeyField(model=Evento, on_delete="CASCADE", backref="evento")
    participante = peewee.ForeignKeyField(model=Participante, on_delete="CASCADE", backref="participante")
    data = peewee.DateField()
    hora = peewee.TimeField()





