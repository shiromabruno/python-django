#!/bin/sh

CONTAINER_NAME="postgres-djangotraining"
POSTGRES_USER="djangouser"
POSTGRES_PASSWORD="secret"
POSTGRES_DB="djangotraining"

docker network create d05-network

docker run -d \
  --name "$CONTAINER_NAME" \
  --network d05-network \
  -e POSTGRES_USER="$POSTGRES_USER" \
  -e POSTGRES_PASSWORD="$POSTGRES_PASSWORD" \
  -e POSTGRES_DB="$POSTGRES_DB" \
  -p 5433:5432\
  postgres:latest

echo "PostgreSQL container '$CONTAINER_NAME' criado."

docker run -d \
  --name adminer-container \
  --network d05-network \
  -p 8080:8080 \
  adminer

echo "Adminer container 'adminer-container' criado."
echo "Acesse o Adminer em http://localhost:8080"

echo "Gerando variáveis de ambiente para conexão com o banco de dados..."

SERVER= docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres-djangotraining

DIR="day05_env"

. $DIR/bin/activate

export DB_NAME= POSTGRES_DB
export DB_USER= POSTGRES_USER
export DB_PASSWORD= POSTGRES_PASSWORD
export DB_HOST= SERVER
export DB_PORT="5433"

echo "Variáveis de ambiente geradas com sucesso!"
