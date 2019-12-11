#!/bin/sh
cd app
# For testing single worker running or not
celery -A taskaddresser_tasks.AddresserTask worker

