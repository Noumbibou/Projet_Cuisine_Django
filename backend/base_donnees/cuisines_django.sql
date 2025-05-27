-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mar. 27 mai 2025 à 14:25
-- Version du serveur : 9.1.0
-- Version de PHP : 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `cuisines_django`
--

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add utilisateur', 6, 'add_utilisateur'),
(22, 'Can change utilisateur', 6, 'change_utilisateur'),
(23, 'Can delete utilisateur', 6, 'delete_utilisateur'),
(24, 'Can view utilisateur', 6, 'view_utilisateur'),
(25, 'Can add cuisines', 7, 'add_cuisines'),
(26, 'Can change cuisines', 7, 'change_cuisines'),
(27, 'Can delete cuisines', 7, 'delete_cuisines'),
(28, 'Can view cuisines', 7, 'view_cuisines'),
(29, 'Can add commande', 8, 'add_commande'),
(30, 'Can change commande', 8, 'change_commande'),
(31, 'Can delete commande', 8, 'delete_commande'),
(32, 'Can view commande', 8, 'view_commande'),
(33, 'Can add plat', 9, 'add_plat'),
(34, 'Can change plat', 9, 'change_plat'),
(35, 'Can delete plat', 9, 'delete_plat'),
(36, 'Can view plat', 9, 'view_plat'),
(37, 'Can add historique', 10, 'add_historique'),
(38, 'Can change historique', 10, 'change_historique'),
(39, 'Can delete historique', 10, 'delete_historique'),
(40, 'Can view historique', 10, 'view_historique'),
(41, 'Can add commande plat', 11, 'add_commandeplat'),
(42, 'Can change commande plat', 11, 'change_commandeplat'),
(43, 'Can delete commande plat', 11, 'delete_commandeplat'),
(44, 'Can view commande plat', 11, 'view_commandeplat'),
(45, 'Can add plat archive', 12, 'add_platarchive'),
(46, 'Can change plat archive', 12, 'change_platarchive'),
(47, 'Can delete plat archive', 12, 'delete_platarchive'),
(48, 'Can view plat archive', 12, 'view_platarchive'),
(49, 'Can add notification', 13, 'add_notification'),
(50, 'Can change notification', 13, 'change_notification'),
(51, 'Can delete notification', 13, 'delete_notification'),
(52, 'Can view notification', 13, 'view_notification');

-- --------------------------------------------------------

--
-- Structure de la table `base_commande`
--

DROP TABLE IF EXISTS `base_commande`;
CREATE TABLE IF NOT EXISTS `base_commande` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date_commande` datetime(6) NOT NULL,
  `prix_total` decimal(10,2) NOT NULL,
  `statut` varchar(20) NOT NULL,
  `utilisateur_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `base_commande_utilisateur_id_b002a652` (`utilisateur_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `base_commande`
--

INSERT INTO `base_commande` (`id`, `date_commande`, `prix_total`, `statut`, `utilisateur_id`) VALUES
(1, '2025-05-26 15:23:26.808771', 145.00, 'en_attente', 2),
(2, '2025-05-27 09:32:23.110588', 119.00, 'en_attente', 2);

-- --------------------------------------------------------

--
-- Structure de la table `base_commandeplat`
--

DROP TABLE IF EXISTS `base_commandeplat`;
CREATE TABLE IF NOT EXISTS `base_commandeplat` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantite` int UNSIGNED NOT NULL,
  `commande_id` bigint NOT NULL,
  `plat_id` bigint DEFAULT NULL,
  `image_plat` varchar(100) DEFAULT NULL,
  `nom_plat` varchar(255) DEFAULT NULL,
  `prix_plat` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `base_commandeplat_commande_id_265820e2` (`commande_id`),
  KEY `base_commandeplat_plat_id_18f9355a` (`plat_id`)
) ;

--
-- Déchargement des données de la table `base_commandeplat`
--

INSERT INTO `base_commandeplat` (`id`, `quantite`, `commande_id`, `plat_id`, `image_plat`, `nom_plat`, `prix_plat`) VALUES
(1, 2, 1, 1, 'plats/tajine.jpg', 'tajine', 45.00),
(2, 1, 1, 5, 'plats/couscous.jpg', 'couscous', 55.00),
(3, 2, 2, 2, 'plats/Croissants.jpg', 'croissant', 2.00),
(4, 1, 2, 3, 'plats/pizza.jpg', 'pizza', 55.00),
(5, 3, 2, 6, 'plats/Pastilla_sucrée.jpg', 'pastella', 20.00);

-- --------------------------------------------------------

--
-- Structure de la table `base_cuisines`
--

DROP TABLE IF EXISTS `base_cuisines`;
CREATE TABLE IF NOT EXISTS `base_cuisines` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `description` longtext,
  `user_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `base_cuisines_name_3f4a1fbb_uniq` (`name`),
  KEY `base_cuisines_user_id_a4164083` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `base_cuisines`
--

INSERT INTO `base_cuisines` (`id`, `name`, `description`, `user_id`) VALUES
(1, 'cuisines marocaines', 'bons plats marocains', NULL),
(2, 'cuisines francaises', 'bons patisseries', NULL),
(3, 'cuisines italiennes ', 'bon pattes', NULL);

-- --------------------------------------------------------

--
-- Structure de la table `base_historique`
--

DROP TABLE IF EXISTS `base_historique`;
CREATE TABLE IF NOT EXISTS `base_historique` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date_action` datetime(6) NOT NULL,
  `type_action` varchar(10) NOT NULL,
  `detail` longtext NOT NULL,
  `id_utilisateur_id` bigint NOT NULL,
  `id_plat_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `base_historique_id_utilisateur_id_953e2cf1` (`id_utilisateur_id`),
  KEY `base_historique_id_plat_id_ffe4f79d` (`id_plat_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `base_notification`
--

DROP TABLE IF EXISTS `base_notification`;
CREATE TABLE IF NOT EXISTS `base_notification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `date_creation` datetime(6) NOT NULL,
  `lu` tinyint(1) NOT NULL,
  `utilisateur_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `base_notification_utilisateur_id_d04c0275` (`utilisateur_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `base_notification`
--

INSERT INTO `base_notification` (`id`, `message`, `date_creation`, `lu`, `utilisateur_id`) VALUES
(1, 'Problème de passer une commande', '2025-05-27 09:50:19.339682', 0, 2);

-- --------------------------------------------------------

--
-- Structure de la table `base_plat`
--

DROP TABLE IF EXISTS `base_plat`;
CREATE TABLE IF NOT EXISTS `base_plat` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nom_plat` varchar(100) NOT NULL,
  `temp_preparation` int NOT NULL,
  `prix` decimal(7,2) NOT NULL,
  `id_cuisine_id` bigint NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `base_plat_id_cuisine_id_80265763` (`id_cuisine_id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `base_plat`
--

INSERT INTO `base_plat` (`id`, `nom_plat`, `temp_preparation`, `prix`, `id_cuisine_id`, `image`) VALUES
(1, 'tajine', 60, 45.00, 1, 'plats/tajine.jpg'),
(2, 'croissant', 45, 2.00, 2, 'plats/Croissants.jpg'),
(3, 'pizza', 90, 55.00, 3, 'plats/pizza.jpg'),
(4, 'spaghetti', 60, 10.00, 3, 'plats/spaghiti.jpg'),
(5, 'couscous', 90, 55.00, 1, 'plats/couscous.jpg'),
(6, 'pastella', 60, 20.00, 1, 'plats/Pastilla_sucrée.jpg'),
(7, 'salade burrata', 30, 5.00, 3, 'plats/salade_burrata.jpg'),
(8, 'escargots', 120, 20.00, 2, 'plats/Escargots.jpg'),
(9, 'Estouffade de boeuf', 100, 30.00, 2, 'plats/Lestouffade_de_bœuf.jpg'),
(10, 'harira', 60, 3.00, 1, 'plats/Moroccan_Harira_.jpg'),
(11, 'lasagne', 90, 20.00, 3, 'plats/Lasagne.jpg'),
(12, 'pommes', 45, 15.00, 2, 'plats/pommeT.jpg'),
(13, 'kabghzal', 60, 15.00, 1, 'plats/kaabghzal_u0ZAKKr.jpg');

-- --------------------------------------------------------

--
-- Structure de la table `base_platarchive`
--

DROP TABLE IF EXISTS `base_platarchive`;
CREATE TABLE IF NOT EXISTS `base_platarchive` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nom_plat` varchar(255) NOT NULL,
  `prix` decimal(8,2) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `temp_preparation` varchar(100) NOT NULL,
  `date_suppression` datetime(6) NOT NULL,
  `id_cuisine_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `base_platarchive_id_cuisine_id_45da2388` (`id_cuisine_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `base_platarchive`
--

INSERT INTO `base_platarchive` (`id`, `nom_plat`, `prix`, `image`, `temp_preparation`, `date_suppression`, `id_cuisine_id`) VALUES
(1, 'kabghzal', 20.00, 'plats/kaabghzal_KmVPbxb.jpg', '60', '2025-05-26 15:40:42.623091', 1),
(2, 'kabghzal', 20.00, 'plats/kaabghzal_1fWXyT2.jpg', '60', '2025-05-26 15:40:53.514733', 1);

-- --------------------------------------------------------

--
-- Structure de la table `base_utilisateur`
--

DROP TABLE IF EXISTS `base_utilisateur`;
CREATE TABLE IF NOT EXISTS `base_utilisateur` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `base_utilisateur`
--

INSERT INTO `base_utilisateur` (`id`, `password`, `last_login`, `email`, `nom`, `prenom`, `is_active`, `date_joined`, `is_staff`, `is_superuser`) VALUES
(1, 'pbkdf2_sha256$1000000$NtgiQcVi0j6dVMFpPAii7g$v72FVsd6IG/hp7LEO3vSYcDnyhX8AdNO5YpY1JJxVEI=', '2025-05-27 12:37:54.350422', 'Chibel55@gmail.com', 'Aliaa', 'Chibel', 1, '2025-05-26 14:50:59.647168', 1, 1),
(2, 'pbkdf2_sha256$1000000$XaBgsFYeyOklHkJUomolaD$vMaETtJeZgeM4ApqrXfp/2qxCF4o5q7HBYvig7bE05Y=', '2025-05-27 09:49:07.458685', 'fomin@gmail.com', 'fomin', 'william', 1, '2025-05-26 15:22:47.531210', 0, 0);

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(6, 'base', 'utilisateur'),
(7, 'base', 'cuisines'),
(8, 'base', 'commande'),
(9, 'base', 'plat'),
(10, 'base', 'historique'),
(11, 'base', 'commandeplat'),
(12, 'base', 'platarchive'),
(13, 'base', 'notification');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-05-26 14:47:33.441740'),
(2, 'base', '0001_initial', '2025-05-26 14:47:33.506667'),
(3, 'admin', '0001_initial', '2025-05-26 14:47:33.627499'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-05-26 14:47:33.631563'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-05-26 14:47:33.636400'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-05-26 14:47:33.692041'),
(7, 'auth', '0001_initial', '2025-05-26 14:47:33.863652'),
(8, 'auth', '0002_alter_permission_name_max_length', '2025-05-26 14:47:33.889252'),
(9, 'auth', '0003_alter_user_email_max_length', '2025-05-26 14:47:33.894578'),
(10, 'auth', '0004_alter_user_username_opts', '2025-05-26 14:47:33.898595'),
(11, 'auth', '0005_alter_user_last_login_null', '2025-05-26 14:47:33.903764'),
(12, 'auth', '0006_require_contenttypes_0002', '2025-05-26 14:47:33.904950'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2025-05-26 14:47:33.908754'),
(14, 'auth', '0008_alter_user_username_max_length', '2025-05-26 14:47:33.913424'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2025-05-26 14:47:33.919267'),
(16, 'auth', '0010_alter_group_name_max_length', '2025-05-26 14:47:33.944308'),
(17, 'auth', '0011_update_proxy_permissions', '2025-05-26 14:47:33.950321'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2025-05-26 14:47:33.954170'),
(19, 'base', '0002_commande_plat_ingredient_historique_commandeplat_and_more', '2025-05-26 14:47:34.366372'),
(20, 'base', '0003_utilisateur_is_staff_utilisateur_is_superuser', '2025-05-26 14:47:34.443809'),
(21, 'base', '0004_remove_cuisines_brand_remove_cuisines_category_and_more', '2025-05-26 14:47:34.659882'),
(22, 'base', '0005_alter_cuisines_name', '2025-05-26 14:47:34.683606'),
(23, 'base', '0006_commandeplat_image_plat_commandeplat_nom_plat_and_more', '2025-05-26 14:47:34.902292'),
(24, 'base', '0007_notification', '2025-05-26 14:47:34.954721'),
(25, 'base', '0008_alter_notification_utilisateur', '2025-05-26 14:47:34.966163'),
(26, 'base', '0009_remove_ingredient_id_plat_and_more', '2025-05-26 14:47:35.067899'),
(27, 'sessions', '0001_initial', '2025-05-26 14:47:35.093348');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('jwwnb914so8yliri52eopxn8bg90fh95', '.eJxVjDsOwjAQRO_iGlmO_0tJnzNYXnuNA8iR4qRC3J1ESgHdaN6bebMQt7WGrdMSpsyubGCX3w5jelI7QH7Edp95mtu6TMgPhZ-083HO9Lqd7t9Bjb3ua29BQlLSOooWSFrjKYEWZPIeBiEKluyTl6CdlgqcQuM0eh1zURIt-3wBzR83Zg:1uJtZ4:WFp9fAYhf-Qns9dphORyRdTIKnQ7u6VbPOTU0vTIMXI', '2025-06-10 12:37:54.356530');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
