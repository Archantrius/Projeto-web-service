import urllib.request
import json

BASE = "http://localhost:3000"


def req(metodo, caminho, corpo=None):
    data = json.dumps(corpo).encode() if corpo else None
    headers = {"Content-Type": "application/json"}
    r = urllib.request.Request(f"{BASE}{caminho}", data=data, headers=headers, method=metodo)
    with urllib.request.urlopen(r) as res:
        return json.loads(res.read())


# Listar monitores
monitores = req("GET", "/monitores")
print("=" * 40)
print("👦👧 MONITORES DETECTADOS (GET):")
print(monitores)

# Cadastrar novo monitor
novo = req("POST", "/monitores", {
    "nome": "Diego Rocha",
    "matricula": "20240099",
    "disciplina": "Redes de Computadores",
})
print("=" * 40)
print("😁 MONITOR(A) CADASTRADO (POST):")
print(novo)

# Atualizar
atualizado = req("PUT", f"/monitores/{novo['id']}", {"status": "inativo"})
print("=" * 40)
print("💾 SISTEMA ATUALIZADO (PUT):")
print(atualizado)

# Remover
req("DELETE", f"/monitores/{novo['id']}")
print("=" * 40)
print("❌ MONITOR(A) REMOVIDO(A) (DELETE)")
print("=" * 40)
