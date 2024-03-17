FROM alpine:latest
ENV NODE_ENV=production

WORKDIR /app

CMD ["python", "app.py"]

