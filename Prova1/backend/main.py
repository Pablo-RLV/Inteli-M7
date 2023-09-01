from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import sqlite3

app = FastAPI()

# CORS
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost",
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de dados para as operações CRUD
class Usuario(BaseModel):
    nome: str
    nome_de_usuario: str
    senha: str

# Operação de criação (Create)
@app.post("/usuarios/")
def criar_usuario(usuario: Usuario):
    cursor.execute('''
        INSERT INTO usuarios (nome, nome_de_usuario, senha)
        VALUES (?, ?, ?)
    ''', (usuario.nome, usuario.nome_de_usuario, usuario.senha))
    conn.commit()
    return {"mensagem": "Usuário criado com sucesso"}

# Operação de leitura (Read)
@app.get("/usuarios/{usuario_id}")
def ler_usuario(usuario_id: int):
    cursor.execute('SELECT * FROM usuarios WHERE id = ?', (usuario_id,))
    usuario = cursor.fetchone()
    if usuario:
        return {"id": usuario[0], "nome": usuario[1], "nome_de_usuario": usuario[2]}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# Operação de leitura (Read)
@app.get("/usuarios/")
def ler_usuarios():
    cursor.execute('SELECT * FROM usuarios')
    ler_usuarios = cursor.fetchall()
    if len:
        return ler_usuarios
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# Operação de atualização (Update)
@app.put("/usuarios/{usuario_id}")
def atualizar_usuario(usuario_id: int, usuario: Usuario):
    cursor.execute('''
        UPDATE usuarios
        SET nome = ?, nome_de_usuario = ?, senha = ?
        WHERE id = ?
    ''', (usuario.nome, usuario.nome_de_usuario, usuario.senha, usuario_id))
    conn.commit()
    return {"mensagem": "Usuário atualizado com sucesso"}

# Operação de exclusão (Delete)
@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int):
    cursor.execute('DELETE FROM usuarios WHERE id = ?', (usuario_id,))
    conn.commit()
    return {"mensagem": "Usuário deletado com sucesso"}

# Configuração do banco de dados SQLite
db_path = "usuarios.db"
conn = sqlite3.connect(db_path, check_same_thread=False)
cursor = conn.cursor()

# Criação da tabela de usuários
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        nome_de_usuario TEXT NOT NULL,
        senha TEXT NOT NULL
    )
''')
conn.commit()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)