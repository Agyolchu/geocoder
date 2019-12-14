#!/bin/sh
cd app
# For testing single worker running or not
celery --app=libs.clients.celery_client worker -E

