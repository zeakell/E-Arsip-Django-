# Dockerfile

# Pull base image
FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /code
WORKDIR /code

# Install dependencies
RUN apt update
RUN apt install -y default-libmysqlclient-dev
RUN apt install -y python3 libapache2-mod-wsgi-py3


RUN pip install pip -U
ADD requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .
COPY  ./arsip /code/