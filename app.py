from api import create_app
from flask_cors import CORS

app = create_app()
CORS(app, resources={r"/api/*": {"origins": "*"}})  # Permite todas as origens para rotas começando com /api/  

if __name__ == '__main__':
    app.run(debug=True)
