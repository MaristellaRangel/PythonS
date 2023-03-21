CREATE DATABASE netflix;
USE netflix;
CREATE TABLE usuarios(
	idUsuario int auto_increment primary key,
    usuario varchar(50) not null,
    email varchar(100) not null,
    plano varchar(50),
    tipo varchar(50),
    idade int 
);

CREATE TABLE filmes(
	idFilme int auto_increment primary key,
    filme varchar(200),
    plano varchar(50),
    descricao varchar(255),
    classificacao int
);

INSERT INTO usuarios (usuario, email, plano, tipo, idade) VALUES
('Maristella', 'maristella@gmail.com', "premium", "admin", 18),
('Daniele', 'daniele@gmail.com', 'medium', 'user', 20); 

SELECT * FROM usuarios;

INSERT INTO filmes (filme, plano, descricao, classificacao) VALUES 
('O homem que viu o infinito', 'medium', 'xxxxxxx', 0),
('Coração valente', 'basic', 'xxxxxxx', 12);

SELECT * FROM filmes;
