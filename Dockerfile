FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
RUN apt-get update && apt-get install -y \
    curl  \
 && rm -rf /var/lib/apt/lists/*


WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

ENTRYPOINT ["/code/docker-entrypoint.sh"]