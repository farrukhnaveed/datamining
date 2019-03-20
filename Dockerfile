FROM python:2.7

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /datamining
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

#RUN apt-get install memcached
RUN pip install python-memcached
EXPOSE 8000

RUN python manage.py syncdb
#RUN python manage.py migrate

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]