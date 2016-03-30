#!/bin/bash
for i in `seq 1 100`;
do
	mysql -uroot -e "INSERT INTO journal_db.records (text,  person, site_id, date) VALUES ('record N$i (797).', 'anonymus$i',  '1', NOW());"
done
for i in `seq 1 100`;
do
	mysql -uroot -e "INSERT INTO journal_db.records (text,  person, site_id, date) VALUES ('record N$i (774).', 'anonymus$i',  '2', NOW());"
done
for i in `seq 1 100`;
do
	mysql -uroot -e "INSERT INTO journal_db.records (text,  person, site_id, date) VALUES ('record N$i.(726)', 'anonymus$i',  '3', NOW());"
done

