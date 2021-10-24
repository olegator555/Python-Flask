CREATE DATABASE `lab2` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
use lab2;
CREATE TABLE `order` (
  `id_order` int NOT NULL,
  `orderer` varchar(45) NOT NULL,
  `date` date NOT NULL,
  `price` decimal(20,0) NOT NULL,
  PRIMARY KEY (`id_order`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `realty` (
  `id_realty` int NOT NULL,
  `square` decimal(20,0) NOT NULL,
  `cost_per_mounth` int NOT NULL,
  PRIMARY KEY (`id_realty`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `realty_in_order` (
  `id` int NOT NULL,
  `id_order` int NOT NULL,
  `id_realty` int NOT NULL,
  `mounths` decimal(5,0) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `1_idx` (`id_order`),
  KEY `2_idx` (`id_realty`),
  CONSTRAINT `1` FOREIGN KEY (`id_order`) REFERENCES `order` (`id_order`),
  CONSTRAINT `2` FOREIGN KEY (`id_realty`) REFERENCES `realty` (`id_realty`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `user_root` (
  `id` int NOT NULL,
  `login` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `user_role` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO lab2.`order` (id_order, orderer, date, price) VALUES (101, 'Pavel', '2021-05-03', 199);
INSERT INTO lab2.`order` (id_order, orderer, date, price) VALUES (102, 'Oleg', '2021-10-16', 250);
INSERT INTO lab2.realty (id_realty, square, cost_per_mounth) VALUES (1001, 25, 18000);
INSERT INTO lab2.realty (id_realty, square, cost_per_mounth) VALUES (1002, 28, 14500);
INSERT INTO lab2.realty (id_realty, square, cost_per_mounth) VALUES (1003, 22, 13000);
INSERT INTO lab2.realty_in_order (id, id_order, id_realty, mounths) VALUES (11, 101, 1001, 5);
INSERT INTO lab2.user_root (id, login, password, user_role) VALUES (1, 'admin', 'admin', 'admin');
INSERT INTO lab2.user_root (id, login, password, user_role) VALUES (2, 'user', 'pass', 'user');
