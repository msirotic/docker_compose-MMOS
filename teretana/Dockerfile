FROM python:3

ENV PYTHONUNBUFFERED=1
ENV WEBAPP_DIR=/DDGN
RUN pip install --upgrade pip

RUN mkdir -p /var/log/gunicorn

RUN mkdir $WEBAPP_DIR

WORKDIR $WEBAPP_DIR
ADD requirements.txt $WEBAPP_DIR/
RUN pip install -r requirements.txt

ADD . $WEBAPP_DIR/