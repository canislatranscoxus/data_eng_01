/*
This script is used to create the database "company01".
Warning: This script will drop the existing tables.

*/

create database company01;
use company01;


DROP TABLE IF EXISTS `departments`;
CREATE TABLE `departments` (
  `id` 			int 		DEFAULT NULL ,
  `department`  varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `jobs`;
CREATE TABLE `jobs` (
  `id` 			int 		DEFAULT NULL ,
  `job`  		varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `hired_employees`;
CREATE TABLE `hired_employees` (
  `id` 				int 		DEFAULT NULL ,
  `name`  			varchar(50) DEFAULT NULL ,
  `datetime` 		datetime 	DEFAULT NULL,
  `department_id`	int 		DEFAULT NULL ,
  `job_id`			int 		DEFAULT NULL 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
