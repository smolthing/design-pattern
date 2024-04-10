# Database Migration with Flyway using docker

## Question
Does Flyway 7.15.0 work with MySQL 8?

## Steps to find out
Run MySQL and Flyway with Docker Compose using `image: mysql:8` (default to latest 8.X.X) and `image: mysql:8.0.30` (Specific version).
```
➜ docker-compose up
[+] Running 4/2
 ✔ Network flyway_default                                                                                                                                Created                                                                 0.1s
 ✔ Container flyway-mysql-1                                                                                                                              Created                                                                 0.0s
 ✔ Container flyway-flyway-1                                                                                                                             Created                                                                 0.0s
 ! flyway The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested                                                                         0.0s
Attaching to flyway-1, mysql-1
mysql-1   | 2024-04-10 17:03:01+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.3.0-1.el8 started.
mysql-1   | 2024-04-10 17:03:01+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
mysql-1   | 2024-04-10 17:03:01+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.3.0-1.el8 started.
mysql-1   | 2024-04-10 17:03:02+00:00 [Note] [Entrypoint]: Initializing database files
mysql-1   | 2024-04-10T17:03:02.078662Z 0 [System] [MY-015017] [Server] MySQL Server Initialization - start.
mysql-1   | 2024-04-10T17:03:02.080945Z 0 [System] [MY-013169] [Server] /usr/sbin/mysqld (mysqld 8.3.0) initializing of server in progress as process 81
mysql-1   | 2024-04-10T17:03:02.090163Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
mysql-1   | 2024-04-10T17:03:02.404826Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
mysql-1   | 2024-04-10T17:03:03.321295Z 6 [Warning] [MY-010453] [Server] root@localhost is created with an empty password ! Please consider switching off the --initialize-insecure option.
mysql-1   | 2024-04-10T17:03:05.388946Z 0 [System] [MY-015018] [Server] MySQL Server Initialization - end.
mysql-1   | 2024-04-10 17:03:05+00:00 [Note] [Entrypoint]: Database files initialized
mysql-1   | 2024-04-10 17:03:05+00:00 [Note] [Entrypoint]: Starting temporary server
mysql-1   | 2024-04-10T17:03:05.448586Z 0 [System] [MY-015015] [Server] MySQL Server - start.
mysql-1   | 2024-04-10T17:03:05.793321Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.3.0) starting as process 125
mysql-1   | 2024-04-10T17:03:05.816140Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
mysql-1   | 2024-04-10T17:03:05.999484Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
mysql-1   | 2024-04-10T17:03:06.247196Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
mysql-1   | 2024-04-10T17:03:06.247305Z 0 [System] [MY-013602] [Server] Channel mysql_main configured to support TLS. Encrypted connections are now supported for this channel.
mysql-1   | 2024-04-10T17:03:06.253000Z 0 [Warning] [MY-011810] [Server] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory.
mysql-1   | 2024-04-10T17:03:06.268149Z 0 [System] [MY-011323] [Server] X Plugin ready for connections. Socket: /var/run/mysqld/mysqlx.sock
mysql-1   | 2024-04-10T17:03:06.268166Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.3.0'  socket: '/var/run/mysqld/mysqld.sock'  port: 0  MySQL Community Server - GPL.
mysql-1   | 2024-04-10 17:03:06+00:00 [Note] [Entrypoint]: Temporary server started.
mysql-1   | '/var/lib/mysql/mysql.sock' -> '/var/run/mysqld/mysqld.sock'
mysql-1   | Warning: Unable to load '/usr/share/zoneinfo/iso3166.tab' as time zone. Skipping it.
mysql-1   | Warning: Unable to load '/usr/share/zoneinfo/leap-seconds.list' as time zone. Skipping it.
mysql-1   | Warning: Unable to load '/usr/share/zoneinfo/leapseconds' as time zone. Skipping it.
mysql-1   | Warning: Unable to load '/usr/share/zoneinfo/tzdata.zi' as time zone. Skipping it.
mysql-1   | Warning: Unable to load '/usr/share/zoneinfo/zone.tab' as time zone. Skipping it.
mysql-1   | Warning: Unable to load '/usr/share/zoneinfo/zone1970.tab' as time zone. Skipping it.
mysql-1   | 2024-04-10 17:03:08+00:00 [Note] [Entrypoint]: Creating database service_db
mysql-1   |
mysql-1   | 2024-04-10 17:03:08+00:00 [Note] [Entrypoint]: Stopping temporary server
mysql-1   | 2024-04-10T17:03:08.381843Z 11 [System] [MY-013172] [Server] Received SHUTDOWN from user root. Shutting down mysqld (Version: 8.3.0).
mysql-1   | 2024-04-10T17:03:09.774126Z 0 [System] [MY-010910] [Server] /usr/sbin/mysqld: Shutdown complete (mysqld 8.3.0)  MySQL Community Server - GPL.
mysql-1   | 2024-04-10T17:03:09.774429Z 0 [System] [MY-015016] [Server] MySQL Server - end.
mysql-1   | 2024-04-10 17:03:10+00:00 [Note] [Entrypoint]: Temporary server stopped
mysql-1   |
mysql-1   | 2024-04-10 17:03:10+00:00 [Note] [Entrypoint]: MySQL init process done. Ready for start up.
mysql-1   |
mysql-1   | 2024-04-10T17:03:10.411210Z 0 [System] [MY-015015] [Server] MySQL Server - start.
mysql-1   | 2024-04-10T17:03:10.698620Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.3.0) starting as process 1
mysql-1   | 2024-04-10T17:03:10.707741Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
mysql-1   | 2024-04-10T17:03:10.895223Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
mysql-1   | 2024-04-10T17:03:11.110884Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
mysql-1   | 2024-04-10T17:03:11.110914Z 0 [System] [MY-013602] [Server] Channel mysql_main configured to support TLS. Encrypted connections are now supported for this channel.
mysql-1   | 2024-04-10T17:03:11.112206Z 0 [Warning] [MY-011810] [Server] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory.
mysql-1   | 2024-04-10T17:03:11.124923Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.3.0'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server - GPL.
mysql-1   | 2024-04-10T17:03:11.125116Z 0 [System] [MY-011323] [Server] X Plugin ready for connections. Bind-address: '::' port: 33060, socket: /var/run/mysqld/mysqlx.sock
flyway-1  | Flyway Community Edition 7.15.0 by Redgate
flyway-1  | Database: jdbc:mysql://mysql:3306/service_db (MySQL 8.3)
flyway-1  | WARNING: Flyway upgrade recommended: MySQL 8.3 is newer than this version of Flyway and support has not been tested. The latest supported version of MySQL is 8.0.
flyway-1  | Successfully validated 1 migration (execution time 00:00.074s)
flyway-1  | Creating Schema History table `service_db`.`flyway_schema_history` ...
flyway-1  | Current version of schema `service_db`: << Empty Schema >>
flyway-1  | Migrating schema `service_db` to version "1 - create tables"
flyway-1  | Successfully applied 1 migration to schema `service_db`, now at version v1 (execution time 00:00.153s)
```

Check container.
```
➜ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                 NAMES
75cf7f701060   mysql:8   "docker-entrypoint.s…"   About a minute ago   Up About a minute   3306/tcp, 33060/tcp   flyway-mysql-1             "docker-entrypoint.s…"   4 minutes ago   Up 4 minutes   3306/tcp, 33060/tcp   flyway-mysql-1
```

Check migration status in database.
```
➜ docker exec -it flyway-mysql-1 mysql -u root -proot
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.3.0 MySQL Community Server - GPL

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use service_db;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+-----------------------+
| Tables_in_service_db  |
+-----------------------+
| flyway_schema_history |
| users                 |
+-----------------------+
2 rows in set (0.00 sec)

mysql> select * from flyway_schema_history;
+----------------+---------+---------------+------+-----------------------+-----------+--------------+---------------------+----------------+---------+
| installed_rank | version | description   | type | script                | checksum  | installed_by | installed_on        | execution_time | success |
+----------------+---------+---------------+------+-----------------------+-----------+--------------+---------------------+----------------+---------+
|              1 | 1       | create tables | SQL  | V1__create_tables.sql | -59397695 | root         | 2024-04-10 17:03:14 |             27 |       1 |
+----------------+---------+---------------+------+-----------------------+-----------+--------------+---------------------+----------------+---------+
1 row in set (0.00 sec)

mysql> describe users;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| username | varchar(255) | NO   |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
2 rows in set (0.00 sec)


mysql> SELECT VERSION();
+-----------+
| VERSION() |
+-----------+
| 8.3.0     |
+-----------+
1 row in set (0.01 sec)
```


Remove the container
```
➜ docker-compose down
```


## Conclusion
> Using Flyway V7.15.0, WARNING: Flyway upgrade recommended: MySQL 8.3 is newer than this version of Flyway and support has not been tested. The latest supported version of MySQL is 8.0.

Flyway V7.15.0 only supports up to MySQL 8.0.

> [We have updated Flyway so that it works with ALL supported database versions, so if you upgrade to version 10 you can access all supported versions of MySQL. The community version of Flyway V10 now works with All versions of MySQL.](https://github.com/flyway/flyway/issues/3298#issuecomment-1774661216)

While Flyway V8 dropped support for older MySQL versions like 5.7, Flyway V10.0 (released in Oct 2023) now supports everything. 🎉

## References
https://github.com/flyway/flyway-docker?tab=readme-ov-file

https://hub.docker.com/r/flyway/flyway/tags
