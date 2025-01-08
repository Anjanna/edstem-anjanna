# small Python base image
FROM python:3.11.6-slim-bullseye

WORKDIR /app

COPY restaurant_api/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY restaurant_api/ /app/restaurant_api

EXPOSE 5000
EXPOSE 5432

ENV FLASK_APP="restaurant_api:create_app"
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
