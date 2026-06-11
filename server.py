from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Banco de dados em memória
monitores = [
    {"id": "1", "nome": "Ana Souza",      "matricula": "20220001", "disciplina": "Cálculo I",    "status": "ativo"},
    {"id": "2", "nome": "Bruno Ferreira", "matricula": "20210042", "disciplina": "POO",           "status": "ativo"},
    {"id": "3", "nome": "Clara Mendes",   "matricula": "20230015", "disciplina": "Banco de Dados","status": "inativo"},
]


@app.route("/monitores", methods=["GET"])
def listar():
    return jsonify(monitores)


@app.route("/monitores/<id>", methods=["GET"])
def buscar(id):
    monitor = next((m for m in monitores if m["id"] == id), None)
    if not monitor:
        return jsonify({"erro": "Monitor não encontrado"}), 404
    return jsonify(monitor)


@app.route("/monitores", methods=["POST"])
def criar():
    dados = request.get_json()
    novo = {
        "id":         str(uuid.uuid4()),
        "nome":       dados["nome"],
        "matricula":  dados["matricula"],
        "disciplina": dados["disciplina"],
        "status":     dados.get("status", "ativo"),
    }
    monitores.append(novo)
    return jsonify(novo), 201


@app.route("/monitores/<id>", methods=["PUT"])
def atualizar(id):
    monitor = next((m for m in monitores if m["id"] == id), None)
    if not monitor:
        return jsonify({"erro": "Monitor não encontrado"}), 404
    dados = request.get_json()
    monitor.update({k: v for k, v in dados.items() if k in monitor})
    return jsonify(monitor)


@app.route("/monitores/<id>", methods=["DELETE"])
def remover(id):
    monitor = next((m for m in monitores if m["id"] == id), None)
    if not monitor:
        return jsonify({"erro": "Monitor não encontrado"}), 404
    monitores.remove(monitor)
    return jsonify({"mensagem": "Monitor removido"})


if __name__ == "__main__":
    app.run(port=3000, debug=True)
