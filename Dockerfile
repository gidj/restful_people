FROM python:3.7

RUN pip3 install pipenv

WORKDIR /usr/src/app

COPY Pipfile ./
COPY Pipfile.lock ./

RUN set -ex && pipenv install --deploy --system

COPY . .

EXPOSE 8000

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app" ]
