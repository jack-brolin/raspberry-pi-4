FROM python:3.7.3
MAINTAINER Strahinja Demic <strahinja.dem@gmail.com>

RUN apt-get update
RUN apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev -y

ADD requirements.txt /
ADD app /app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip

WORKDIR /

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV TZ=Europe/Belgrade
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && dpkg-reconfigure -f noninteractive tzdata
