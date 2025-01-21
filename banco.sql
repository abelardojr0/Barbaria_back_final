CREATE TABLE barbeiros(
	id SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	cpf CHAR(11) NOT NULL UNIQUE,
	telefone VARCHAR(15) NOT NULL
);

CREATE TABLE servicos(
	id SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	descricao TEXT,
	valor NUMERIC(10,2) NOT NULL,
	porcentagem_barbeiro NUMERIC(5,2) NOT NULL
);

CREATE TABLE atendimentos(
	id SERIAL PRIMARY KEY,
	data_atendimento TIMESTAMP NOT NULL,
	id_barbeiro INT NOT NULL,
	FOREIGN KEY (id_barbeiro) REFERENCES barbeiros(id),
	id_servico INT NOT NULL,
	FOREIGN KEY (id_servico) REFERENCES servicos(id)
);


INSERT INTO barbeiros (nome, cpf, telefone) VALUES 
('João Silva', '67834512288', '988776655'),
('Maria', '67834512280', '988776600'),
('Luiz Chagas', '67834512265', '988776611')




INSERT INTO servicos (nome, descricao, valor, porcentagem_barbeiro) VALUES 
('Corte de Masculino', 'Corte Tesoura ou Degradê', 60.00, 75.00),
('Barba', 'Aparar ou Fazer Barba', 39.99, 60.00)




INSERT INTO atendimentos (data_atendimento, id_barbeiro, id_servico) VALUES 
('2024-12-03 19:14:00', 3, 1)



