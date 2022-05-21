-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: puc_projeto
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `disponibilidade`
--

DROP TABLE IF EXISTS `disponibilidade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `disponibilidade` (
  `dat_referencia` date NOT NULL,
  `val_dispf` decimal(8,2) DEFAULT NULL,
  `val_indisppf` decimal(8,2) DEFAULT NULL,
  `val_indispff` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`dat_referencia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disponibilidade`
--

LOCK TABLES `disponibilidade` WRITE;
/*!40000 ALTER TABLE `disponibilidade` DISABLE KEYS */;
INSERT INTO `disponibilidade` VALUES ('2011-01-01',91.71,7.02,1.26),('2011-02-01',89.94,8.23,1.83),('2011-03-01',89.33,8.40,2.26),('2011-04-01',89.98,8.37,1.65),('2011-05-01',89.31,8.66,2.03),('2011-06-01',89.39,8.59,2.02),('2011-07-01',88.41,9.29,2.31),('2011-08-01',87.14,10.37,2.49),('2011-09-01',86.91,10.61,2.49),('2011-10-01',88.37,9.44,2.18),('2011-11-01',89.28,8.31,2.41),('2011-12-01',89.48,8.19,2.33),('2012-01-01',89.72,8.42,1.86),('2012-02-01',88.32,9.10,2.58),('2012-03-01',87.21,9.88,2.91),('2012-04-01',87.64,9.67,2.69),('2012-05-01',88.24,9.69,2.07),('2012-06-01',88.71,9.17,2.12),('2012-07-01',88.00,9.50,2.50),('2012-08-01',87.70,10.15,2.14),('2012-09-01',88.32,10.01,1.67),('2012-10-01',87.97,10.44,1.59),('2012-11-01',88.04,10.56,1.40),('2012-12-01',89.47,8.66,1.86),('2013-01-01',90.47,7.31,2.22),('2013-02-01',90.53,7.15,2.33),('2013-03-01',89.27,8.10,2.63),('2013-04-01',87.80,9.70,2.49),('2013-05-01',88.95,8.63,2.42),('2013-06-01',90.13,7.74,2.12),('2013-07-01',89.01,8.25,2.74),('2013-08-01',88.53,9.12,2.35),('2013-09-01',88.31,9.12,2.57),('2013-10-01',89.06,8.51,2.43),('2013-11-01',88.10,9.38,2.53),('2013-12-01',89.88,7.49,2.63),('2014-01-01',89.95,7.06,2.99),('2014-02-01',90.33,6.58,3.09),('2014-03-01',90.16,7.10,2.73),('2014-04-01',89.06,8.17,2.78),('2014-05-01',86.81,10.12,3.07),('2014-06-01',89.97,7.36,2.68),('2014-07-01',89.49,7.62,2.89),('2014-08-01',86.32,10.81,2.88),('2014-09-01',84.90,11.13,3.73),('2014-10-01',87.29,9.22,3.19),('2014-11-01',87.78,8.77,3.25),('2014-12-01',89.34,7.72,2.95),('2015-01-01',88.57,7.40,4.03),('2015-02-01',89.21,7.67,3.12),('2015-03-01',87.78,9.12,3.10),('2015-04-01',88.24,8.03,3.73),('2015-05-01',86.47,9.62,3.91),('2015-06-01',86.35,9.97,3.68),('2015-07-01',86.63,10.11,3.26),('2015-08-01',85.86,10.57,3.57),('2015-09-01',83.62,11.72,4.66),('2015-10-01',84.09,11.49,4.43),('2015-11-01',84.73,10.56,4.71),('2015-12-01',86.51,8.81,4.68),('2016-01-01',86.80,8.18,5.02),('2016-02-01',85.62,9.33,5.05),('2016-03-01',84.31,10.24,5.45),('2016-04-01',84.42,10.36,5.22),('2016-05-01',84.43,10.66,4.92),('2016-06-01',84.50,10.37,5.13),('2016-07-01',84.80,10.21,4.99),('2016-08-01',85.40,10.53,4.07),('2016-09-01',83.93,11.86,4.20),('2016-10-01',82.56,12.60,4.84),('2016-11-01',82.99,12.36,4.65),('2016-12-01',84.88,10.43,4.69),('2017-01-01',87.33,7.78,4.89),('2017-02-01',87.32,7.88,4.80),('2017-03-01',86.18,8.44,5.38),('2017-04-01',85.43,9.30,5.27),('2017-05-01',84.73,10.27,5.00),('2017-06-01',84.00,11.00,5.00),('2017-07-01',85.73,10.35,3.92),('2017-08-01',83.32,11.75,4.93),('2017-09-01',80.05,14.44,5.51),('2017-10-01',81.27,12.94,5.80),('2017-11-01',82.30,11.48,6.22),('2017-12-01',85.29,8.44,6.27),('2018-01-01',86.94,7.07,5.98),('2018-02-01',87.72,7.20,5.08),('2018-03-01',85.10,8.70,6.19),('2018-04-01',84.67,10.05,5.28),('2018-05-01',85.88,9.47,4.66),('2018-06-01',85.76,9.78,4.47),('2018-07-01',84.21,11.00,4.80),('2018-08-01',80.01,14.44,5.55),('2018-09-01',78.58,17.42,4.00),('2018-10-01',81.85,14.03,4.13),('2018-11-01',83.16,12.82,4.03),('2018-12-01',86.21,9.30,4.48),('2019-01-01',87.98,7.03,5.00),('2019-02-01',88.66,6.51,4.83),('2019-03-01',89.08,6.42,4.50),('2019-04-01',87.57,7.75,4.69),('2019-05-01',88.18,7.56,4.26),('2019-06-01',87.60,8.27,4.13),('2019-07-01',84.78,11.60,3.62),('2019-08-01',83.63,13.08,3.29),('2019-09-01',81.48,15.19,3.33),('2019-10-01',82.12,14.23,3.64),('2019-11-01',82.50,13.72,3.78),('2019-12-01',87.71,8.89,3.40),('2020-01-01',89.41,6.89,3.70),('2020-02-01',89.46,6.71,3.83),('2020-03-01',90.12,6.05,3.83),('2020-04-01',91.82,5.10,3.07),('2020-05-01',90.65,5.93,3.42),('2020-06-01',89.55,7.74,2.71),('2020-07-01',88.07,9.13,2.79),('2020-08-01',86.11,11.49,2.39),('2020-09-01',83.89,13.66,2.45),('2020-10-01',85.03,12.42,2.55),('2020-11-01',84.90,11.59,3.50),('2020-12-01',87.62,9.28,3.10),('2021-01-01',88.51,8.01,3.48),('2021-02-01',88.76,8.03,3.21),('2021-03-01',88.77,7.76,3.48),('2021-04-01',88.88,7.93,3.19),('2021-05-01',88.27,9.13,2.60),('2021-06-01',86.68,10.31,3.01),('2021-07-01',84.89,12.16,2.95),('2021-08-01',83.66,13.45,2.89),('2021-09-01',83.44,13.62,2.94),('2021-10-01',84.19,12.68,3.13),('2021-11-01',85.71,11.76,2.53),('2021-12-01',89.18,8.47,2.34),('2022-01-01',90.99,6.80,2.21),('2022-02-01',91.26,6.73,2.01),('2022-03-01',91.71,6.75,1.55);
/*!40000 ALTER TABLE `disponibilidade` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-18 20:59:07
