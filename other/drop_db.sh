#!/bin/bash
sudo mysql -uroot -e "DROP DATABASE IF EXISTS journal_db;"
sudo mysql -uroot -e "DROP USER jrnl@localhost;"

