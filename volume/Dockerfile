FROM node:14
EXPOSE 3000
WORKDIR /app
COPY package.json /app/
RUN npm install
COPY . /app/
ARG MY_ARG="LOL"
RUN echo $MY_ARG
CMD [ "node", "main.js" ]