from src import ma  # Importa a instância Marshmallow para serialização
from src.models.usuario_model import Usuario  # Importa o modelo de usuário
from marshmallow import fields  # Importa tipos de campos para o schema

class UsuarioSchema(ma.SQLAlchemyAutoSchema):  # Schema para serializar/deserializar o modelo Usuario
    class Meta:
        model = Usuario.usuario  # Define o modelo associado ao schema
        fields = ('id', 'none', 'email', ' telefone', 'senha')  # Campos que serão serializados
        # Atenção: 'none' provavelmente deveria ser 'nome' e ' telefone' tem espaço extra
    nome = fields.String(required=True)  # Campo nome obrigatório
    email = fields.String(required=True)  # Campo email obrigatório
    telefone = fields.String(required=True)  # Campo telefone obrigatório
    senha = fields.String(required=True)  # Campo senha obrigatório 