FROM python:3.8-slim

WORKDIR /app

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 && \
    curl -sL https://cli-assets.heroku.com/install.sh | sh && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install -r requirements.txt

ENV HEROKU_API_KEY=HRKU-1c52e2de-dce6-4e0a-903d-fc41b8883aae

EXPOSE 8080

ENTRYPOINT ["sh", "start.sh"]