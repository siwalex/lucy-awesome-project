# pull official base image
FROM python:3.7-slim

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8080

# install dependencies
RUN pip install --upgrade pip
RUN pip install Flask gunicorn

# copy project
COPY . /app/

CMD python server.py runserver 0.0.0.0:$PORT
