#!/bin/bash
DBNAME=journal_db
DATE=`date +"%Y%m%d"`
SQLFILE=$DBNAME-${DATE}.sql
mysqldump --opt --user=root  $DBNAME > $SQLFILE
gzip -f $SQLFILE
for file in *.sql.gz; do scp "$file" dms26:backup/journal-db && rm "$file" ; done
