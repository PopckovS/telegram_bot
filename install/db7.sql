-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.7.32-0ubuntu0.18.04.1 - (Ubuntu)
-- Server OS:                    Linux
-- HeidiSQL Version:             11.1.0.6116
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for table bot.Company
DROP TABLE IF EXISTS `Company`;
CREATE TABLE IF NOT EXISTS `Company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `caption` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `requisites` text,
  `facts` text,
  `phone` varchar(50) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for table bot.CompanyDescription
DROP TABLE IF EXISTS `CompanyDescription`;
CREATE TABLE IF NOT EXISTS `CompanyDescription` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `text` text,
  `Company_id` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Company_id` (`Company_id`),
  CONSTRAINT `CompanyDescription_ibfk_1` FOREIGN KEY (`Company_id`) REFERENCES `Company` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for table bot.Telegram_Admin
DROP TABLE IF EXISTS `Telegram_Admin`;
CREATE TABLE IF NOT EXISTS `Telegram_Admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `phone_number` varchar(255) DEFAULT NULL,
  `telegramID` int(11) NOT NULL,
  `password` text NOT NULL,
  `get_messages` int(11) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for table bot.Telegram_Messages
DROP TABLE IF EXISTS `Telegram_Messages`;
CREATE TABLE IF NOT EXISTS `Telegram_Messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `telegramID` int(11) NOT NULL,
  `recipient` int(11) NOT NULL,
  `message` text NOT NULL,
  `messageID` int(11) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for table bot.Telegram_Projects
DROP TABLE IF EXISTS `Telegram_Projects`;
CREATE TABLE IF NOT EXISTS `Telegram_Projects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `telegramID` int(11) NOT NULL,
  `fio` varchar(255) DEFAULT NULL,
  `contacts` text,
  `aboutProject` text,
  `document` int(11) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for table bot.Telegram_User
DROP TABLE IF EXISTS `Telegram_User`;
CREATE TABLE IF NOT EXISTS `Telegram_User` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `telegramID` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `username` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `create_project` int(11) NOT NULL,
  `bot_command` int(11) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
