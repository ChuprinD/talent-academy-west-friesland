-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: NHN
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `corop`
--

DROP TABLE IF EXISTS `corop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `corop` (
  `id` int NOT NULL AUTO_INCREMENT,
  `corop_naam` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `corop`
--

LOCK TABLES `corop` WRITE;
/*!40000 ALTER TABLE `corop` DISABLE KEYS */;
INSERT INTO `corop` VALUES (1,'Alkmaar en omgeving (C)'),(2,'Achterhoek (C)'),(3,'Agglomeratie \'s-Gravenhage (C)'),(4,'Agglomeratie Haarlem (C)'),(5,'Agglomeratie Leiden en Bollenstreek (C)'),(6,'Arnhem/Nijmegen (C)'),(7,'Delft en Westland (C)'),(8,'Delfzijl en omgeving (C)'),(9,'Flevoland (C)'),(10,'Groot-Amsterdam (C)'),(11,'Groot-Rijnmond (C)'),(12,'Het Gooi en Vechtstreek (C)'),(13,'IJmond (C)'),(14,'Kop van Noord-Holland (C)'),(15,'Midden-Limburg (C)'),(16,'Midden-Noord-Brabant (C)'),(17,'Noord-Drenthe (C)'),(18,'Noord-Friesland (C)'),(19,'Noord-Limburg (C)'),(20,'Noord-Overijssel (C)'),(21,'Noordoost-Noord-Brabant (C)'),(22,'Oost-Groningen (C)'),(23,'Oost-Zuid-Holland (C)'),(24,'Overig Groningen (C)'),(25,'Overig Zeeland (C)'),(26,'Twente (C)'),(27,'Utrecht (C)'),(28,'Veluwe (C)'),(29,'West-Noord-Brabant (C)'),(30,'Zaanstreek (C)'),(31,'Zeeuwsch-Vlaanderen (C)'),(32,'Zuid-Limburg (C)'),(33,'Zuidoost-Drenthe (C)'),(34,'Zuidoost-Friesland (C)'),(35,'Zuidoost-Noord-Brabant (C)'),(36,'Zuidoost-Zuid-Holland (C)'),(37,'Zuidwest-Drenthe (C)'),(38,'Zuidwest-Friesland (C)'),(39,'Zuidwest-Gelderland (C)'),(40,'Zuidwest-Overijssel (C)');
/*!40000 ALTER TABLE `corop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gemeente`
--

DROP TABLE IF EXISTS `gemeente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gemeente` (
  `id` int NOT NULL AUTO_INCREMENT,
  `gemeente_naam` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gemeente`
--

LOCK TABLES `gemeente` WRITE;
/*!40000 ALTER TABLE `gemeente` DISABLE KEYS */;
INSERT INTO `gemeente` VALUES (1,'Alkmaar'),(2,'Bergen (NH.)'),(3,'Castricum'),(4,'Den Helder'),(5,'Drechterland'),(6,'Enkhuizen'),(7,'Heiloo'),(8,'Hollands Kroon'),(9,'Hoorn'),(10,'Koggenland'),(11,'Medemblik'),(12,'Opmeer'),(13,'Schagen'),(14,'Stede Broec'),(15,'Texel'),(16,'Uitgeest');
/*!40000 ALTER TABLE `gemeente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jongeren`
--

DROP TABLE IF EXISTS `jongeren`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jongeren` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Jaar` int NOT NULL,
  `Niveau_regio` enum('Gemeente','Corop') NOT NULL,
  `Regio_id` int DEFAULT NULL,
  `werkende_jongeren` int NOT NULL,
  `totaal_jongeren` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jongeren`
--

LOCK TABLES `jongeren` WRITE;
/*!40000 ALTER TABLE `jongeren` DISABLE KEYS */;
INSERT INTO `jongeren` VALUES (1,2018,'Corop',1,10100,33100),(2,2018,'Corop',14,17000,51700),(3,2018,'Gemeente',1,4900,14700),(4,2018,'Gemeente',2,900,3600),(5,2018,'Gemeente',3,1400,4900),(6,2018,'Gemeente',4,2500,7300),(7,2018,'Gemeente',5,900,2700),(8,2018,'Gemeente',6,800,2400),(9,2018,'Gemeente',7,700,2900),(10,2018,'Gemeente',8,2200,6600),(11,2018,'Gemeente',9,3200,10200),(12,2018,'Gemeente',10,1100,3300),(13,2018,'Gemeente',11,2000,6200),(14,2018,'Gemeente',12,600,1800),(15,2018,'Gemeente',13,2000,6300),(16,2018,'Gemeente',14,1000,3000),(17,2018,'Gemeente',15,700,1700),(18,2018,'Gemeente',16,600,2000),(19,2019,'Corop',1,10400,33500),(20,2019,'Corop',14,17800,52200),(21,2019,'Gemeente',1,5000,14700),(22,2019,'Gemeente',2,900,3600),(23,2019,'Gemeente',3,1400,4900),(24,2019,'Gemeente',4,2600,7400),(25,2019,'Gemeente',5,900,2800),(26,2019,'Gemeente',6,800,2400),(27,2019,'Gemeente',7,700,3000),(28,2019,'Gemeente',8,2500,6900),(29,2019,'Gemeente',9,3300,10200),(30,2019,'Gemeente',10,1100,3400),(31,2019,'Gemeente',11,2100,6300),(32,2019,'Gemeente',12,600,1700),(33,2019,'Gemeente',13,2100,6300),(34,2019,'Gemeente',14,1100,3100),(35,2019,'Gemeente',15,700,1700),(36,2019,'Gemeente',16,700,2000),(37,2020,'Corop',1,10200,33600),(38,2020,'Corop',14,17500,52400),(39,2020,'Gemeente',1,4800,14800),(40,2020,'Gemeente',2,900,3500),(41,2020,'Gemeente',3,1300,4800),(42,2020,'Gemeente',4,2500,7200),(43,2020,'Gemeente',5,900,2800),(44,2020,'Gemeente',6,800,2400),(45,2020,'Gemeente',7,700,3100),(46,2020,'Gemeente',8,2600,7000),(47,2020,'Gemeente',9,3100,10300),(48,2020,'Gemeente',10,1200,3400),(49,2020,'Gemeente',11,2000,6200),(50,2020,'Gemeente',12,700,1800),(51,2020,'Gemeente',13,2100,6400),(52,2020,'Gemeente',14,1000,3100),(53,2020,'Gemeente',15,600,1700),(54,2020,'Gemeente',16,600,2000),(55,2021,'Corop',1,10600,33500),(56,2021,'Corop',14,18300,52300),(57,2021,'Gemeente',1,5000,14600),(58,2021,'Gemeente',2,1000,3500),(59,2021,'Gemeente',3,1400,4700),(60,2021,'Gemeente',4,2600,7300),(61,2021,'Gemeente',5,900,2700),(62,2021,'Gemeente',6,800,2400),(63,2021,'Gemeente',7,700,3100),(64,2021,'Gemeente',8,2700,6900),(65,2021,'Gemeente',9,3400,10400),(66,2021,'Gemeente',10,1200,3300),(67,2021,'Gemeente',11,2200,6300),(68,2021,'Gemeente',12,700,1800),(69,2021,'Gemeente',13,2200,6500),(70,2021,'Gemeente',14,1000,3100),(71,2021,'Gemeente',15,700,1700),(72,2021,'Gemeente',16,600,2000),(73,2022,'Corop',1,11300,33900),(74,2022,'Corop',14,19600,52900),(75,2022,'Gemeente',1,5300,14800),(76,2022,'Gemeente',2,1100,3600),(77,2022,'Gemeente',3,1500,4700),(78,2022,'Gemeente',4,2700,7200),(79,2022,'Gemeente',5,1000,2800),(80,2022,'Gemeente',6,900,2400),(81,2022,'Gemeente',7,800,3100),(82,2022,'Gemeente',8,2800,7000),(83,2022,'Gemeente',9,3700,10500),(84,2022,'Gemeente',10,1200,3400),(85,2022,'Gemeente',11,2400,6500),(86,2022,'Gemeente',12,700,1800),(87,2022,'Gemeente',13,2400,6600),(88,2022,'Gemeente',14,1100,3100),(89,2022,'Gemeente',15,700,1700),(90,2022,'Gemeente',16,600,2000);
/*!40000 ALTER TABLE `jongeren` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jongeren_woon_en_werkregio`
--

DROP TABLE IF EXISTS `jongeren_woon_en_werkregio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jongeren_woon_en_werkregio` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Jaar` int NOT NULL,
  `Niveau_regio` enum('Gemeente','Corop') NOT NULL,
  `Woonregio_id` int DEFAULT NULL,
  `Werkregio_id` int DEFAULT NULL,
  `Werkende_jongeren` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=401 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jongeren_woon_en_werkregio`
--

LOCK TABLES `jongeren_woon_en_werkregio` WRITE;
/*!40000 ALTER TABLE `jongeren_woon_en_werkregio` DISABLE KEYS */;
INSERT INTO `jongeren_woon_en_werkregio` VALUES (1,2018,'Corop',1,2,0),(2,2018,'Corop',1,3,100),(3,2018,'Corop',1,4,700),(4,2018,'Corop',1,5,0),(5,2018,'Corop',1,1,18000),(6,2018,'Corop',1,6,0),(7,2018,'Corop',1,7,0),(8,2018,'Corop',1,8,0),(9,2018,'Corop',1,9,0),(10,2018,'Corop',1,10,5000),(11,2018,'Corop',1,11,100),(12,2018,'Corop',1,12,100),(13,2018,'Corop',1,13,2000),(14,2018,'Corop',1,14,3400),(15,2018,'Corop',1,15,0),(16,2018,'Corop',1,16,100),(17,2018,'Corop',1,17,0),(18,2018,'Corop',1,18,0),(19,2018,'Corop',1,19,0),(20,2018,'Corop',1,20,0),(21,2018,'Corop',1,21,0),(22,2018,'Corop',1,22,0),(23,2018,'Corop',1,23,0),(24,2018,'Corop',1,24,0),(25,2018,'Corop',1,25,0),(26,2018,'Corop',1,26,0),(27,2018,'Corop',1,27,300),(28,2018,'Corop',1,28,0),(29,2018,'Corop',1,29,0),(30,2018,'Corop',1,30,900),(31,2018,'Corop',1,31,0),(32,2018,'Corop',1,32,0),(33,2018,'Corop',1,33,0),(34,2018,'Corop',1,34,0),(35,2018,'Corop',1,35,100),(36,2018,'Corop',1,36,0),(37,2018,'Corop',1,37,0),(38,2018,'Corop',1,38,0),(39,2018,'Corop',1,39,0),(40,2018,'Corop',1,40,0),(41,2018,'Corop',14,2,0),(42,2018,'Corop',14,3,200),(43,2018,'Corop',14,4,500),(44,2018,'Corop',14,5,0),(45,2018,'Corop',14,1,5800),(46,2018,'Corop',14,6,0),(47,2018,'Corop',14,7,400),(48,2018,'Corop',14,8,0),(49,2018,'Corop',14,9,200),(50,2018,'Corop',14,10,5900),(51,2018,'Corop',14,11,200),(52,2018,'Corop',14,12,400),(53,2018,'Corop',14,13,800),(54,2018,'Corop',14,14,34300),(55,2018,'Corop',14,15,0),(56,2018,'Corop',14,16,200),(57,2018,'Corop',14,17,0),(58,2018,'Corop',14,18,0),(59,2018,'Corop',14,19,0),(60,2018,'Corop',14,20,0),(61,2018,'Corop',14,21,0),(62,2018,'Corop',14,22,0),(63,2018,'Corop',14,23,0),(64,2018,'Corop',14,24,0),(65,2018,'Corop',14,25,0),(66,2018,'Corop',14,26,0),(67,2018,'Corop',14,27,300),(68,2018,'Corop',14,28,0),(69,2018,'Corop',14,29,0),(70,2018,'Corop',14,30,700),(71,2018,'Corop',14,31,0),(72,2018,'Corop',14,32,0),(73,2018,'Corop',14,33,0),(74,2018,'Corop',14,34,0),(75,2018,'Corop',14,35,100),(76,2018,'Corop',14,36,0),(77,2018,'Corop',14,37,0),(78,2018,'Corop',14,38,0),(79,2018,'Corop',14,39,0),(80,2018,'Corop',14,40,0),(81,2019,'Corop',1,2,0),(82,2019,'Corop',1,3,0),(83,2019,'Corop',1,4,1000),(84,2019,'Corop',1,5,0),(85,2019,'Corop',1,1,18100),(86,2019,'Corop',1,6,0),(87,2019,'Corop',1,7,0),(88,2019,'Corop',1,8,0),(89,2019,'Corop',1,9,0),(90,2019,'Corop',1,10,5800),(91,2019,'Corop',1,11,0),(92,2019,'Corop',1,12,100),(93,2019,'Corop',1,13,1700),(94,2019,'Corop',1,14,3000),(95,2019,'Corop',1,15,0),(96,2019,'Corop',1,16,200),(97,2019,'Corop',1,17,0),(98,2019,'Corop',1,18,0),(99,2019,'Corop',1,19,0),(100,2019,'Corop',1,20,0),(101,2019,'Corop',1,21,0),(102,2019,'Corop',1,22,0),(103,2019,'Corop',1,23,0),(104,2019,'Corop',1,24,0),(105,2019,'Corop',1,25,0),(106,2019,'Corop',1,26,0),(107,2019,'Corop',1,27,400),(108,2019,'Corop',1,28,0),(109,2019,'Corop',1,29,0),(110,2019,'Corop',1,30,800),(111,2019,'Corop',1,31,0),(112,2019,'Corop',1,32,0),(113,2019,'Corop',1,33,0),(114,2019,'Corop',1,34,0),(115,2019,'Corop',1,35,200),(116,2019,'Corop',1,36,0),(117,2019,'Corop',1,37,0),(118,2019,'Corop',1,38,0),(119,2019,'Corop',1,39,0),(120,2019,'Corop',1,40,0),(121,2019,'Corop',14,2,0),(122,2019,'Corop',14,3,200),(123,2019,'Corop',14,4,500),(124,2019,'Corop',14,5,0),(125,2019,'Corop',14,1,5100),(126,2019,'Corop',14,6,0),(127,2019,'Corop',14,7,500),(128,2019,'Corop',14,8,0),(129,2019,'Corop',14,9,200),(130,2019,'Corop',14,10,6400),(131,2019,'Corop',14,11,200),(132,2019,'Corop',14,12,300),(133,2019,'Corop',14,13,800),(134,2019,'Corop',14,14,34800),(135,2019,'Corop',14,15,0),(136,2019,'Corop',14,16,200),(137,2019,'Corop',14,17,0),(138,2019,'Corop',14,18,0),(139,2019,'Corop',14,19,0),(140,2019,'Corop',14,20,0),(141,2019,'Corop',14,21,0),(142,2019,'Corop',14,22,0),(143,2019,'Corop',14,23,0),(144,2019,'Corop',14,24,0),(145,2019,'Corop',14,25,0),(146,2019,'Corop',14,26,0),(147,2019,'Corop',14,27,500),(148,2019,'Corop',14,28,100),(149,2019,'Corop',14,29,0),(150,2019,'Corop',14,30,800),(151,2019,'Corop',14,31,0),(152,2019,'Corop',14,32,0),(153,2019,'Corop',14,33,0),(154,2019,'Corop',14,34,0),(155,2019,'Corop',14,35,100),(156,2019,'Corop',14,36,0),(157,2019,'Corop',14,37,0),(158,2019,'Corop',14,38,0),(159,2019,'Corop',14,39,0),(160,2019,'Corop',14,40,0),(161,2020,'Corop',1,2,0),(162,2020,'Corop',1,3,0),(163,2020,'Corop',1,4,1600),(164,2020,'Corop',1,5,100),(165,2020,'Corop',1,1,17200),(166,2020,'Corop',1,6,0),(167,2020,'Corop',1,7,0),(168,2020,'Corop',1,8,0),(169,2020,'Corop',1,9,0),(170,2020,'Corop',1,10,5100),(171,2020,'Corop',1,11,100),(172,2020,'Corop',1,12,200),(173,2020,'Corop',1,13,2000),(174,2020,'Corop',1,14,2800),(175,2020,'Corop',1,15,0),(176,2020,'Corop',1,16,0),(177,2020,'Corop',1,17,0),(178,2020,'Corop',1,18,0),(179,2020,'Corop',1,19,0),(180,2020,'Corop',1,20,0),(181,2020,'Corop',1,21,0),(182,2020,'Corop',1,22,0),(183,2020,'Corop',1,23,0),(184,2020,'Corop',1,24,0),(185,2020,'Corop',1,25,0),(186,2020,'Corop',1,26,0),(187,2020,'Corop',1,27,300),(188,2020,'Corop',1,28,0),(189,2020,'Corop',1,29,0),(190,2020,'Corop',1,30,1200),(191,2020,'Corop',1,31,0),(192,2020,'Corop',1,32,0),(193,2020,'Corop',1,33,0),(194,2020,'Corop',1,34,0),(195,2020,'Corop',1,35,0),(196,2020,'Corop',1,36,0),(197,2020,'Corop',1,37,0),(198,2020,'Corop',1,38,0),(199,2020,'Corop',1,39,0),(200,2020,'Corop',1,40,0),(201,2020,'Corop',14,2,0),(202,2020,'Corop',14,3,200),(203,2020,'Corop',14,4,400),(204,2020,'Corop',14,5,0),(205,2020,'Corop',14,1,5600),(206,2020,'Corop',14,6,100),(207,2020,'Corop',14,7,500),(208,2020,'Corop',14,8,0),(209,2020,'Corop',14,9,200),(210,2020,'Corop',14,10,5200),(211,2020,'Corop',14,11,200),(212,2020,'Corop',14,12,300),(213,2020,'Corop',14,13,700),(214,2020,'Corop',14,14,33500),(215,2020,'Corop',14,15,0),(216,2020,'Corop',14,16,0),(217,2020,'Corop',14,17,0),(218,2020,'Corop',14,18,0),(219,2020,'Corop',14,19,0),(220,2020,'Corop',14,20,0),(221,2020,'Corop',14,21,0),(222,2020,'Corop',14,22,0),(223,2020,'Corop',14,23,100),(224,2020,'Corop',14,24,0),(225,2020,'Corop',14,25,0),(226,2020,'Corop',14,26,0),(227,2020,'Corop',14,27,400),(228,2020,'Corop',14,28,200),(229,2020,'Corop',14,29,0),(230,2020,'Corop',14,30,1500),(231,2020,'Corop',14,31,0),(232,2020,'Corop',14,32,0),(233,2020,'Corop',14,33,0),(234,2020,'Corop',14,34,0),(235,2020,'Corop',14,35,0),(236,2020,'Corop',14,36,0),(237,2020,'Corop',14,37,0),(238,2020,'Corop',14,38,0),(239,2020,'Corop',14,39,0),(240,2020,'Corop',14,40,0),(241,2021,'Corop',14,22,0),(242,2022,'Corop',14,22,0),(243,2021,'Corop',14,8,0),(244,2022,'Corop',14,8,0),(245,2021,'Corop',14,24,100),(246,2022,'Corop',14,24,100),(247,2021,'Corop',14,18,100),(248,2022,'Corop',14,18,100),(249,2021,'Corop',14,38,0),(250,2022,'Corop',14,38,100),(251,2021,'Corop',14,34,0),(252,2022,'Corop',14,34,0),(253,2021,'Corop',14,17,0),(254,2022,'Corop',14,17,0),(255,2021,'Corop',14,33,0),(256,2022,'Corop',14,33,0),(257,2021,'Corop',14,37,0),(258,2022,'Corop',14,37,0),(259,2021,'Corop',14,20,100),(260,2022,'Corop',14,20,100),(261,2021,'Corop',14,40,0),(262,2022,'Corop',14,40,0),(263,2021,'Corop',14,26,100),(264,2022,'Corop',14,26,100),(265,2021,'Corop',14,28,100),(266,2022,'Corop',14,28,100),(267,2021,'Corop',14,2,0),(268,2022,'Corop',14,2,0),(269,2021,'Corop',14,6,100),(270,2022,'Corop',14,6,100),(271,2021,'Corop',14,39,0),(272,2022,'Corop',14,39,0),(273,2021,'Corop',14,27,500),(274,2022,'Corop',14,27,700),(275,2021,'Corop',14,14,36700),(276,2022,'Corop',14,14,37400),(277,2021,'Corop',14,1,4900),(278,2022,'Corop',14,1,5000),(279,2021,'Corop',14,13,600),(280,2022,'Corop',14,13,800),(281,2021,'Corop',14,4,300),(282,2022,'Corop',14,4,300),(283,2021,'Corop',14,30,600),(284,2022,'Corop',14,30,500),(285,2021,'Corop',14,10,5400),(286,2022,'Corop',14,10,5900),(287,2021,'Corop',14,12,200),(288,2022,'Corop',14,12,200),(289,2021,'Corop',14,5,100),(290,2022,'Corop',14,5,100),(291,2021,'Corop',14,3,200),(292,2022,'Corop',14,3,300),(293,2021,'Corop',14,7,300),(294,2022,'Corop',14,7,400),(295,2021,'Corop',14,23,100),(296,2022,'Corop',14,23,100),(297,2021,'Corop',14,11,300),(298,2022,'Corop',14,11,300),(299,2021,'Corop',14,36,100),(300,2022,'Corop',14,36,100),(301,2021,'Corop',14,31,0),(302,2022,'Corop',14,31,0),(303,2021,'Corop',14,25,0),(304,2022,'Corop',14,25,0),(305,2021,'Corop',14,29,100),(306,2022,'Corop',14,29,100),(307,2021,'Corop',14,16,100),(308,2022,'Corop',14,16,100),(309,2021,'Corop',14,21,100),(310,2022,'Corop',14,21,100),(311,2021,'Corop',14,35,100),(312,2022,'Corop',14,35,100),(313,2021,'Corop',14,19,0),(314,2022,'Corop',14,19,0),(315,2021,'Corop',14,15,0),(316,2022,'Corop',14,15,0),(317,2021,'Corop',14,32,0),(318,2022,'Corop',14,32,0),(319,2021,'Corop',14,9,300),(320,2022,'Corop',14,9,400),(321,2021,'Corop',1,22,0),(322,2022,'Corop',1,22,0),(323,2021,'Corop',1,8,0),(324,2022,'Corop',1,8,0),(325,2021,'Corop',1,24,0),(326,2022,'Corop',1,24,0),(327,2021,'Corop',1,18,0),(328,2022,'Corop',1,18,0),(329,2021,'Corop',1,38,0),(330,2022,'Corop',1,38,0),(331,2021,'Corop',1,34,0),(332,2022,'Corop',1,34,0),(333,2021,'Corop',1,17,0),(334,2022,'Corop',1,17,0),(335,2021,'Corop',1,33,0),(336,2022,'Corop',1,33,0),(337,2021,'Corop',1,37,0),(338,2022,'Corop',1,37,0),(339,2021,'Corop',1,20,0),(340,2022,'Corop',1,20,0),(341,2021,'Corop',1,40,0),(342,2022,'Corop',1,40,0),(343,2021,'Corop',1,26,0),(344,2022,'Corop',1,26,0),(345,2021,'Corop',1,28,100),(346,2022,'Corop',1,28,0),(347,2021,'Corop',1,2,0),(348,2022,'Corop',1,2,0),(349,2021,'Corop',1,6,100),(350,2022,'Corop',1,6,100),(351,2021,'Corop',1,39,0),(352,2022,'Corop',1,39,0),(353,2021,'Corop',1,27,400),(354,2022,'Corop',1,27,400),(355,2021,'Corop',1,14,2600),(356,2022,'Corop',1,14,2500),(357,2021,'Corop',1,1,20800),(358,2022,'Corop',1,1,21700),(359,2021,'Corop',1,13,1700),(360,2022,'Corop',1,13,1900),(361,2021,'Corop',1,4,500),(362,2022,'Corop',1,4,400),(363,2021,'Corop',1,30,800),(364,2022,'Corop',1,30,700),(365,2021,'Corop',1,10,4400),(366,2022,'Corop',1,10,4600),(367,2021,'Corop',1,12,100),(368,2022,'Corop',1,12,100),(369,2021,'Corop',1,5,100),(370,2022,'Corop',1,5,100),(371,2021,'Corop',1,3,100),(372,2022,'Corop',1,3,200),(373,2021,'Corop',1,7,0),(374,2022,'Corop',1,7,0),(375,2021,'Corop',1,23,0),(376,2022,'Corop',1,23,0),(377,2021,'Corop',1,11,100),(378,2022,'Corop',1,11,200),(379,2021,'Corop',1,36,0),(380,2022,'Corop',1,36,0),(381,2021,'Corop',1,31,0),(382,2022,'Corop',1,31,0),(383,2021,'Corop',1,25,0),(384,2022,'Corop',1,25,0),(385,2021,'Corop',1,29,100),(386,2022,'Corop',1,29,0),(387,2021,'Corop',1,16,200),(388,2022,'Corop',1,16,100),(389,2021,'Corop',1,21,100),(390,2022,'Corop',1,21,100),(391,2021,'Corop',1,35,100),(392,2022,'Corop',1,35,200),(393,2021,'Corop',1,19,0),(394,2022,'Corop',1,19,0),(395,2021,'Corop',1,15,0),(396,2022,'Corop',1,15,0),(397,2021,'Corop',1,32,0),(398,2022,'Corop',1,32,0),(399,2021,'Corop',1,9,100),(400,2022,'Corop',1,9,100);
/*!40000 ALTER TABLE `jongeren_woon_en_werkregio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `volwassene_woon_en_werkregio`
--

DROP TABLE IF EXISTS `volwassene_woon_en_werkregio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `volwassene_woon_en_werkregio` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Jaar` int NOT NULL,
  `Niveau_regio` enum('Gemeente','Corop') NOT NULL,
  `Woonregio_id` int DEFAULT NULL,
  `Werkregio_id` int DEFAULT NULL,
  `Werkende_volwassene` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=401 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `volwassene_woon_en_werkregio`
--

LOCK TABLES `volwassene_woon_en_werkregio` WRITE;
/*!40000 ALTER TABLE `volwassene_woon_en_werkregio` DISABLE KEYS */;
INSERT INTO `volwassene_woon_en_werkregio` VALUES (1,2018,'Corop',1,2,0),(2,2018,'Corop',1,3,600),(3,2018,'Corop',1,4,2300),(4,2018,'Corop',1,5,300),(5,2018,'Corop',1,1,41600),(6,2018,'Corop',1,6,0),(7,2018,'Corop',1,7,0),(8,2018,'Corop',1,8,0),(9,2018,'Corop',1,9,0),(10,2018,'Corop',1,10,16100),(11,2018,'Corop',1,11,700),(12,2018,'Corop',1,12,200),(13,2018,'Corop',1,13,6500),(14,2018,'Corop',1,14,7900),(15,2018,'Corop',1,15,0),(16,2018,'Corop',1,16,0),(17,2018,'Corop',1,17,0),(18,2018,'Corop',1,18,0),(19,2018,'Corop',1,19,0),(20,2018,'Corop',1,20,0),(21,2018,'Corop',1,21,0),(22,2018,'Corop',1,22,0),(23,2018,'Corop',1,23,0),(24,2018,'Corop',1,24,0),(25,2018,'Corop',1,25,0),(26,2018,'Corop',1,26,0),(27,2018,'Corop',1,27,1300),(28,2018,'Corop',1,28,0),(29,2018,'Corop',1,29,0),(30,2018,'Corop',1,30,3600),(31,2018,'Corop',1,31,0),(32,2018,'Corop',1,32,0),(33,2018,'Corop',1,33,0),(34,2018,'Corop',1,34,0),(35,2018,'Corop',1,35,0),(36,2018,'Corop',1,36,0),(37,2018,'Corop',1,37,0),(38,2018,'Corop',1,38,0),(39,2018,'Corop',1,39,0),(40,2018,'Corop',1,40,0),(41,2018,'Corop',14,2,0),(42,2018,'Corop',14,3,600),(43,2018,'Corop',14,4,1300),(44,2018,'Corop',14,5,200),(45,2018,'Corop',14,1,15800),(46,2018,'Corop',14,6,0),(47,2018,'Corop',14,7,200),(48,2018,'Corop',14,8,0),(49,2018,'Corop',14,9,700),(50,2018,'Corop',14,10,17100),(51,2018,'Corop',14,11,700),(52,2018,'Corop',14,12,700),(53,2018,'Corop',14,13,3300),(54,2018,'Corop',14,14,77700),(55,2018,'Corop',14,15,0),(56,2018,'Corop',14,16,0),(57,2018,'Corop',14,17,0),(58,2018,'Corop',14,18,0),(59,2018,'Corop',14,19,0),(60,2018,'Corop',14,20,0),(61,2018,'Corop',14,21,0),(62,2018,'Corop',14,22,0),(63,2018,'Corop',14,23,0),(64,2018,'Corop',14,24,0),(65,2018,'Corop',14,25,0),(66,2018,'Corop',14,26,0),(67,2018,'Corop',14,27,1400),(68,2018,'Corop',14,28,500),(69,2018,'Corop',14,29,200),(70,2018,'Corop',14,30,2500),(71,2018,'Corop',14,31,0),(72,2018,'Corop',14,32,0),(73,2018,'Corop',14,33,0),(74,2018,'Corop',14,34,0),(75,2018,'Corop',14,35,0),(76,2018,'Corop',14,36,0),(77,2018,'Corop',14,37,0),(78,2018,'Corop',14,38,0),(79,2018,'Corop',14,39,0),(80,2018,'Corop',14,40,0),(81,2019,'Corop',1,2,0),(82,2019,'Corop',1,3,600),(83,2019,'Corop',1,4,3000),(84,2019,'Corop',1,5,100),(85,2019,'Corop',1,1,41600),(86,2019,'Corop',1,6,0),(87,2019,'Corop',1,7,0),(88,2019,'Corop',1,8,0),(89,2019,'Corop',1,9,0),(90,2019,'Corop',1,10,17500),(91,2019,'Corop',1,11,600),(92,2019,'Corop',1,12,300),(93,2019,'Corop',1,13,6600),(94,2019,'Corop',1,14,7700),(95,2019,'Corop',1,15,0),(96,2019,'Corop',1,16,0),(97,2019,'Corop',1,17,0),(98,2019,'Corop',1,18,0),(99,2019,'Corop',1,19,0),(100,2019,'Corop',1,20,0),(101,2019,'Corop',1,21,0),(102,2019,'Corop',1,22,0),(103,2019,'Corop',1,23,0),(104,2019,'Corop',1,24,0),(105,2019,'Corop',1,25,0),(106,2019,'Corop',1,26,0),(107,2019,'Corop',1,27,1400),(108,2019,'Corop',1,28,0),(109,2019,'Corop',1,29,0),(110,2019,'Corop',1,30,3000),(111,2019,'Corop',1,31,0),(112,2019,'Corop',1,32,0),(113,2019,'Corop',1,33,0),(114,2019,'Corop',1,34,0),(115,2019,'Corop',1,35,0),(116,2019,'Corop',1,36,0),(117,2019,'Corop',1,37,0),(118,2019,'Corop',1,38,0),(119,2019,'Corop',1,39,0),(120,2019,'Corop',1,40,0),(121,2019,'Corop',14,2,0),(122,2019,'Corop',14,3,700),(123,2019,'Corop',14,4,1400),(124,2019,'Corop',14,5,200),(125,2019,'Corop',14,1,14800),(126,2019,'Corop',14,6,700),(127,2019,'Corop',14,7,300),(128,2019,'Corop',14,8,0),(129,2019,'Corop',14,9,700),(130,2019,'Corop',14,10,17900),(131,2019,'Corop',14,11,600),(132,2019,'Corop',14,12,700),(133,2019,'Corop',14,13,2900),(134,2019,'Corop',14,14,78700),(135,2019,'Corop',14,15,0),(136,2019,'Corop',14,16,0),(137,2019,'Corop',14,17,0),(138,2019,'Corop',14,18,0),(139,2019,'Corop',14,19,0),(140,2019,'Corop',14,20,0),(141,2019,'Corop',14,21,0),(142,2019,'Corop',14,22,0),(143,2019,'Corop',14,23,0),(144,2019,'Corop',14,24,0),(145,2019,'Corop',14,25,0),(146,2019,'Corop',14,26,0),(147,2019,'Corop',14,27,1900),(148,2019,'Corop',14,28,400),(149,2019,'Corop',14,29,0),(150,2019,'Corop',14,30,2900),(151,2019,'Corop',14,31,0),(152,2019,'Corop',14,32,0),(153,2019,'Corop',14,33,0),(154,2019,'Corop',14,34,0),(155,2019,'Corop',14,35,0),(156,2019,'Corop',14,36,0),(157,2019,'Corop',14,37,0),(158,2019,'Corop',14,38,0),(159,2019,'Corop',14,39,0),(160,2019,'Corop',14,40,0),(161,2020,'Corop',1,2,0),(162,2020,'Corop',1,3,500),(163,2020,'Corop',1,4,2700),(164,2020,'Corop',1,5,100),(165,2020,'Corop',1,1,41200),(166,2020,'Corop',1,6,0),(167,2020,'Corop',1,7,0),(168,2020,'Corop',1,8,0),(169,2020,'Corop',1,9,0),(170,2020,'Corop',1,10,17900),(171,2020,'Corop',1,11,500),(172,2020,'Corop',1,12,600),(173,2020,'Corop',1,13,6500),(174,2020,'Corop',1,14,7600),(175,2020,'Corop',1,15,0),(176,2020,'Corop',1,16,0),(177,2020,'Corop',1,17,0),(178,2020,'Corop',1,18,0),(179,2020,'Corop',1,19,0),(180,2020,'Corop',1,20,0),(181,2020,'Corop',1,21,0),(182,2020,'Corop',1,22,0),(183,2020,'Corop',1,23,0),(184,2020,'Corop',1,24,0),(185,2020,'Corop',1,25,0),(186,2020,'Corop',1,26,0),(187,2020,'Corop',1,27,1300),(188,2020,'Corop',1,28,0),(189,2020,'Corop',1,29,0),(190,2020,'Corop',1,30,3100),(191,2020,'Corop',1,31,0),(192,2020,'Corop',1,32,0),(193,2020,'Corop',1,33,0),(194,2020,'Corop',1,34,0),(195,2020,'Corop',1,35,0),(196,2020,'Corop',1,36,0),(197,2020,'Corop',1,37,0),(198,2020,'Corop',1,38,0),(199,2020,'Corop',1,39,0),(200,2020,'Corop',1,40,0),(201,2020,'Corop',14,2,0),(202,2020,'Corop',14,3,600),(203,2020,'Corop',14,4,1400),(204,2020,'Corop',14,5,300),(205,2020,'Corop',14,1,16100),(206,2020,'Corop',14,6,0),(207,2020,'Corop',14,7,500),(208,2020,'Corop',14,8,0),(209,2020,'Corop',14,9,700),(210,2020,'Corop',14,10,16900),(211,2020,'Corop',14,11,600),(212,2020,'Corop',14,12,700),(213,2020,'Corop',14,13,2800),(214,2020,'Corop',14,14,77800),(215,2020,'Corop',14,15,0),(216,2020,'Corop',14,16,0),(217,2020,'Corop',14,17,0),(218,2020,'Corop',14,18,0),(219,2020,'Corop',14,19,0),(220,2020,'Corop',14,20,0),(221,2020,'Corop',14,21,0),(222,2020,'Corop',14,22,0),(223,2020,'Corop',14,23,0),(224,2020,'Corop',14,24,0),(225,2020,'Corop',14,25,0),(226,2020,'Corop',14,26,0),(227,2020,'Corop',14,27,1700),(228,2020,'Corop',14,28,700),(229,2020,'Corop',14,29,0),(230,2020,'Corop',14,30,3000),(231,2020,'Corop',14,31,0),(232,2020,'Corop',14,32,0),(233,2020,'Corop',14,33,0),(234,2020,'Corop',14,34,0),(235,2020,'Corop',14,35,0),(236,2020,'Corop',14,36,100),(237,2020,'Corop',14,37,0),(238,2020,'Corop',14,38,0),(239,2020,'Corop',14,39,0),(240,2020,'Corop',14,40,0),(241,2021,'Corop',1,2,0),(242,2021,'Corop',1,3,600),(243,2021,'Corop',1,4,1700),(244,2021,'Corop',1,5,300),(245,2021,'Corop',1,1,45200),(246,2021,'Corop',1,6,200),(247,2021,'Corop',1,7,100),(248,2021,'Corop',1,8,0),(249,2021,'Corop',1,9,200),(250,2021,'Corop',1,10,15800),(251,2021,'Corop',1,11,600),(252,2021,'Corop',1,12,200),(253,2021,'Corop',1,13,6800),(254,2021,'Corop',1,14,8100),(255,2021,'Corop',1,15,0),(256,2021,'Corop',1,16,200),(257,2021,'Corop',1,17,0),(258,2021,'Corop',1,18,0),(259,2021,'Corop',1,19,0),(260,2021,'Corop',1,20,100),(261,2021,'Corop',1,21,100),(262,2021,'Corop',1,22,0),(263,2021,'Corop',1,23,100),(264,2021,'Corop',1,24,0),(265,2021,'Corop',1,25,0),(266,2021,'Corop',1,26,200),(267,2021,'Corop',1,27,1200),(268,2021,'Corop',1,28,200),(269,2021,'Corop',1,29,100),(270,2021,'Corop',1,30,3000),(271,2021,'Corop',1,31,0),(272,2021,'Corop',1,32,0),(273,2021,'Corop',1,33,0),(274,2021,'Corop',1,34,0),(275,2021,'Corop',1,35,100),(276,2021,'Corop',1,36,100),(277,2021,'Corop',1,37,0),(278,2021,'Corop',1,38,0),(279,2021,'Corop',1,39,0),(280,2021,'Corop',1,40,0),(281,2021,'Corop',14,2,0),(282,2021,'Corop',14,3,600),(283,2021,'Corop',14,4,900),(284,2021,'Corop',14,5,400),(285,2021,'Corop',14,1,14500),(286,2021,'Corop',14,6,200),(287,2021,'Corop',14,7,400),(288,2021,'Corop',14,8,0),(289,2021,'Corop',14,9,1000),(290,2021,'Corop',14,10,17300),(291,2021,'Corop',14,11,700),(292,2021,'Corop',14,12,400),(293,2021,'Corop',14,13,2600),(294,2021,'Corop',14,14,82000),(295,2021,'Corop',14,15,0),(296,2021,'Corop',14,16,200),(297,2021,'Corop',14,17,0),(298,2021,'Corop',14,18,200),(299,2021,'Corop',14,19,0),(300,2021,'Corop',14,20,200),(301,2021,'Corop',14,21,200),(302,2021,'Corop',14,22,0),(303,2021,'Corop',14,23,200),(304,2021,'Corop',14,24,200),(305,2021,'Corop',14,25,0),(306,2021,'Corop',14,26,200),(307,2021,'Corop',14,27,1600),(308,2021,'Corop',14,28,400),(309,2021,'Corop',14,29,200),(310,2021,'Corop',14,30,2200),(311,2021,'Corop',14,31,0),(312,2021,'Corop',14,32,0),(313,2021,'Corop',14,33,0),(314,2021,'Corop',14,34,0),(315,2021,'Corop',14,35,200),(316,2021,'Corop',14,36,200),(317,2021,'Corop',14,37,0),(318,2021,'Corop',14,38,100),(319,2021,'Corop',14,39,100),(320,2021,'Corop',14,40,0),(321,2022,'Corop',1,2,0),(322,2022,'Corop',1,3,700),(323,2022,'Corop',1,4,1600),(324,2022,'Corop',1,5,400),(325,2022,'Corop',1,1,46200),(326,2022,'Corop',1,6,200),(327,2022,'Corop',1,7,200),(328,2022,'Corop',1,8,0),(329,2022,'Corop',1,9,200),(330,2022,'Corop',1,10,16000),(331,2022,'Corop',1,11,600),(332,2022,'Corop',1,12,400),(333,2022,'Corop',1,13,6900),(334,2022,'Corop',1,14,7900),(335,2022,'Corop',1,15,0),(336,2022,'Corop',1,16,0),(337,2022,'Corop',1,17,0),(338,2022,'Corop',1,18,0),(339,2022,'Corop',1,19,0),(340,2022,'Corop',1,20,100),(341,2022,'Corop',1,21,200),(342,2022,'Corop',1,22,0),(343,2022,'Corop',1,23,100),(344,2022,'Corop',1,24,0),(345,2022,'Corop',1,25,0),(346,2022,'Corop',1,26,200),(347,2022,'Corop',1,27,1400),(348,2022,'Corop',1,28,200),(349,2022,'Corop',1,29,100),(350,2022,'Corop',1,30,3400),(351,2022,'Corop',1,31,0),(352,2022,'Corop',1,32,0),(353,2022,'Corop',1,33,0),(354,2022,'Corop',1,34,0),(355,2022,'Corop',1,35,200),(356,2022,'Corop',1,36,100),(357,2022,'Corop',1,37,0),(358,2022,'Corop',1,38,0),(359,2022,'Corop',1,39,0),(360,2022,'Corop',1,40,0),(361,2022,'Corop',14,2,0),(362,2022,'Corop',14,3,800),(363,2022,'Corop',14,4,900),(364,2022,'Corop',14,5,400),(365,2022,'Corop',14,1,14500),(366,2022,'Corop',14,6,200),(367,2022,'Corop',14,7,600),(368,2022,'Corop',14,8,0),(369,2022,'Corop',14,9,1200),(370,2022,'Corop',14,10,18000),(371,2022,'Corop',14,11,900),(372,2022,'Corop',14,12,500),(373,2022,'Corop',14,13,2600),(374,2022,'Corop',14,14,82600),(375,2022,'Corop',14,15,0),(376,2022,'Corop',14,16,0),(377,2022,'Corop',14,17,0),(378,2022,'Corop',14,18,200),(379,2022,'Corop',14,19,0),(380,2022,'Corop',14,20,200),(381,2022,'Corop',14,21,200),(382,2022,'Corop',14,22,0),(383,2022,'Corop',14,23,200),(384,2022,'Corop',14,24,0),(385,2022,'Corop',14,25,0),(386,2022,'Corop',14,26,200),(387,2022,'Corop',14,27,1800),(388,2022,'Corop',14,28,500),(389,2022,'Corop',14,29,200),(390,2022,'Corop',14,30,2400),(391,2022,'Corop',14,31,0),(392,2022,'Corop',14,32,0),(393,2022,'Corop',14,33,0),(394,2022,'Corop',14,34,0),(395,2022,'Corop',14,35,200),(396,2022,'Corop',14,36,200),(397,2022,'Corop',14,37,0),(398,2022,'Corop',14,38,100),(399,2022,'Corop',14,39,100),(400,2022,'Corop',14,40,0);
/*!40000 ALTER TABLE `volwassene_woon_en_werkregio` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-31 10:55:57
