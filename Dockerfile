# syntax=docker/dockerfile:1
FROM python:3.9-alpine
WORKDIR /code
ENV DB_PORT=5432
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]