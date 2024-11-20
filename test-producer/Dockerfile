FROM node:16

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

# Exponer el puerto en el que se ejecuta la aplicación (si es necesario)
# No es necesario para Kafka, pero es útil si tu servicio expone algún puerto
# EXPOSE 3000 

CMD ["npm", "start"]
