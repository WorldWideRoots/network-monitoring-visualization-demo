# Dockerfile for Node.js API
FROM node:22

WORKDIR /app

COPY package.json package.json
RUN npm install

COPY app.js app.js

CMD ["node", "app.js"]

 