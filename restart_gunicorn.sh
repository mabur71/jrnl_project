#!/bin/bash
sudo ln -sf /home/`echo $USER`/journal-project/etc/gunicorn.test.conf   /etc/gunicorn.d/test
sudo ln -sf /home/`echo $USER`/journal-project/etc/gunicorn.journal.conf   /etc/gunicorn.d/journal
sudo /etc/init.d/gunicorn restart
