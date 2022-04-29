CREATE DATABASE `jeu_nsi`;
CREATE TABLE `jeu_nsi`.`base` ( `ID` INT(4) NOT NULL AUTO_INCREMENT COMMENT 'max : 999999' , `pseudo` VARCHAR(15) NOT NULL COMMENT 'string classique' , `ELO` INT NOT NULL DEFAULT '0' COMMENT 'correspond au classement du joueur' , PRIMARY KEY (`ID`)) ENGINE = InnoDB COMMENT = 'table de base pour le jeu';
ALTER TABLE `base` AUTO_INCREMENT=100000;
CREATE TABLE `jeu_nsi`.`statistiques` ( `ID` INT(4) NOT NULL COMMENT 'max : 999999' , `nombre_morts` INT(4) NOT NULL DEFAULT'0' COMMENT 'compteur de morts' , `plus_haut_ELO` INT(4) NOT NULL DEFAULT '0' COMMENT 'plus haut elo jamais atteint du joueur' ,`temps_de_jeu` INT(4) NOT NULL DEFAULT '0' COMMENT 'temps de jeu en secondes', `serie_de_victoire_actuelle` INT(4) NOT NULL DEFAULT '0' COMMENT 'combien de victoires à la suite par rapport à la dernière partie', `plus_grande_serie_de_victoire` INT(4) NOT NULL DEFAULT '0' COMMENT 'nombre le plus grand de victoire à la suite', PRIMARY KEY (`ID`)) ENGINE = InnoDB COMMENT = 'table des statistiques';
CREATE TABLE `jeu_nsi`.`badges` ( `ID` INT(4) NOT NULL COMMENT 'max : 999999' , `crevard` BOOLEAN NOT NULL DEFAULT FALSE COMMENT 'débloqué si mort + de 100 fois' , `grand_vainqueur` BOOLEAN NOT NULL DEFAULT FALSE COMMENT 'avoir gagné toutes les courses d\'une partie' , `mauvais_joueur` BOOLEAN NOT NULL DEFAULT FALSE COMMENT 'donné à un joueur qui a un comportement innaproprié', PRIMARY KEY (`ID`)) ENGINE = InnoDB COMMENT = 'table des badges du joueur';