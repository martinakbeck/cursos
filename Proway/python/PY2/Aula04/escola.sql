-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 09-Jan-2022 às 16:20
-- Versão do servidor: 10.4.14-MariaDB
-- versão do PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `escola`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `cad_alunos`
--

CREATE TABLE `cad_alunos` (
  `id_cad_aluno` int(11) NOT NULL,
  `nome_cad_aluno` varchar(20) NOT NULL,
  `sexo_cad_aluno` char(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `cad_categorias`
--

CREATE TABLE `cad_categorias` (
  `id_cad_categoria` int(11) NOT NULL,
  `nome_cad_categoria` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `cad_cursos`
--

CREATE TABLE `cad_cursos` (
  `id_cad_curso` int(11) NOT NULL,
  `nome_cad_curso` varchar(50) NOT NULL,
  `carga_horaria_cad_curso` int(11) NOT NULL,
  `id_cad_categoria` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `cad_professores`
--

CREATE TABLE `cad_professores` (
  `id_cad_professor` int(11) NOT NULL,
  `nome_cad_professor` varchar(20) NOT NULL,
  `sexo_cad_professor` char(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `cad_vendas`
--

CREATE TABLE `cad_vendas` (
  `id_cad_venda` int(11) NOT NULL,
  `id_cad_curso` int(11) NOT NULL,
  `id_cad_vendedor` int(11) NOT NULL,
  `id_cad_aluno` int(11) NOT NULL,
  `id_cad_professor` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `cad_vendedores`
--

CREATE TABLE `cad_vendedores` (
  `id_cad_vendedor` int(11) NOT NULL,
  `nome_cad_vendedor` varchar(20) NOT NULL,
  `sexo_cad_vendedor` char(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `cad_alunos`
--
ALTER TABLE `cad_alunos`
  ADD PRIMARY KEY (`id_cad_aluno`);

--
-- Índices para tabela `cad_categorias`
--
ALTER TABLE `cad_categorias`
  ADD PRIMARY KEY (`id_cad_categoria`);

--
-- Índices para tabela `cad_cursos`
--
ALTER TABLE `cad_cursos`
  ADD PRIMARY KEY (`id_cad_curso`),
  ADD KEY `fk_id_cad_categoria` (`id_cad_categoria`);

--
-- Índices para tabela `cad_professores`
--
ALTER TABLE `cad_professores`
  ADD PRIMARY KEY (`id_cad_professor`);

--
-- Índices para tabela `cad_vendas`
--
ALTER TABLE `cad_vendas`
  ADD PRIMARY KEY (`id_cad_venda`),
  ADD KEY `fk_id_cad_curso` (`id_cad_curso`),
  ADD KEY `fk_id_cad_vendedor` (`id_cad_vendedor`),
  ADD KEY `fk_id_cad_aluno` (`id_cad_aluno`),
  ADD KEY `fk_id_cad_professor` (`id_cad_professor`);

--
-- Índices para tabela `cad_vendedores`
--
ALTER TABLE `cad_vendedores`
  ADD PRIMARY KEY (`id_cad_vendedor`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `cad_alunos`
--
ALTER TABLE `cad_alunos`
  MODIFY `id_cad_aluno` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `cad_categorias`
--
ALTER TABLE `cad_categorias`
  MODIFY `id_cad_categoria` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `cad_cursos`
--
ALTER TABLE `cad_cursos`
  MODIFY `id_cad_curso` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `cad_professores`
--
ALTER TABLE `cad_professores`
  MODIFY `id_cad_professor` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `cad_vendas`
--
ALTER TABLE `cad_vendas`
  MODIFY `id_cad_venda` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `cad_vendedores`
--
ALTER TABLE `cad_vendedores`
  MODIFY `id_cad_vendedor` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `cad_cursos`
--
ALTER TABLE `cad_cursos`
  ADD CONSTRAINT `fk_id_cad_categoria` FOREIGN KEY (`id_cad_categoria`) REFERENCES `cad_categorias` (`id_cad_categoria`);

--
-- Limitadores para a tabela `cad_vendas`
--
ALTER TABLE `cad_vendas`
  ADD CONSTRAINT `fk_id_cad_aluno` FOREIGN KEY (`id_cad_aluno`) REFERENCES `cad_alunos` (`id_cad_aluno`),
  ADD CONSTRAINT `fk_id_cad_curso` FOREIGN KEY (`id_cad_curso`) REFERENCES `cad_cursos` (`id_cad_curso`),
  ADD CONSTRAINT `fk_id_cad_professor` FOREIGN KEY (`id_cad_professor`) REFERENCES `cad_professores` (`id_cad_professor`),
  ADD CONSTRAINT `fk_id_cad_vendedor` FOREIGN KEY (`id_cad_vendedor`) REFERENCES `cad_vendedores` (`id_cad_vendedor`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
