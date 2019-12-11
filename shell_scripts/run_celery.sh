#!/bin/sh
cd app
celery -A taskaddresser_tasks.AddresserTask worker

