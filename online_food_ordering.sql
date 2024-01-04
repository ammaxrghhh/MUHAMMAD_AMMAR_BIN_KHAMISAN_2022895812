-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2024 at 01:39 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `online_food_ordering`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer_order`
--

CREATE TABLE `customer_order` (
  `customer_name` text NOT NULL,
  `phone_number` varchar(12) NOT NULL,
  `Cart` varchar(200) NOT NULL,
  `Total_price` varchar(50) NOT NULL,
  `delivery_location` varchar(300) NOT NULL,
  `delivery_date` varchar(30) NOT NULL,
  `delivery_time_hours` int(3) NOT NULL,
  `delivery_time_minutes` int(3) NOT NULL,
  `additional_notes` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `customer_order`
--

INSERT INTO `customer_order` (`customer_name`, `phone_number`, `Cart`, `Total_price`, `delivery_location`, `delivery_date`, `delivery_time_hours`, `delivery_time_minutes`, `additional_notes`) VALUES
('MUHAMMAD AMMAR BIN KHAMISAN', '0134259876', 'Special Burger, Orange Juice', '', 'lobi kolej malinja', '1/3/24', 11, 10, 'taknak sayur'),
('HANIF AIMAN', '0149307134', 'Special Burger, Lemon Tea, Sprite', '10.0', 'lobi malinja', '1/4/24', 13, 25, 'taknak banyak sos'),
('', '', '', '0', '', '1/3/24', 0, 0, ''),
('', '', '', '0', '', '1/3/24', 0, 0, ''),
('', '', '', '0', '', '1/3/24', 0, 0, ''),
('Samad Haji Ayob', '0129556178', 'Special Burger, Luxury Golden Burger, Sprite', '28.0', 'Pejabat HEP, UiTM Kedah', '1/3/24', 14, 15, 'dah sampai call ya'),
('Hazim Ahmad ', '0175437231', 'King Burger, Orange Juice, Orange Juice', '13.0', 'Foodcourt Mahsuri, UiTM Kedah', '1/4/24', 16, 45, 'nak abang yang hensem yang hantar'),
('KHAIRUL ANUAR', '0143224578', 'King Burger, King Burger, Orange Juice, Orange Juice', '20.0', 'pejabat hep uitm kedah', '1/4/24', 13, 10, '-'),
('KHAIRUL ANUAR', '0143224578', 'King Burger, King Burger, Orange Juice, Orange Juice', '20.0', 'pejabat hep uitm kedah', '1/4/24', 13, 10, '-'),
('AMIR YAHYA', '0132453678', 'Demon Spicy Burger, Lemon Tea', '23.0', 'lobi kolej malinja', '1/4/24', 13, 10, 'tanak sos banyak'),
('FAKHRUL OMAR', '0124458769', 'Special Burger, Coke', '7.0', 'perpustakaan badlishah UITM KEDAH', '1/4/24', 15, 15, '-'),
('FAKHRUL OMAR', '0124458769', 'Special Burger, Coke', '7.0', 'perpustakaan badlishah UITM KEDAH', '1/4/24', 15, 15, '');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
