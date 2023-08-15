# 0x0D-SQL_introduction


SQL is a fundamental tool for working with databases, whether you're managing small-scale applications or large enterprise systems. Learning SQL empowers you to effectively interact with data, retrieve meaningful insights, and maintain data integrity within your applications 


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Supported Commands](#supported-commands)
- [Execution](#Execution)
- [Requirements](#Requirements)

## Introduction
SQL (Structured Query Language) is a powerful and standardized language used for managing and manipulating relational databases. It provides a way to interact with databases to store, retrieve, update, and delete data. SQL is not specific to any particular database system; rather, it is a common language that can be used with various relational database management systems (RDBMS) such as MySQL, PostgreSQL, SQLite, SQL Server, and Oracle, among others.

Key Concepts of SQL:

Relational Databases: SQL is primarily used for working with relational databases, which store data in tables composed of rows and columns. Each table represents an entity, and rows represent individual records, while columns store specific attributes of those records.

Data Manipulation: SQL allows you to perform various data manipulation operations, including:

SELECT: Retrieving data from one or more tables using queries.
INSERT: Adding new records into tables.
UPDATE: Modifying existing records in tables.
DELETE: Removing records from tables.
Data Definition: SQL handles data definition tasks, including:

CREATE: Creating new database objects like tables, views, indexes, and schemas.
ALTER: Modifying the structure of existing database objects.
DROP: Deleting database objects.
Data Integrity: SQL supports the enforcement of data integrity rules such as primary keys, foreign keys, and constraints to ensure accurate and reliable data.

Query Language: SQL is a declarative language, which means you specify what you want to retrieve or modify, and the database management system handles the details of how to execute the query.

Normalization: SQL databases promote the concept of normalization, which involves organizing data into efficient and structured formats to minimize data redundancy and improve data integrity.

Joins: SQL allows you to combine data from multiple tables using various types of joins, such as INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN.

Aggregation: SQL supports functions like SUM, AVG, COUNT, MIN, and MAX to perform calculations on data sets.

## Features

## Usage


## General

What’s a database
What’s a relational database
What does SQL stand for
What’s MySQL
How to create a database in MySQL
What does DDL and DML stand for
How to CREATE or ALTER a table
How to SELECT data from a table
How to INSERT, UPDATE or DELETE data
What are subqueries
How to use MySQL functions

## Requirements

General
Allowed editors: vi, vim, emacs
All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
All your files should end with a new line
All your SQL queries should have a comment just before (i.e. syntax above)
All your files should start by a comment describing the task
All SQL keywords should be in uppercase (SELECT, WHERE…)
A README.md file, at the root of the folder of the project, is mandatory
The length of your files will be tested using wc

#Comments for your SQL file:

$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

#Install MySQL 8.0 on Ubuntu 20.04 LTS
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
Connect to your MySQL server:

$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
Use “container-on-demand” to run MySQL
In the container, credentials are root/root

Ask for container Ubuntu 20.04
Connect via SSH
OR connect via the Web terminal
In the container, you should start MySQL before playing with it:
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
In the container, credentials are root/root
root@0db97afe3b98:~/0x0D-SQL_introduction# 
