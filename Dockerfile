FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN apt-get update && apt-get install -y gdal-bin
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt
