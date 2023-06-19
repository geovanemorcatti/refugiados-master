# AUTHOR: THALLES
# Date: Abril 23rd, 2020
#

FROM python:3.8
ENV PYTHONUNBUFFERED 1
LABEL Name=puc_refugiados Version=1.0
RUN mkdir /code
WORKDIR /code
COPY /django/src/requirements.txt /code/
COPY /django/src/ /code/

ARG DJANGO_SECRET_KEY="-"
ARG DEBUG=0
ENV DJANGO_SECRET_KEY ${DJANGO_SECRET_KEY}
ENV DEBUG ${DEBUG}

#Installs python dependencies
RUN pip install -r requirements.txt

#Installs language pack for pt_BR
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y locales
RUN sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=pt_BR.UTF-8
ENV LANG pt_BR.UTF-8 

RUN chmod +x "bin/start.sh"
ENTRYPOINT ./bin/start.sh