from flask_restful import Resource  # Importa a classe base para recursos RESTful
from marshmallow import ValidationError  # Importa exceção para validação de dados
from src.schemas import usuario_schema  # Importa o schema do usuário para serialização
from flask import request, jsonify, make_response  # Importa funções do Flask para requisições e respostas
from src.services import usuario_services  # Importa serviços relacionados ao usuário
from src import api  # Importa a instância da API para adicionar recursos

 # POST-GET-PUT-DELETE
 # Lidar com todos os usuários
class UsuarioList(Resource):  # Recurso para operações com lista de usuários
    def get(self):  # Método GET para listar usuários
        usuario = usuario_services.listar_usuario()  # Busca usuários cadastrados
        
        if not usuario:
            return make_response(jsonify({'message':'Não existe usuarios cadastrado'}))  # Retorna mensagem se não houver usuários
        
        schema = usuario_schema.UsuarioSchema(many=True)  # Instancia schema para múltiplos usuários
        
        return make_response(jsonify(schema.dump(usuario)), 200)  # Retorna lista de usuários serializada
    
    def post(self):  # Método POST para criar novo usuário
        ...  
        
api.add_resource(UsuarioList, '/usuario')  # Adiciona o recurso à rota '/usuario'