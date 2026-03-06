from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!!!</h1>"


@app.route("/curso")
def fer():
    return "<h1>Desenvolvimento de sistemas, Fernanda</h1>"


@app.route("/cidade")
def pira():
    
    dados = {
        "nome": "Piracicaba",
        "estado": "São Paulo",
        "população": 423000,
        "fundação": "1767"
    }

    return dados

if __name__ == "__main__":
    app.run(debug=True)
