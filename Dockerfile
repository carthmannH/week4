FROM node:21-bullseye
ENV NODE_ENV=production

WORKDIR /app

RUN npm install --omit-dev

CMD [ "app.py" ]
