FROM node:21-bullseye
ENV NODE_ENV=production

WORKDIR /app

CMD [ "app.py" ]
