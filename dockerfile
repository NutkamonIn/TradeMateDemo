FROM python:3.11.7
ENV PYTHONUNBUFFERED=1
WORKDIR /TRADE_WEB
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install mysqlclient
RUN pip3 install -r requirements.txt
