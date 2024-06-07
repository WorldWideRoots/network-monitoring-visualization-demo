# Dockerfile for Vue.js Front-End
FROM node:22

WORKDIR /app

COPY package.json package.json
RUN npm install

COPY . .

CMD ["npm", "run", "serve"]
