from flask import Flask
from flask_restful import Resource, Api
from resources.hotel import Hoteis, Hotel

app = Flask(__name__)
api = Api(app)

# Configurações

# Rotas
api.add_resource(Hoteis,"/hoteis")
api.add_resource(Hotel,"/hoteis/<string:id_hotel>")

# Iniciar a aplicação
if __name__ == "__main__":
    app.run(debug=True)