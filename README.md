# 📚 Sistema de Gerenciamento de Monitores

Este projeto implementa uma API simples em **Flask** para gerenciar monitores acadêmicos, junto com um cliente em **Python** que consome essa API utilizando `urllib.request`.

## 🚀 Funcionalidades

- **Listar monitores**: retorna todos os monitores cadastrados.  
- **Buscar monitor**: retorna um monitor específico pelo seu `id`.  
- **Cadastrar monitor**: adiciona um novo monitor ao sistema.  
- **Atualizar monitor**: altera informações de um monitor existente.  
- **Remover monitor**: exclui um monitor do sistema.  

---

## 📂 Estrutura do Projeto

```
├── Client.py   # Cliente que consome a API
├── Server.py   # Servidor Flask com a API REST
```

---

## ⚙️ Como executar

### 1. Clonar o repositório
```bash
git clone https://github.com/Archantrius/Projeto-web-service.git
cd Projeto-web-service
```

### 2. Instalar dependências
Certifique-se de ter o **Python 3** instalado e o **Flask**:
```bash
pip install flask
```

### 3. Iniciar o servidor
Execute o arquivo `server.py`:
```bash
python server.py
```
O servidor estará disponível em `http://localhost:3000`.

### 4. Executar o cliente
Em outro terminal, rode:
```bash
python client.py
```

---

## 🔗 Endpoints da API

| Método | Endpoint            | Descrição                          |
|--------|---------------------|------------------------------------|
| **GET**    | `/monitores`         | Listar todos os monitores |
| **GET**    | `/monitores/<id>`    | Buscar monitor por ID |
| **POST**   | `/monitores`         | Cadastrar novo monitor |
| **PUT**    | `/monitores/<id>`    | Atualizar monitor existente |
| **DELETE** | `/monitores/<id>`    | Remover monitor |

---

## 🧑‍💻 Exemplo de fluxo (Client.py)

1. **Listar monitores existentes**  
2. **Cadastrar novo monitor**  
3. **Atualizar status do monitor**  
4. **Remover monitor cadastrado**  

---

## 📌 Observações

- O banco de dados é **em memória**, ou seja, os dados são perdidos ao reiniciar o servidor.  
- IDs são gerados automaticamente com `uuid`.  
- O cliente utiliza `urllib.request` para realizar requisições HTTP.  

---
