from ..models import usuario_model  # Importa o modelo de usuário
from src import db  # Importa a instância do banco de dados
from ..schemas import usuario_schema  # Importa o schema para serialização de usuário


def cadastrar_usuario(usuario):
    # Cria uma instância do usuário com os dados recebidos
    usuario_db = usuario_model.Usuario(nome=usuario.nome, email=usuario.email, telefone=usuario.telefone, senha=usuario.senha)
    # Criptografa a senha do usuário
    usuario_db.gen_senha(usuario.senha)
    db.sessin.add(usuario_db)  # Adiciona o usuário ao banco de dados (possível erro: 'sessin' deveria ser 'session')
    db.session.commit()  # Salva as alterações no banco de dados
    return usuario_db  # Retorna o usuário cadastrado
    
def listar_usuarios():
    usuario = usuario_model.Usuario.query.all()  # Busca todos os usuários
    schema = usuario_schema.UsuarioSchema(many=True)  # Instancia schema para múltiplos usuários
    return usuario_model.Usuario.query.all()  # Retorna todos os usuários

def listar_usuario_id(id):
    return usuario_model.Usuario.query.all()  # (Possível erro: deveria buscar por id)
    
def excluir_usuario(id):  # Função para excluir usuário pelo id
    ...  
    
def editar_usuario(id):  # Função para editar usuário pelo id
    ... 
    
def listar_usuario_email(email):  # Função para listar usuário por email
    return usuario_model.Usuario.query.filter_by(email=email).first()
    