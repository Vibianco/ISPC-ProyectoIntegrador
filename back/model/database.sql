CREATE SCHEMA IF NOT EXISTS `mirifa` DEFAULT CHARACTER SET utf8mb4 ;
USE `mirifa` ;

CREATE TABLE IF NOT EXISTS `mirifa`.`provincia` (
  `id_provincia` INT(4) NOT NULL,
  `provincia` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id_provincia`));
  
CREATE TABLE IF NOT EXISTS `mirifa`.`usuario` (
  `id_usuario` INT(11) NOT NULL,
  `dni` INT(8) NOT NULL,
  `nombre` VARCHAR(50) NOT NULL,
  `apellido` VARCHAR(50) NOT NULL,
  `telefono` VARCHAR(15) NOT NULL,
  `id_provincia` INT(4) NOT NULL,
  `ciudad` VARCHAR(45) NOT NULL,
  `usuario` VARCHAR(60) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE INDEX `id_usuario_UNIQUE` (`id_usuario` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `usuario_UNIQUE` (`usuario` ASC) VISIBLE,
  INDEX `id_provincia_idx` (`id_provincia` ASC) VISIBLE,
  CONSTRAINT `id_provincia`
    FOREIGN KEY (`id_provincia`)
    REFERENCES `mirifa`.`provincia` (`id_provincia`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);

  CREATE TABLE IF NOT EXISTS `mirifa`.`medio_pago` (
  `id_medio_pago` INT(4) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_medio_pago`));
  
CREATE TABLE IF NOT EXISTS `mirifa`.`factura` (
  `id_factura` BIGINT(20) NOT NULL,
  `id_usuario` INT(11) NOT NULL,
  `total` INT(11) NOT NULL,
  `fecha` DATE NOT NULL,
  `fact_id_provincia` INT(4) NOT NULL,
  `id_medio_pago` INT(4) NOT NULL,
  PRIMARY KEY (`id_factura`),
  INDEX `id_usuario_idx` (`id_usuario` ASC) VISIBLE,
  INDEX `id_provincia_idx` (`fact_id_provincia` ASC) VISIBLE,
  INDEX `id_medio_pago_idx` (`id_medio_pago` ASC) VISIBLE,
  CONSTRAINT `id_usuario`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `mirifa`.`usuario` (`id_usuario`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `fact_id_provincia`
    FOREIGN KEY (`fact_id_provincia`)
    REFERENCES `mirifa`.`provincia` (`id_provincia`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `id_medio_pago`
    FOREIGN KEY (`id_medio_pago`)
    REFERENCES `mirifa`.`medio_pago` (`id_medio_pago`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);
 
 CREATE TABLE IF NOT EXISTS `mirifa`.`rifa` (
  `id_rifa` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre_sorteo` VARCHAR(100) NOT NULL,
  `motivo` VARCHAR(100) NOT NULL,
  `organizador` VARCHAR(45) NOT NULL,
  `premio1` VARCHAR(100) NOT NULL,
  `premio2` VARCHAR(100) NULL,
  `premio3` VARCHAR(100) NULL,
  `cantidad_rifas` INT(4) NOT NULL,
  `valor` INT(10) NULL,
  `fecha_sorteo` DATE NOT NULL,
  `id_organizador` INT(11) NOT NULL,
  PRIMARY KEY (`id_rifa`),
  INDEX `id_organizador_idx` (`id_organizador` ASC) VISIBLE,
  CONSTRAINT `id_organizador`
    FOREIGN KEY (`id_organizador`)
    REFERENCES `mirifa`.`usuario` (`id_usuario`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);
 
CREATE TABLE IF NOT EXISTS `mirifa`.`numeros_rifas` (
  `id_numero` INT(11) NOT NULL AUTO_INCREMENT,
  `id_rifa` INT(11) NOT NULL,
  PRIMARY KEY (`id_numero`),
  INDEX `id_rifa_idx` (`id_rifa` ASC) VISIBLE,
  CONSTRAINT `id_rifa`
    FOREIGN KEY (`id_rifa`)
    REFERENCES `mirifa`.`rifa` (`id_rifa`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);
  
CREATE TABLE IF NOT EXISTS `mirifa`.`venta` (
  `id_venta` INT(11) NOT NULL,
  `id_rifa_venta` INT(11) NOT NULL,
  `cantidad` INT(6) NOT NULL,
  `id_fact` BIGINT(20) NOT NULL,
  `descuento` FLOAT NULL,
  PRIMARY KEY (`id_venta`),
  INDEX `id_rifa_idx` (`id_rifa_venta` ASC) VISIBLE,
  INDEX `id_fact_idx` (`id_fact` ASC) VISIBLE,
  CONSTRAINT `id_rifa_venta`
    FOREIGN KEY (`id_rifa_venta`)
    REFERENCES `mirifa`.`rifa` (`id_rifa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `id_fact`
    FOREIGN KEY (`id_fact`)
    REFERENCES `mirifa`.`factura` (`id_factura`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);