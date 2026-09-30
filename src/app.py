from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "projeto": "DevSecOps Scan",
        "status": "Aplicação funcionando"
    })


@app.route("/hello")
def hello():
    nome = request.args.get("nome", "Visitante")

    return jsonify({
        "mensagem": f"Olá, {nome}!"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
