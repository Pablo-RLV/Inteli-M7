DROP TABLE IF EXISTS minhas_notas ;

CREATE TABLE minhas_notas (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT NOT null,
    data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);