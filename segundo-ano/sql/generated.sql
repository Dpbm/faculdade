-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema exercicio
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema exercicio
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `exercicio` DEFAULT CHARACTER SET utf8 ;
USE `exercicio` ;

-- -----------------------------------------------------
-- Table `exercicio`.`produto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `exercicio`.`produto` (
  `idproduto` INT UNSIGNED NOT NULL,
  `descricao` VARCHAR(30) NOT NULL,
  `grupo` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idproduto`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `exercicio`.`almoxarifado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `exercicio`.`almoxarifado` (
  `idalmoxarifado` INT UNSIGNED NOT NULL,
  `nome` VARCHAR(9) NOT NULL,
  PRIMARY KEY (`idalmoxarifado`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `exercicio`.`produto_almoxarifado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `exercicio`.`produto_almoxarifado` (
  `idproduto` INT UNSIGNED NOT NULL,
  `idalmoxarifado` INT UNSIGNED NOT NULL,
  `qtde` INT UNSIGNED NOT NULL,
  `cadastro` DATE NOT NULL,
  `valor_unitario` DECIMAL(5,2) UNSIGNED NOT NULL,
  PRIMARY KEY (`idproduto`, `idalmoxarifado`),
  INDEX `fk_produto_has_almoxarifado_almoxarifado1_idx` (`idalmoxarifado` ASC),
  INDEX `fk_produto_has_almoxarifado_produto1_idx` (`idproduto` ASC),
  CONSTRAINT `fk_produto_has_almoxarifado_produto1`
    FOREIGN KEY (`idproduto`)
    REFERENCES `exercicio`.`produto` (`idproduto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_produto_has_almoxarifado_almoxarifado1`
    FOREIGN KEY (`idalmoxarifado`)
    REFERENCES `exercicio`.`almoxarifado` (`idalmoxarifado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `exercicio`.`almoxarifado_fone`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `exercicio`.`almoxarifado_fone` (
  `idtelefone` INT UNSIGNED NOT NULL,
  `idalmoxarifado` INT UNSIGNED NOT NULL,
  `telefone` VARCHAR(9) NOT NULL,
  PRIMARY KEY (`idtelefone`, `idalmoxarifado`),
  INDEX `fk_almoxarifado_fone_almoxarifado1_idx` (`idalmoxarifado` ASC),
  CONSTRAINT `fk_almoxarifado_fone_almoxarifado1`
    FOREIGN KEY (`idalmoxarifado`)
    REFERENCES `exercicio`.`almoxarifado` (`idalmoxarifado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
