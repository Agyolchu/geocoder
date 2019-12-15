#!/bin/sh
cd app
celery --app=libs.clients.celery_client worker -E

