FROM python:3.8-slim

RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt

EXPOSE 8080
ENTRYPOINT ["sh", "start.sh"]