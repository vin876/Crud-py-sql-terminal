-- Criação de banco de dados, se ainda não existir
CREATE DATABASE IF NOT EXISTS tarefas_db;

-- Selecione o banco de dados para uso
USE tarefas_db;

-- Criação da tabela de tarefas
CREATE TABLE IF NOT EXISTS tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT,
    status VARCHAR(50) DEFAULT 'pendente'
);
