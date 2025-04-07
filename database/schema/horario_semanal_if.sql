CREATE SCHEMA IF NOT EXISTS horario_semanal_if;

USE horario_semanal_if;

CREATE TABLE IF NOT EXISTS horarios (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome_da_turma VARCHAR(255),
	curso VARCHAR(255),
	disciplina VARCHAR(255),
	dia_da_semana VARCHAR(255),
	horario_da_aula VARCHAR(255),
	sala VARCHAR(255),
	professor VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS user (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	email VARCHAR(255),
	senha VARCHAR(255)
);