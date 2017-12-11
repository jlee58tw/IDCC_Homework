#!/bin/bash
cd /home/user
. venv/bin/activate
cd /home/user/test
python autotest.py
cd /home/user/web
python manage.py send_queued_messages --limit=10
