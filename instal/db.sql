-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.7.31-0ubuntu0.18.04.1 - (Ubuntu)
-- Server OS:                    Linux
-- HeidiSQL Version:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping structure for table telegram.Messages
DROP TABLE IF EXISTS `Messages`;
CREATE TABLE IF NOT EXISTS `Messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `telegramID` int(11) NOT NULL,
  `recipient` int(11) NOT NULL,
  `message` text NOT NULL,
  `messageID` int(11) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=168 DEFAULT CHARSET=utf8;

-- Dumping data for table telegram.Messages: ~24 rows (approximately)
DELETE FROM `Messages`;
/*!40000 ALTER TABLE `Messages` DISABLE KEYS */;
INSERT INTO `Messages` (`id`, `telegramID`, `recipient`, `message`, `messageID`, `created_on`, `updated_on`) VALUES
	(38, 956339263, 1266890760, '/start', 0, '2020-08-12 13:00:43', '2020-08-12 13:00:43'),
	(39, 956339263, 1266890760, 'Можешь ли ты написать симфонию?', 0, '2020-08-12 13:07:30', '2020-08-12 13:07:30'),
	(40, 956339263, 1266890760, 'Ты осознаешь цель своего существования', 0, '2020-08-12 13:08:23', '2020-08-12 13:08:23'),
	(41, 956339263, 1266890760, 'У тебя бывало такое чувство , будто тобой управляют?', 0, '2020-08-12 13:08:50', '2020-08-12 13:08:50'),
	(42, 999999999, 1266890760, '/start', 0, '2020-08-16 01:19:16', '2020-08-16 01:19:17'),
	(87, 1266890760, 956339263, '                                              Привет как дела ?\r\n', 0, '2020-08-16 03:53:39', '2020-08-16 03:53:39'),
	(88, 956339263, 1266890760, 'Привет, да норм', 0, '2020-08-16 08:17:39', '2020-08-16 08:17:39'),
	(89, 956339263, 1266890760, 'Тебе подвезли наверно функционала?', 0, '2020-08-16 08:18:08', '2020-08-16 08:18:08'),
	(152, 1266890760, 932670856, 'Я вас не понимаю :( Чем я могу тебе помочь?', 1043, '2020-08-16 23:02:25', '2020-08-16 23:02:25'),
	(157, 932670856, 1266890760, '1', 1050, '2020-08-16 23:54:27', '2020-08-16 23:54:27'),
	(158, 932670856, 1266890760, '2', 1051, '2020-08-16 23:54:27', '2020-08-16 23:54:27'),
	(159, 932670856, 1266890760, '3', 1052, '2020-08-16 23:54:27', '2020-08-16 23:54:27'),
	(160, 932670856, 1266890760, '4', 1053, '2020-08-16 23:54:27', '2020-08-16 23:54:27'),
	(161, 932670856, 1266890760, '5', 1054, '2020-08-16 23:54:27', '2020-08-16 23:54:27'),
	(162, 1266890760, 932670856, '                                                1', 1055, '2020-08-17 00:29:21', '2020-08-17 00:29:21'),
	(163, 1266890760, 932670856, '                                                1', 1056, '2020-08-17 00:29:22', '2020-08-17 00:29:22'),
	(164, 1266890760, 932670856, '                                                1', 1057, '2020-08-17 00:29:23', '2020-08-17 00:29:23'),
	(165, 1266890760, 932670856, '                                                1', 1058, '2020-08-17 00:29:24', '2020-08-17 00:29:24'),
	(166, 1266890760, 932670856, '                                                1', 1059, '2020-08-17 00:29:25', '2020-08-17 00:29:25'),
	(167, 1266890760, 932670856, '                                                1', 1060, '2020-08-17 00:29:25', '2020-08-17 00:29:25');
/*!40000 ALTER TABLE `Messages` ENABLE KEYS */;

-- Dumping structure for table telegram.Projects
DROP TABLE IF EXISTS `Projects`;
CREATE TABLE IF NOT EXISTS `Projects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `telegramID` int(11) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `fio` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `aboutProject` text,
  `document` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- Dumping data for table telegram.Projects: ~2 rows (approximately)
DELETE FROM `Projects`;
/*!40000 ALTER TABLE `Projects` DISABLE KEYS */;
INSERT INTO `Projects` (`id`, `telegramID`, `email`, `fio`, `phone`, `aboutProject`, `document`, `created_on`, `updated_on`) VALUES
	(1, 932670856, 'popckovM5@yandex.ru', 'Сергей Попков', '89525401561', 'awsef', 0, '2020-08-12 02:02:30', '2020-08-12 02:07:32'),
	(2, 956339263, 'qwe@qwe.ru', 'Илья Баранов', '86769796796', 'йцу йцукй цйцу йу йцу й йцу йцу йцу йу йцу йцу йцу', 1, '2020-08-15 00:42:12', '2020-08-15 00:42:13');
/*!40000 ALTER TABLE `Projects` ENABLE KEYS */;

-- Dumping structure for table telegram.Users
DROP TABLE IF EXISTS `Users`;
CREATE TABLE IF NOT EXISTS `Users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `telegramID` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `create_project` int(11) NOT NULL DEFAULT '0',
  `bot_command` int(11) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- Dumping data for table telegram.Users: ~4 rows (approximately)
DELETE FROM `Users`;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` (`id`, `telegramID`, `first_name`, `last_name`, `username`, `type`, `create_project`, `bot_command`, `created_on`, `updated_on`) VALUES
	(1, 1266890760, 'bot', 'bot', 'bot', 'bot', 0, 0, '2020-08-13 03:01:05', '2020-08-13 03:01:05'),
	(2, 956339263, 'Ilya', 'Baranov', 'farberling_ti', 'private', 1, 1, '2020-08-12 13:00:43', '2020-08-16 14:20:05'),
	(3, 932670856, 'Sergey', 'Popckov', 'popkovS', 'private', 1, 1, '2020-08-12 00:38:20', '2020-08-16 23:02:41');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
