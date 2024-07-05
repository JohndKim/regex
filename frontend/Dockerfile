FROM node:18-alpine

WORKDIR /frontend

COPY package*.json ./

RUN npm install

RUN npm i -g serve

COPY . .

EXPOSE 3000

CMD [ "serve", "-s", "dist" ]