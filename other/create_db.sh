#!/bin/bash
sudo mysql -uroot -e "CREATE DATABASE journal_db CHARACTER SET utf8"
sudo mysql -uroot -e "CREATE USER 'jrnl'@'localhost' IDENTIFIED BY 'jrnl'"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'jrnl'@'localhost'"
sudo mysql -uroot -e "FLUSH PRIVILEGES"

