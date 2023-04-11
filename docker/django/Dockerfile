FROM python:3.8

COPY requirements.txt /tmp/requirements.txt

RUN python -m venv /env \
&& /env/bin/pip install --upgrade pip \
&& /env/bin/pip install --no-cache-dir -r /tmp/requirements.txt

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
ENV DJANGO_SETTINGS_MODULE=breakingbadapi_task.settings

WORKDIR /app

COPY setup.py /app/
COPY src /app/src

COPY ./docker/django/start_local.sh /

RUN python setup.py develop