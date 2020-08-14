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
  `created_on` datetime DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8;

-- Dumping data for table telegram.Messages: ~19 rows (approximately)
DELETE FROM `Messages`;
/*!40000 ALTER TABLE `Messages` DISABLE KEYS */;
INSERT INTO `Messages` (`id`, `telegramID`, `recipient`, `message`, `created_on`, `updated_on`) VALUES
	(1, 932670856, 1266890760, '/start', '2020-08-12 02:01:30', '2020-08-12 02:01:30'),
	(2, 932670856, 1266890760, 'Привет бот', '2020-08-12 02:01:44', '2020-08-12 02:01:44'),
	(3, 1266890760, 932670856, 'Я вас не понимаю :( Чем я могу тебе помочь?', '2020-08-12 02:01:44', '2020-08-12 02:01:44'),
	(4, 932670856, 1266890760, 'Факты о нас', '2020-08-12 02:01:57', '2020-08-12 02:01:57'),
	(5, 1266890760, 932670856, 'Пользователю показан блок \'Факты о нас\'', '2020-08-12 02:01:57', '2020-08-12 02:01:57'),
	(6, 932670856, 1266890760, 'Наши цены', '2020-08-12 02:02:04', '2020-08-12 02:02:04'),
	(7, 1266890760, 932670856, 'Пользователю показан блок \'Услуг Компании\'', '2020-08-12 02:02:04', '2020-08-12 02:02:04'),
	(8, 932670856, 1266890760, 'Наши реквизиты', '2020-08-12 02:02:07', '2020-08-12 02:02:07'),
	(9, 1266890760, 932670856, 'Пользователю показан блок \'Наши реквизиты\'', '2020-08-12 02:02:07', '2020-08-12 02:02:07'),
	(10, 932670856, 1266890760, 'Расчитать стоимость проекта', '2020-08-12 02:02:13', '2020-08-12 02:02:13'),
	(11, 1266890760, 932670856, 'Как Вас зовут?', '2020-08-12 02:02:13', '2020-08-12 02:02:13'),
	(12, 932670856, 1266890760, 'Сергей Попков', '2020-08-12 02:02:30', '2020-08-12 02:02:30'),
	(13, 1266890760, 932670856, 'Ваш email ?', '2020-08-12 02:02:30', '2020-08-12 02:02:30'),
	(14, 932670856, 1266890760, 'popckovM5@yandex.ru', '2020-08-12 02:02:54', '2020-08-12 02:02:54'),
	(15, 1266890760, 932670856, 'Ваш телефон ?', '2020-08-12 02:02:54', '2020-08-12 02:02:54'),
	(16, 932670856, 1266890760, '345efdgdfsg', '2020-08-12 02:03:04', '2020-08-12 02:03:04'),
	(17, 1266890760, 932670856, 'Кажется, это неправильный телефона :( Попробуй еще раз!', '2020-08-12 02:03:04', '2020-08-12 02:03:04'),
	(18, 932670856, 1266890760, '89525401561', '2020-08-12 02:03:41', '2020-08-12 02:03:41'),
	(19, 1266890760, 932670856, 'Расскажите о Вашем проекте', '2020-08-12 02:03:41', '2020-08-12 02:03:41'),
	(20, 932670856, 1266890760, 'Ну там, то да се, тудым сюдым, там пых распыхчих, не то так это', '2020-08-12 02:04:13', '2020-08-12 02:04:13'),
	(21, 1266890760, 932670856, 'Пользователю задан вопрос \'Правильно ли заполнил данные\'', '2020-08-12 02:04:13', '2020-08-12 02:04:13'),
	(22, 932670856, 1266890760, 'Ну там, то да се, тудым сюдым, там пых распыхчих, не то так это', '2020-08-12 02:04:13', '2020-08-12 02:04:13'),
	(23, 932670856, 1266890760, 'фыва', '2020-08-12 02:07:10', '2020-08-12 02:07:10'),
	(24, 1266890760, 932670856, 'Я вас не понимаю :( Чем я могу тебе помочь?', '2020-08-12 02:07:10', '2020-08-12 02:07:10'),
	(25, 932670856, 1266890760, 'Расчитать стоимость проекта', '2020-08-12 02:07:13', '2020-08-12 02:07:13'),
	(26, 1266890760, 932670856, 'Как Вас зовут?', '2020-08-12 02:07:13', '2020-08-12 02:07:13'),
	(27, 932670856, 1266890760, '111111', '2020-08-12 02:07:18', '2020-08-12 02:07:18'),
	(28, 1266890760, 932670856, 'Ваш email ?', '2020-08-12 02:07:18', '2020-08-12 02:07:18'),
	(29, 932670856, 1266890760, 'popckovM5@yandex.ru', '2020-08-12 02:07:26', '2020-08-12 02:07:26'),
	(30, 1266890760, 932670856, 'Ваш телефон ?', '2020-08-12 02:07:26', '2020-08-12 02:07:26'),
	(31, 932670856, 1266890760, '89525401561', '2020-08-12 02:07:31', '2020-08-12 02:07:31'),
	(32, 1266890760, 932670856, 'Расскажите о Вашем проекте', '2020-08-12 02:07:31', '2020-08-12 02:07:31'),
	(33, 932670856, 1266890760, 'awsef', '2020-08-12 02:07:32', '2020-08-12 02:07:32'),
	(34, 1266890760, 932670856, 'Пользователю задан вопрос \'Правильно ли заполнил данные\'', '2020-08-12 02:07:32', '2020-08-12 02:07:32'),
	(35, 1266890760, 932670856, 'Пользователю задан вопрос \'Правильно ли заполнил данные\'', '2020-08-12 02:07:32', '2020-08-12 02:07:32'),
	(36, 932670856, 1266890760, 'ghj', '2020-08-12 12:56:45', '2020-08-12 12:56:45'),
	(37, 1266890760, 932670856, 'Я вас не понимаю :( Чем я могу тебе помочь?', '2020-08-12 12:56:45', '2020-08-12 12:56:45'),
	(38, 956339263, 1266890760, '/start', '2020-08-12 13:00:43', '2020-08-12 13:00:43'),
	(39, 956339263, 1266890760, 'Можешь ли ты написать симфонию?', '2020-08-12 13:07:30', '2020-08-12 13:07:30'),
	(40, 956339263, 1266890760, 'Ты осознаешь цель своего существования', '2020-08-12 13:08:23', '2020-08-12 13:08:23'),
	(41, 956339263, 1266890760, 'У тебя бывало такое чувство , будто тобой управляют?', '2020-08-12 13:08:50', '2020-08-12 13:08:50');
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
  `created_on` datetime DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Dumping data for table telegram.Projects: ~0 rows (approximately)
DELETE FROM `Projects`;
/*!40000 ALTER TABLE `Projects` DISABLE KEYS */;
INSERT INTO `Projects` (`id`, `telegramID`, `email`, `fio`, `phone`, `aboutProject`, `created_on`, `updated_on`) VALUES
	(1, 932670856, 'popckovM5@yandex.ru', 'Сергей Попков', '89525401561', 'awsef', '2020-08-12 02:02:30', '2020-08-12 02:07:32');
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
  `bot_command` int(11) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- Dumping data for table telegram.Users: ~0 rows (approximately)
DELETE FROM `Users`;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` (`id`, `telegramID`, `first_name`, `last_name`, `username`, `type`, `bot_command`, `created_on`, `updated_on`) VALUES
	(1, 932670856, 'Sergey', 'Popckov', 'popkovS', 'private', 0, '2020-08-12 00:38:20', '2020-08-12 00:38:20'),
	(2, 956339263, 'Ilya', 'Baranov', 'farberling_ti', 'private', 0, '2020-08-12 13:00:43', '2020-08-12 13:00:43');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;