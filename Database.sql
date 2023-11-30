-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.9.2-MariaDB-log - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for kuliner_spk
CREATE DATABASE IF NOT EXISTS `spk_mora` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `spk_mora`;

-- Dumping structure for table kuliner_spk.data_bobot
CREATE TABLE IF NOT EXISTS `data_bobot` (
  `id_bobot` int(35) NOT NULL AUTO_INCREMENT,
  `kode_kriteria` varchar(255) NOT NULL,
  `nama_bobot` varchar(255) NOT NULL,
  `nilai_bobot` double NOT NULL,
  PRIMARY KEY (`id_bobot`),
  KEY `kode_kriteria` (`kode_kriteria`),
  CONSTRAINT `FK_data_bobot_data_kriteria` FOREIGN KEY (`kode_kriteria`) REFERENCES `data_kriteria` (`id_kriteria`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

-- Dumping data for table kuliner_spk.data_bobot: ~23 rows (approximately)
/*!40000 ALTER TABLE `data_bobot` DISABLE KEYS */;
INSERT INTO `data_bobot` (`id_bobot`, `kode_kriteria`, `nama_bobot`, `nilai_bobot`) VALUES
	(1, 'C1', 'X<5', 1),
	(2, 'C1', '5<X>10', 2),
	(3, 'C1', '10<X>15', 3),
	(4, 'C1', '15<X>20', 4),
	(5, 'C1', 'X>20', 5),
	(6, 'C2', 'X<1', 1),
	(7, 'C2', '1<X>3', 2),
	(8, 'C2', '3<X>5', 3),
	(9, 'C2', '5<X>7', 4),
	(10, 'C2', 'X>7', 5),
	(11, 'C3', 'X<Rp.20.000,00', 3),
	(12, 'C3', 'Rp.20.000,00<X>Rp.30.000,00', 2),
	(13, 'C3', 'X>Rp.30.000,00', 1),
	(14, 'C4', 'X<4', 1),
	(15, 'C4', '4<X>8', 2),
	(16, 'C4', '8<X>12', 3),
	(17, 'C4', '12<X>16', 4),
	(18, 'C4', 'X>16', 5),
	(19, 'C5', 'X<1', 5),
	(20, 'C5', '1<X>3', 4),
	(21, 'C5', '3<X>5', 3),
	(22, 'C5', '5<X>7', 2),
	(23, 'C5', 'X>7', 1);
/*!40000 ALTER TABLE `data_bobot` ENABLE KEYS */;

-- Dumping structure for table kuliner_spk.data_kriteria
CREATE TABLE IF NOT EXISTS `data_kriteria` (
  `id_kriteria` varchar(255) NOT NULL DEFAULT 'AUTO_INCREMENT',
  `nama_kriteria` varchar(255) NOT NULL,
  `nilai_krieria` double NOT NULL,
  `tipe_kriteria` enum('B','C') DEFAULT NULL,
  PRIMARY KEY (`id_kriteria`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table kuliner_spk.data_kriteria: ~5 rows (approximately)
/*!40000 ALTER TABLE `data_kriteria` DISABLE KEYS */;
INSERT INTO `data_kriteria` (`id_kriteria`, `nama_kriteria`, `nilai_krieria`, `tipe_kriteria`) VALUES
	('C1', 'Varian Menu', 0.2, 'B'),
	('C2', 'Fasilitas', 0.25, 'B'),
	('C3', 'Harga', 0.3, 'C'),
	('C4', 'Waktu Operasional', 0.15, 'B'),
	('C5', 'Lokasi', 0.1, 'C');
/*!40000 ALTER TABLE `data_kriteria` ENABLE KEYS */;

-- Dumping structure for table kuliner_spk.data_kuliner
CREATE TABLE IF NOT EXISTS `data_kuliner` (
  `id_kuliner` int(35) NOT NULL AUTO_INCREMENT,
  `nama_usaha` varchar(255) NOT NULL,
  PRIMARY KEY (`id_kuliner`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Dumping data for table kuliner_spk.data_kuliner: ~3 rows (approximately)
/*!40000 ALTER TABLE `data_kuliner` DISABLE KEYS */;
INSERT INTO `data_kuliner` (`id_kuliner`, `nama_usaha`) VALUES
	(1, 'Sate Kambing Pak Manto'),
	(2, 'Tahu Kupat Sido Mampir'),
	(3, 'Mie Kemruyuk');
/*!40000 ALTER TABLE `data_kuliner` ENABLE KEYS */;

-- Dumping structure for table kuliner_spk.jenis_usaha
CREATE TABLE IF NOT EXISTS `jenis_usaha` (
  `id_usaha` int(35) NOT NULL AUTO_INCREMENT,
  `nama_jenis` varchar(255) NOT NULL,
  PRIMARY KEY (`id_usaha`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Dumping data for table kuliner_spk.jenis_usaha: ~3 rows (approximately)
/*!40000 ALTER TABLE `jenis_usaha` DISABLE KEYS */;
INSERT INTO `jenis_usaha` (`id_usaha`, `nama_jenis`) VALUES
	(1, 'Sate'),
	(2, 'Tahu Kupat'),
	(3, 'Mie Goreng');
/*!40000 ALTER TABLE `jenis_usaha` ENABLE KEYS */;

-- Dumping structure for table kuliner_spk.konversi_penilaian
CREATE TABLE IF NOT EXISTS `konversi_penilaian` (
  `id_konversi` int(35) NOT NULL AUTO_INCREMENT,
  `nama_usaha` varchar(255) NOT NULL DEFAULT '',
  `C1` int(35) NOT NULL,
  `C2` int(35) NOT NULL,
  `C3` int(35) NOT NULL,
  `C4` int(35) NOT NULL,
  `C5` int(35) NOT NULL,
  PRIMARY KEY (`id_konversi`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Dumping data for table kuliner_spk.konversi_penilaian: ~3 rows (approximately)
/*!40000 ALTER TABLE `konversi_penilaian` DISABLE KEYS */;
INSERT INTO `konversi_penilaian` (`id_konversi`, `nama_usaha`, `C1`, `C2`, `C3`, `C4`, `C5`) VALUES
	(1, 'Sate Kambing Pak Manto', 4, 4, 1, 4, 4),
	(2, 'Tahu Kupat Sido Mampir', 1, 3, 3, 4, 4),
	(3, 'Mie Kemruyuk', 5, 5, 2, 4, 4);
/*!40000 ALTER TABLE `konversi_penilaian` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
