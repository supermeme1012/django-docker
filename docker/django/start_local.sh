#!/bin/bash
set -eux
if ! /bin/ls src/breakingbadapi_task.egg-info; then
    echo "Installing breakingbadapi_task in src/breakingbadapi_task.egg-info"
    python setup.py develop
else
    echo "breakingbadapi_task is already installed in src/breakingbadapi_task.egg-info"
fi
django-admin migrate --noinput
django-admin runserver 0.0.0.0:8000
