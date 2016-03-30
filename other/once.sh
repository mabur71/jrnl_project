#!/bin/bash
./create_db.sh
/home/operators/journal-project/jrnl/manage.py makemigrations
/home/operators/journal-project/jrnl/manage.py migrate
 
