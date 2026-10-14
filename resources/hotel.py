from flask_restful import Resource

lista_hoteis = [
    {"hotel_id": "SFC", "nome": "Hotel Santos FC", "estrelas": 5, "diaria": 79.99, "Cidade": "Santos"},
    {"hotel_id": "SPC", "nome": "Hotel São Paulo FC", "estrelas": 3.5, "diaria": 49.99, "Cidade": "São Paulo"},
    {"hotel_id": "FLA", "nome": "Hotel Flamengo FC", "estrelas": 4.5, "diaria": 99.99, "Cidade": "Rio de Janeiro"}
]

class Hoteis(Resource):
    def get(self):
        return { "hoteis": lista_hoteis }