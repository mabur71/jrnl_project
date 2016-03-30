#!/bin/bash
rm -f debug.log
touch debug.log
chmod a=rw debug.log
rm -f gunicorn.access.log
rm -f gunicorn.error.log
rm -f nginx.access.log
rm -f nginx.error.log
