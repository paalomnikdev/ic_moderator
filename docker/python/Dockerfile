FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN apk add --no-cache mariadb-connector-c-dev gcc python3-dev musl-dev mariadb-dev

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["gunicorn", "-c", "gunicorn.py", "ic_bot.wsgi"]
