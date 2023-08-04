CREATE DATABASE IF NOT EXISTS prueba; 
USE prueba;

DROP TABLE IF EXISTS sesion CASCADE;
DROP TABLE IF EXISTS usuario CASCADE;



CREATE TABLE IF NOT EXISTS usuario (
	`Rut` INT PRIMARY KEY NOT NULL,
	`Contraseña`  VARCHAR(50),
	`Nombre` VARCHAR(30),
	`pApellido` VARCHAR(30),
	`sApellido` VARCHAR(30),
	`intentos_con` INT
);

CREATE TABLE IF NOT EXISTS sesion (
	`idSesion` INT PRIMARY KEY AUTO_INCREMENT,
	`Rut` INT NOT NULL, 
	`Hash_login` VARCHAR(35) NOT NULL , 
	`Hash1` VARCHAR(45),
	`UnHash1` INT,
	`Hash2` VARCHAR(45),
	`UnHash2` VARCHAR(3),
	`Hash3` VARCHAR(45),
	`UnHash3` INT,
	`Fecha` DATE
	
);


ALTER TABLE `sesion`
	ADD FOREIGN KEY (Rut)
	REFERENCES usuario(Rut)
	ON DELETE CASCADE;


