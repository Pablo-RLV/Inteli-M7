SERVIDOR = 'http://localhost:8000';

async function criarUsuario() {
    const nome = document.getElementById('nome').value;
    const nome_de_usuario = document.getElementById('nome_de_usuario').value;
    const senha = document.getElementById('senha').value;
    const response = await fetch(SERVIDOR+'/usuarios/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nome, nome_de_usuario, senha })
    });

    const data = await response.json();
    alert(data.mensagem);
}

async function buscarUsuario() {
    try{
        const usuario_id = document.getElementById('usuario_id').value;
        if (!usuario_id)
            throw new Error('ID do usuário não informado');
        const response = await fetch(`${SERVIDOR}/usuarios/${usuario_id}`, {method:'GET'});
        const data = await response.json();
        if (response.status == 404)
            throw new Error('Usuário não encontrado');
        const usuarioInfo = document.getElementById('usuario_info');
        usuarioInfo.textContent = `ID: ${data.id}, Nome: ${data.nome}, Nome de Usuário: ${data.nome_de_usuario}`;
    } catch (error) {
        alert(error);
    }
}

async function atualizarUsuario() {
    const usuario_id = document.getElementById('usuario_id_atualizar').value;
    const nome = document.getElementById('nome_atualizar').value;
    const nome_de_usuario = document.getElementById('nome_de_usuario_atualizar').value;
    const senha = document.getElementById('senha_atualizar').value;

    const response = await fetch(`${SERVIDOR}/usuarios/${usuario_id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nome, nome_de_usuario, senha })
    });

    const data = await response.json();
    alert(data.mensagem);
}

async function deletarUsuario() {
    const usuario_id = document.getElementById('usuario_id_deletar').value;
    const response = await fetch(`${SERVIDOR}/usuarios/${usuario_id}`, {
        method: 'DELETE'
    });

    const data = await response.json();
    alert(data.mensagem);
}
