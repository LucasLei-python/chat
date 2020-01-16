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
-- Table structure for table `chat`
--

DROP TABLE IF EXISTS `chat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chat` (
  `sender` char(30) NOT NULL,
  `receiver` char(30) NOT NULL,
  `content` varchar(500) NOT NULL,
  `time` datetime NOT NULL,
  `status` char(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat`
--

LOCK TABLES `chat` WRITE;
/*!40000 ALTER TABLE `chat` DISABLE KEYS */;
INSERT INTO `chat` VALUES ('client_1','client_2','2313132132','2020-01-14 20:20:35','');
/*!40000 ALTER TABLE `chat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hobby`
--

DROP TABLE IF EXISTS `hobby`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hobby` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `interest` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hobby`
--

LOCK TABLES `hobby` WRITE;
/*!40000 ALTER TABLE `hobby` DISABLE KEYS */;
/*!40000 ALTER TABLE `hobby` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Table structure for table `personal_hobby`
--

DROP TABLE IF EXISTS `personal_hobby`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `personal_hobby` (
  `uid` int(11) DEFAULT NULL,
  `id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal_hobby`
--

LOCK TABLES `personal_hobby` WRITE;
/*!40000 ALTER TABLE `personal_hobby` DISABLE KEYS */;
/*!40000 ALTER TABLE `personal_hobby` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  `loguid` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test`
--

LOCK TABLES `test` WRITE;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;
INSERT INTO `test` VALUES (1,'aaa');
/*!40000 ALTER TABLE `test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_circle_comment`
--

DROP TABLE IF EXISTS `user_circle_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_circle_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` varchar(10) DEFAULT NULL,
  `circle_id` varchar(10) DEFAULT NULL,
  `comment` varchar(500) DEFAULT NULL,
  `kiss` int(11) DEFAULT '0',
  `inittime` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_circle_comment`
--

LOCK TABLES `user_circle_comment` WRITE;
/*!40000 ALTER TABLE `user_circle_comment` DISABLE KEYS */;
INSERT INTO `user_circle_comment` VALUES (2,'1002','2','哈哈,一起吧',1,'2020-01-10 11:49:24'),(3,'1003','2','没啥好吃的,有什么可以推荐的么',1,'2020-01-11 10:59:30'),(4,'1003','1','可以放心出门',1,'2020-01-11 10:59:30'),(5,'1003','4','ok',NULL,NULL),(6,'1005','4','face[ok] ',NULL,NULL),(7,'1005','4','13',NULL,NULL),(8,'1005','4','已准备就绪',NULL,NULL),(9,'1005','4','fdf',NULL,NULL),(10,'1005','4','1323333',NULL,'2020-01-15 20:48:40'),(11,'1005','3','face[嘘] ',NULL,'2020-01-15 20:48:40'),(12,'1005','4','dfd[hr]dfd',NULL,'2020-01-15 20:58:52');
/*!40000 ALTER TABLE `user_circle_comment` ENABLE KEYS */;
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
  `sex` set('男','女') DEFAULT NULL,
  `tel` char(11) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  `address` varchar(20) DEFAULT NULL,
  `graph` blob,
  `signature` varchar(200) DEFAULT NULL,
  `inituid` varchar(20) DEFAULT NULL,
  `init_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `modifyuid` varchar(20) DEFAULT NULL,
  `modifydate` datetime DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=1013 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_info`
--

LOCK TABLES `user_info` WRITE;
/*!40000 ALTER TABLE `user_info` DISABLE KEYS */;
INSERT INTO `user_info` VALUES (1000,'系统账户','123','8','男','13147055486','826746997@qq.com','深圳',NULL,'fnsaidf ','lucas','2019-12-19 12:01:29',NULL,NULL),(1002,'上山打老虎','f546321.','0',NULL,NULL,'lucaslei@163.com',NULL,NULL,NULL,NULL,'2020-01-09 10:46:01',NULL,NULL),(1003,'fan','666666','0',NULL,NULL,'1024786993@qq.com',NULL,NULL,NULL,NULL,'2020-01-09 19:25:45',NULL,NULL),(1005,'test','123456','0','','','826746996@qq.com','','',NULL,NULL,'2020-01-13 14:34:50',NULL,NULL),(1006,'yan','333333','0','','','1513857399@qq.com','','',NULL,NULL,'2020-01-13 19:19:41',NULL,NULL),(1007,'test1','666666','0',NULL,NULL,'556325@qq.com',NULL,NULL,NULL,NULL,'2020-01-15 14:53:06',NULL,NULL),(1008,'test2','666666','0',NULL,NULL,'5562325@qq.com',NULL,NULL,NULL,NULL,'2020-01-15 14:53:06',NULL,NULL),(1009,'test3','666666','0',NULL,NULL,'5526325@qq.com',NULL,NULL,NULL,NULL,'2020-01-15 14:53:36',NULL,NULL),(1010,'test4','666666','0',NULL,NULL,'25562325@qq.com',NULL,NULL,NULL,NULL,'2020-01-15 14:53:36',NULL,NULL),(1011,'test5','666666','0',NULL,NULL,'55263325@qq.com',NULL,NULL,NULL,NULL,'2020-01-15 14:54:05',NULL,NULL),(1012,'test6','666666','0',NULL,NULL,'252562325@qq.com',NULL,NULL,NULL,NULL,'2020-01-15 14:54:05',NULL,NULL);
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
  `see_type` varchar(10) DEFAULT NULL,
  `title` varchar(500) DEFAULT NULL,
  `class_type` varchar(10) DEFAULT NULL,
  `content` varchar(2000) DEFAULT NULL,
  `posted_time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_life_circle`
--

LOCK TABLES `user_life_circle` WRITE;
/*!40000 ALTER TABLE `user_life_circle` DISABLE KEYS */;
INSERT INTO `user_life_circle` VALUES (1,'1002',NULL,NULL,'动态','今天天气真好','2020-01-11 11:53:55'),(2,'1002',NULL,NULL,'动态','中午吃黄焖鸡','2020-01-10 16:13:05'),(3,'1005',NULL,'test','动态','face[右哼哼] face[左哼哼] ','2020-01-13 15:31:15'),(4,'1000','ALL','答辩通知','公告','答辩在即,大家做好准备工作,挑自己最熟悉的部分讲face[good] ','2020-01-15 18:05:34');
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
) ENGINE=InnoDB AUTO_INCREMENT=99 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_loginlogs`
--

LOCK TABLES `user_loginlogs` WRITE;
/*!40000 ALTER TABLE `user_loginlogs` DISABLE KEYS */;
INSERT INTO `user_loginlogs` VALUES (1,'1000','2019-12-26 15:44:50',NULL),(2,'1000','2019-12-26 17:11:45',NULL),(3,'1000','2019-12-26 18:35:35',NULL),(4,'1000','2019-12-26 18:48:00',NULL),(5,'1000','2019-12-26 18:49:58',NULL),(6,'1000','2019-12-26 18:50:58',NULL),(7,'1000','2019-12-26 18:51:53',NULL),(8,'1000','2019-12-26 18:53:13',NULL),(9,'1000','2019-12-26 21:24:41',NULL),(10,'1000','2019-12-27 09:08:18',NULL),(11,'1000','2019-12-27 09:09:53',NULL),(12,'1000','2019-12-30 12:29:11',NULL),(13,'1000','2019-12-30 14:22:58',NULL),(14,'1000','2019-12-30 14:26:50',NULL),(15,'1000','2019-12-30 14:35:07',NULL),(16,'1000','2019-12-30 14:35:11',NULL),(17,'1000','2019-12-30 14:41:12',NULL),(18,'1000','2019-12-30 14:43:48',NULL),(19,'1000','2019-12-30 19:10:18',NULL),(20,'1000','2019-12-30 19:11:48',NULL),(21,'1000','2019-12-30 19:35:16',NULL),(22,'1000','2020-01-02 20:35:57',NULL),(23,'826746996@qq.com','2020-01-07 14:17:12',NULL),(24,'1000','2020-01-07 14:19:29',NULL),(25,'1000','2020-01-07 15:08:17',NULL),(26,'1000','2020-01-07 15:08:31',NULL),(27,'1000','2020-01-07 15:08:33',NULL),(28,'1000','2020-01-07 15:20:47',NULL),(29,'1000','2020-01-07 15:24:51',NULL),(30,'1000','2020-01-07 15:25:49',NULL),(31,'1000','2020-01-07 15:28:31',NULL),(32,'1000','2020-01-07 15:29:59',NULL),(33,'1000','2020-01-07 16:03:49',NULL),(34,'1000','2020-01-07 16:48:48',NULL),(35,'1000','2020-01-07 18:50:14',NULL),(36,'1000','2020-01-07 19:07:23',NULL),(37,'1000','2020-01-07 19:07:58',NULL),(38,'1000','2020-01-07 19:45:52',NULL),(39,'1000','2020-01-08 10:58:33',NULL),(40,'1000','2020-01-08 11:00:09',NULL),(41,'1000','2020-01-08 11:01:22',NULL),(42,'1000','2020-01-08 11:02:22',NULL),(43,'1000','2020-01-08 11:56:11',NULL),(44,'1000','2020-01-08 11:59:41',NULL),(45,'1000','2020-01-08 18:40:17',NULL),(46,'1000','2020-01-09 08:59:21',NULL),(47,'1000','2020-01-09 09:48:34',NULL),(48,'1000','2020-01-09 09:50:14',NULL),(49,'1000','2020-01-09 09:51:26',NULL),(50,'1002','2020-01-09 10:46:46',NULL),(51,'1002','2020-01-09 10:48:44',NULL),(52,'1000','2020-01-09 10:50:59',NULL),(53,'1000','2020-01-09 11:51:54',NULL),(54,'1000','2020-01-09 19:11:06',NULL),(55,'1000','2020-01-09 19:11:23',NULL),(56,'1000','2020-01-09 19:11:29',NULL),(57,'1000','2020-01-09 19:11:30',NULL),(58,'1000','2020-01-09 19:11:37',NULL),(59,'1000','2020-01-09 19:16:57',NULL),(60,'1003','2020-01-09 19:26:37',NULL),(61,'1000','2020-01-10 09:03:38',NULL),(62,'1000','2020-01-10 09:04:59',NULL),(63,'1000','2020-01-10 09:25:36',NULL),(64,'1000','2020-01-10 09:35:01',NULL),(65,'1000','2020-01-10 10:08:11',NULL),(66,'1000','2020-01-10 10:24:16',NULL),(67,'1000','2020-01-10 10:26:48',NULL),(68,'1000','2020-01-10 10:28:45',NULL),(69,'1000','2020-01-10 10:40:34',NULL),(70,'1000','2020-01-10 10:44:34',NULL),(71,'1000','2020-01-10 16:37:22',NULL),(72,'1000','2020-01-10 16:39:35',NULL),(73,'1000','2020-01-10 16:59:22',NULL),(74,'1000','2020-01-10 17:34:52',NULL),(75,'1000','2020-01-10 21:47:23',NULL),(76,'1000','2020-01-11 12:54:11',NULL),(77,'1000','2020-01-11 15:47:11',NULL),(78,'1000','2020-01-11 16:07:02',NULL),(79,'1002','2020-01-11 16:20:26',NULL),(80,'1000','2020-01-11 16:23:06',NULL),(81,'1000','2020-01-11 17:48:18',NULL),(82,'1000','2020-01-13 08:48:21',NULL),(83,'1005','2020-01-13 14:35:50',NULL),(84,'1005','2020-01-13 15:26:35',NULL),(85,'1005','2020-01-13 18:56:13',NULL),(86,'1000','2020-01-13 18:57:35',NULL),(87,'1000','2020-01-13 19:15:06',NULL),(88,'1006','2020-01-13 19:20:22',NULL),(89,'1000','2020-01-13 19:33:41',NULL),(90,'1000','2020-01-13 19:47:59',NULL),(91,'1000','2020-01-13 20:44:14',NULL),(92,'1000','2020-01-14 13:11:14',NULL),(93,'1003','2020-01-14 14:18:18',NULL),(94,'1010','2020-01-15 14:59:16',NULL),(95,'1000','2020-01-15 17:43:31',NULL),(96,'1000','2020-01-15 18:02:06',NULL),(97,'1003','2020-01-15 18:39:23',NULL),(98,'1005','2020-01-15 20:39:51',NULL);
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
-- Table structure for table `user_sign_in`
--

DROP TABLE IF EXISTS `user_sign_in`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_sign_in` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` varchar(10) DEFAULT NULL,
  `kiss_count` int(11) DEFAULT NULL,
  `kiss_day` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_sign_in`
--

LOCK TABLES `user_sign_in` WRITE;
/*!40000 ALTER TABLE `user_sign_in` DISABLE KEYS */;
INSERT INTO `user_sign_in` VALUES (2,'1000',5,'2020-01-13'),(3,'1005',5,'2020-01-13'),(4,'1006',5,'2020-01-13'),(5,'1005',5,'2020-01-15');
/*!40000 ALTER TABLE `user_sign_in` ENABLE KEYS */;
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

--
-- Table structure for table `vertify_code`
--

DROP TABLE IF EXISTS `vertify_code`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vertify_code` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) DEFAULT NULL,
  `code` char(6) DEFAULT NULL,
  `inittime` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vertify_code`
--

LOCK TABLES `vertify_code` WRITE;
/*!40000 ALTER TABLE `vertify_code` DISABLE KEYS */;
INSERT INTO `vertify_code` VALUES (1,'826746996@qq.com','123456','2020-01-04 17:00:00'),(2,'826746996@qq.com','123456','2020-01-04 17:28:12'),(3,'826746996@qq.com','694732','2020-01-04 17:48:51'),(4,'826746996@qq.com','913746','2020-01-04 18:01:54'),(5,'1024786993@qq.com','738694','2020-01-06 09:39:28'),(6,'1024786993@qq.com','418329','2020-01-06 09:55:48'),(7,'1024786993@qq.com','978614','2020-01-06 14:32:01'),(8,'1024786993@qq.com','756839','2020-01-06 18:54:10'),(9,'1027486993@qq.com','284736','2020-01-06 18:58:08'),(10,'1024786993@qq.com','174285','2020-01-06 19:00:17'),(11,'1024786993@qq.com','819267','2020-01-06 19:06:33'),(12,'1024786993@qq.com','691745','2020-01-06 19:12:02'),(13,'1024786993@qq.com','679183','2020-01-06 20:40:40'),(14,'1024786993@qq.com','457321','2020-01-06 20:50:19'),(15,'1024786993@qq.com','298634','2020-01-06 20:57:31'),(16,'1024786993@qq.com','814635','2020-01-06 21:03:52'),(17,'1024786993@qq.com','351672','2020-01-06 21:16:40'),(18,'1024786993@qq.com','496325','2020-01-06 21:22:21'),(19,'1024786993@qq.com','265971','2020-01-06 21:28:12'),(20,'1024786993@qq.com','679435','2020-01-06 21:34:16'),(21,'1024786993@qq.com','723985','2020-01-07 13:55:49'),(22,'1024786993@qq.com','631728','2020-01-07 14:01:40'),(23,'1024786993@qq.com','391687','2020-01-07 14:07:48'),(24,'1024786993@qq.com','578926','2020-01-07 15:07:31'),(25,'8555','198536','2020-01-07 16:58:31'),(26,'826746996@qq.com','574821','2020-01-07 17:15:00'),(27,'826666','812469','2020-01-07 17:20:28'),(28,'','763521','2020-01-07 17:20:57'),(29,'826746996@qq.com','831269','2020-01-07 17:22:56'),(30,'826746996@qq.com','924356','2020-01-07 17:31:55'),(31,'826746996@qq.com','463857','2020-01-07 17:44:26'),(32,'826746996@qq.com','391824','2020-01-07 18:09:48'),(33,'826746996@qq.com','937652','2020-01-07 18:16:52'),(34,'826746996@qq.com','376298','2020-01-07 18:38:18'),(35,'826746996@qq.com','689423','2020-01-07 18:46:04'),(36,'826746996@qq.com','912578','2020-01-07 19:01:51'),(37,'826746996@qq.com','924537','2020-01-07 19:13:03'),(38,'826746996@qq.com','462879','2020-01-07 19:33:11'),(39,'1513857399@qq.com','736248','2020-01-07 19:44:19'),(40,'826746996@qq.com','839257','2020-01-07 20:21:36'),(41,'826746996@qq.com','194325','2020-01-07 20:27:58'),(42,'826746996@qq.com','423857','2020-01-07 20:40:42'),(43,'826746996@qq.com','915267','2020-01-07 20:47:55'),(44,'826746996@qq.com','963742','2020-01-07 20:55:43'),(45,'826746996@qq.com','324597','2020-01-07 21:05:12'),(46,'826746996@qq.com','934651','2020-01-07 21:11:53'),(47,'826746996@qq.com','791632','2020-01-08 09:06:43'),(48,'826746996@qq.com','648523','2020-01-08 09:17:30'),(49,'826746996@qq.com','816532','2020-01-08 09:23:42'),(50,'826746996@qq.com','493815','2020-01-08 09:30:32'),(51,'826746996@qq.com','127983','2020-01-08 09:38:21'),(52,'826746996@qq.com','294831','2020-01-08 09:49:59'),(53,'826746996@qq.com','572468','2020-01-08 09:59:36'),(54,'826746996@qq.com','742813','2020-01-08 10:09:25'),(55,'826746996@qq.com','682591','2020-01-08 10:19:08'),(56,'826746996@qq.com','693541','2020-01-08 10:25:30'),(57,'826746996@qq.com','743296','2020-01-08 10:33:24'),(58,'826746996@qq.com','813597','2020-01-08 11:34:11'),(59,'lucaslei1991@163.com','562197','2020-01-08 13:00:28'),(60,'lucaslei1991@163.com','854123','2020-01-08 14:18:18'),(61,'82674696@qq.com','439278','2020-01-08 18:36:27'),(62,'lucaslei@163.com','253648','2020-01-08 18:58:25'),(63,'lucaslei1991@163.com','865741','2020-01-08 19:00:46'),(64,'lucaslei1991@163.com','458361','2020-01-08 19:13:47'),(65,'lucaslei1991@163.com','475138','2020-01-08 19:33:23'),(66,'lucaslei1991@163.com','932751','2020-01-08 19:43:00'),(67,'lucaslei1991@163.com','389452','2020-01-09 10:45:10'),(68,'1024786993@qq.com','132856','2020-01-09 19:25:19'),(69,'826746996@qq.com','325841','2020-01-13 14:26:06'),(70,'826746996@qq.com','719482','2020-01-13 14:34:35'),(71,'102478993@qq.com','728419','2020-01-13 19:18:32'),(72,'1513857399@qq.com','425136','2020-01-13 19:19:09');
/*!40000 ALTER TABLE `vertify_code` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-15 21:26:43
