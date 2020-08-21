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

-- Dumping data for table bot.Company: ~0 rows (approximately)
DELETE FROM `Company`;
/*!40000 ALTER TABLE `Company` DISABLE KEYS */;
INSERT INTO `Company` (`id`, `name`, `caption`, `email`, `requisites`, `facts`, `phone`, `created_on`, `updated_on`) VALUES
	(1, 'Mitlabs', 'MITLABS — DIGITAL-ИНТЕГРАТОР\r\n               И IT-ЛАБОРАТОРИЯ ПОЛНОГО ЦИКЛА', 'info@mitlabs.ru', '     Реквизиты ООО «МИТЛАБС».\r\n        Адрес: 394006, город Воронеж, \r\n        проспект Революции 33б, 5 этаж\r\n        ООО «Митлабс» 394000, г. Воронеж, \r\n        Проспект Революции, д.33Б, 5 этаж ОГРН 1173668029370 \r\n        / ИНН 3666219432 \r\n        / КПП 366601001\r\n        Ген директор: Меньшикова Елена Александровна\r\n        mitlabs.ru\r\n        info@mitlabs.ru\r\n        +7 (495) 646–02–30\r\n        Р/с 40702810808500002246 \r\n        в ТОЧКА ПАО БАНКА ФК ОТКРЫТИЕ;\r\n        БИК: 044525999;\r\n        Корр.счет: 30101810845250000999;', 'ФАКТЫ:\r\n        1 место в конкурсе PlugAndPlay Moscow\r\n        3 собственных IT-проекта\r\n        450+ выполненных проектов\r\n        60+ сотрудников\r\n        10+ разработанных Highload-систем\r\n        150000+ часов работы', '+7 (495) 646 02 30', '2020-08-21 03:53:38', '2020-08-21 03:53:38');
/*!40000 ALTER TABLE `Company` ENABLE KEYS */;

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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- Dumping data for table bot.CompanyDescription: ~0 rows (approximately)
DELETE FROM `CompanyDescription`;
/*!40000 ALTER TABLE `CompanyDescription` DISABLE KEYS */;
INSERT INTO `CompanyDescription` (`id`, `title`, `text`, `Company_id`, `created_on`, `updated_on`) VALUES
	(1, 'Дизайн от А до Я', 'ДИЗАЙН ОТ А ДО Я\r\n            MITLabs — это команда экспертов в UX/UI-дизайне, \r\n            WEB- и графическом дизайне. Мы создаем удобные \r\n            интерфейсы с учетом потребностей пользователей, \r\n            разрабатываем графику, привлекающую внимание \r\n            целевой аудитории, продумываем визуал для \r\n            сайтов, на которые люди готовы возвращаться снова \r\n            и снова.\r\n            Стоимость работ от 2070 до 2860 рублей/час', 1, '2020-08-21 03:53:45', '2020-08-21 03:53:46'),
	(2, 'Маркетинг', 'СИСТЕМНЫЙ МАРКЕТИНГ\r\n            Системный подход в маркетинге,\r\n            это мощная методология  продвижения и увеличения \r\n            продаж, настоящее оружие массового поражения, \r\n            способное при грамотном применении вызвать взрыв \r\n            интереса и доверия к вашей компании у целевой \r\n            аудитории, создать экспертный облик и хорошую \r\n            репутацию, обеспечить рост продаж. Мы умеем \r\n            пользоваться этим оружием во благо наших клиентов.\r\n            Пожалуйста, оставьте свои контакты и мы рассчитаем \r\n            вам стоимость проекта.', 1, '2020-08-21 03:54:46', '2020-08-21 03:54:46'),
	(3, 'Разработка сайта', 'РАЗРАБОТКА\r\n            Разрабатываем сайты и приложения с учетом \r\n            особенностей вашего бизнеса, конкурентов, \r\n            требований и предпочтений целевой аудитории.\r\n            Мы предлагаем идеи, отвечающие вашим целям, \r\n            задачам и бюджету, создаем решения, которые \r\n            помогают продавать, развиваться и выстраивать \r\n            работающие каналы коммуникации с клиентами.\r\n            Стоимость работ от 1 760 до 2 860 рублей/час.', 1, '2020-08-21 03:55:09', '2020-08-21 03:55:09'),
	(4, 'E-COMMERCE', 'E-COMMERCE Продвигаем и продаем.\r\n            Мы исследуем лучший мировой опыт в сфере \r\n            электронной коммерции, разрабатываем и выпускаем \r\n            функциональные интернет-магазины для успешного \r\n            развития вашего бизнеса. Мы используем актуальную \r\n            статистику и тестируем решения перед внедрением, \r\n            а вы получаете новых клиентов и хороший трафик. \r\n            С нами даже высоконагруженный интернет-магазин \r\n            сможет принимать заказы с первого дня запуска.', 1, '2020-08-21 03:55:25', '2020-08-21 03:55:25'),
	(5, 'DEVOPS', 'DEVOPS, АДМИНИСТРИРОВАНИЕ, ТЕХНИЧЕСКАЯ ПОДДЕРЖКА\r\n            Мы интегрируем то,что должно быть интегрировано. \r\n            Code/Build/Test/Release! Круглосуточный мониторинг, \r\n            администрирование и техническая поддержка сайтов \r\n            любых размеров и сложности. Мы обеспечим \r\n            стабильную и бесперебойную работу ваших ресурсов, \r\n            чтобы они приносили прибыль.\r\n            Стоимость работ от 2 070 до 2 860 рублей/час.', 1, '2020-08-21 03:55:41', '2020-08-21 03:55:41'),
	(6, 'AI И ML', 'AI И ML. РОБОТЫ ВАС НЕ ПОРАБОТЯТ, ЕСЛИ ВЫ \r\n            ПРОЯВИТЕ К НИМ НЕМНОГО УВАЖЕНИЯ.\r\n            Если вам приходится выполнять однотипные \r\n            задания раз за разом, значит, вы теряете \r\n            свое время и преимущество. Алгоритмы сделают \r\n            повседневную работу за вас. AI не спит, не \r\n            теряет концентрации, не ошибается (ну почти). \r\n            Автоматизация, умное планирование, общение с \r\n            клиентами, гибкое ценообразование, \r\n            умный поиск — все это может и должно быть \r\n            выведено на новый, современный уровень.', 1, '2020-08-21 03:56:01', '2020-08-21 03:56:01'),
	(7, 'Документы и право', 'ДОКУМЕНТЫ И ПРАВО\r\n            Мы не только прекрасно разрабатываем, \r\n            но и отлично пишем. В команде работают \r\n            эксперты по разаботке технических заданий, \r\n            подготовке методических рекомендаций, \r\n            созданию грамотных договоров. С нами \r\n            юридические услуги становятся проще и доступнее, \r\n            а техническая документация — понятнее.', 1, '2020-08-21 03:56:19', '2020-08-21 03:56:20');
/*!40000 ALTER TABLE `CompanyDescription` ENABLE KEYS */;

-- Dumping structure for table bot.Telegram_Admin
DROP TABLE IF EXISTS `Telegram_Admin`;
CREATE TABLE IF NOT EXISTS `Telegram_Admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `telegramID` int(11) NOT NULL,
  `password` text NOT NULL,
  `get_messages` int(11) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table bot.Telegram_Admin: ~0 rows (approximately)
DELETE FROM `Telegram_Admin`;
/*!40000 ALTER TABLE `Telegram_Admin` DISABLE KEYS */;
/*!40000 ALTER TABLE `Telegram_Admin` ENABLE KEYS */;

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Dumping data for table bot.Telegram_Messages: ~1 rows (approximately)
DELETE FROM `Telegram_Messages`;
/*!40000 ALTER TABLE `Telegram_Messages` DISABLE KEYS */;
INSERT INTO `Telegram_Messages` (`id`, `telegramID`, `recipient`, `message`, `messageID`, `created_on`, `updated_on`) VALUES
	(1, 932670856, 1266890760, '/start', 1690, '2020-08-21 00:51:35', '2020-08-21 00:51:35');
/*!40000 ALTER TABLE `Telegram_Messages` ENABLE KEYS */;

-- Dumping structure for table bot.Telegram_Projects
DROP TABLE IF EXISTS `Telegram_Projects`;
CREATE TABLE IF NOT EXISTS `Telegram_Projects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `telegramID` int(11) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `fio` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `aboutProject` text,
  `document` int(11) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table bot.Telegram_Projects: ~0 rows (approximately)
DELETE FROM `Telegram_Projects`;
/*!40000 ALTER TABLE `Telegram_Projects` DISABLE KEYS */;
/*!40000 ALTER TABLE `Telegram_Projects` ENABLE KEYS */;

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Dumping data for table bot.Telegram_User: ~1 rows (approximately)
DELETE FROM `Telegram_User`;
/*!40000 ALTER TABLE `Telegram_User` DISABLE KEYS */;
INSERT INTO `Telegram_User` (`id`, `telegramID`, `first_name`, `last_name`, `username`, `type`, `create_project`, `bot_command`, `created_on`, `updated_on`) VALUES
	(1, 932670856, 'Sergey', 'Popckov', 'popkovS', 'private', 0, 0, '2020-08-21 00:51:35', '2020-08-21 00:51:35');
/*!40000 ALTER TABLE `Telegram_User` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
