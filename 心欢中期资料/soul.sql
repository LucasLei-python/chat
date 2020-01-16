-- MySQL dump 10.13  Distrib 5.7.28, for Linux (x86_64)
--
-- Host: localhost    Database: soul
-- ------------------------------------------------------
-- Server version	5.7.28-0ubuntu0.18.04.4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `menber_level`
--

DROP TABLE IF EXISTS `menber_level`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menber_level` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `level` varchar(20) DEFAULT NULL,
  `money` decimal(10,2) DEFAULT NULL,
  `inituid` varchar(20) DEFAULT NULL,
  `inittime` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menber_level`
--

LOCK TABLES `menber_level` WRITE;
/*!40000 ALTER TABLE `menber_level` DISABLE KEYS */;
/*!40000 ALTER TABLE `menber_level` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_comment`
--

DROP TABLE IF EXISTS `user_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` varchar(20) DEFAULT NULL,
  `comment` varchar(500) DEFAULT NULL,
  `init_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `reply` varchar(500) DEFAULT NULL,
  `reply_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_comment`
--

LOCK TABLES `user_comment` WRITE;
/*!40000 ALTER TABLE `user_comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_info`
--

DROP TABLE IF EXISTS `user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_info` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `pwd` varchar(50) NOT NULL,
  `user_type` char(1) NOT NULL DEFAULT '0',
  `sex` set('男','女') NOT NULL,
  `tel` char(11) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  `address` varchar(20) DEFAULT NULL,
  `graph` blob,
  `inituid` varchar(20) DEFAULT NULL,
  `init_time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=1001 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_info`
--

LOCK TABLES `user_info` WRITE;
/*!40000 ALTER TABLE `user_info` DISABLE KEYS */;
INSERT INTO `user_info` VALUES (1000,'系统账户','password.123','2','男','13147055486','826746996@qq.com','深圳',NULL,'lucas','2019-12-19 12:01:29');
/*!40000 ALTER TABLE `user_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_life_circle`
--

DROP TABLE IF EXISTS `user_life_circle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_life_circle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` varchar(30) DEFAULT NULL,
  `content` varchar(2000) DEFAULT NULL,
  `posted_time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_life_circle`
--

LOCK TABLES `user_life_circle` WRITE;
/*!40000 ALTER TABLE `user_life_circle` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_life_circle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_loginlogs`
--

DROP TABLE IF EXISTS `user_loginlogs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_loginlogs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `loguid` varchar(30) DEFAULT NULL,
  `login_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `logout_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_loginlogs`
--

LOCK TABLES `user_loginlogs` WRITE;
/*!40000 ALTER TABLE `user_loginlogs` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_loginlogs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_menber`
--

DROP TABLE IF EXISTS `user_menber`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_menber` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` varchar(20) DEFAULT NULL,
  `level` varchar(20) DEFAULT NULL,
  `fee_style` varchar(20) DEFAULT NULL,
  `money` decimal(10,2) DEFAULT NULL,
  `inituid` varchar(20) DEFAULT NULL,
  `inittime` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_menber`
--

LOCK TABLES `user_menber` WRITE;
/*!40000 ALTER TABLE `user_menber` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_menber` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_type`
--

DROP TABLE IF EXISTS `user_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usertype` char(1) DEFAULT NULL COMMENT '用户类别：0表示普通会员，1表示VIP，2表示系统管理员',
  `description` varchar(20) DEFAULT NULL,
  `inituid` varchar(20) DEFAULT NULL,
  `inittime` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_type`
--

LOCK TABLES `user_type` WRITE;
/*!40000 ALTER TABLE `user_type` DISABLE KEYS */;
INSERT INTO `user_type` VALUES (1,'0','普通用户','lucas','2019-12-19 12:35:54'),(2,'1','VIP','lucas','2019-12-19 12:35:54'),(3,'2','系统账户','lucas','2019-12-19 12:35:54');
/*!40000 ALTER TABLE `user_type` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-25 18:59:20
