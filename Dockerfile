FROM python:3.8.13-bullseye

RUN rm -rf /etc/localtime
RUN ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN pip3 install --no-cache-dir --upgrade pip

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

WORKDIR /app
