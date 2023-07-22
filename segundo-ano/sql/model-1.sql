-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema aula
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema aula
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `aula` DEFAULT CHARACTER SET utf8 ;
USE `aula` ;

-- -----------------------------------------------------
-- Table `aula`.`Estado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aula`.`Estado` (
  `uf` VARCHAR(2) NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`uf`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aula`.`Cidade`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aula`.`Cidade` (
  `codigo` INT NOT NULL,
  `nome` VARCHAR(80) NOT NULL,
  `uf` VARCHAR(2) NOT NULL,
  PRIMARY KEY (`codigo`),
  INDEX `fk_Cidade_Estado_idx` (`uf` ASC),
  CONSTRAINT `fk_Cidade_Estado`
    FOREIGN KEY (`uf`)
    REFERENCES `aula`.`Estado` (`uf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aula`.`Deposito`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aula`.`Deposito` (
  `iddeposito` INT NOT NULL,
  `descricao` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`iddeposito`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aula`.`Produto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aula`.`Produto` (
  `idproduto` INT NOT NULL,
  `descricao` VARCHAR(45) NOT NULL,
  `valor` DECIMAL(9,2) NOT NULL,
  PRIMARY KEY (`idproduto`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aula`.`estoque`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aula`.`estoque` (
  `iddeposito` INT NOT NULL,
  `idproduto` INT NOT NULL,
  `qtde` INT NOT NULL,
  PRIMARY KEY (`iddeposito`, `idproduto`),
  INDEX `fk_Deposito_has_Produto_Produto1_idx` (`idproduto` ASC),
  INDEX `fk_Deposito_has_Produto_Deposito1_idx` (`iddeposito` ASC),
  CONSTRAINT `fk_Deposito_has_Produto_Deposito1`
    FOREIGN KEY (`iddeposito`)
    REFERENCES `aula`.`Deposito` (`iddeposito`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Deposito_has_Produto_Produto1`
    FOREIGN KEY (`idproduto`)
    REFERENCES `aula`.`Produto` (`idproduto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
