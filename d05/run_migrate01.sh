#!/bin/sh
DIR="day05_env"

# Caminho para o diretório onde está localizado o arquivo manage.py
PROJECT_DIR="./d05/"

. $DIR/bin/activate

# Nome do aplicativo para o qual você deseja gerar a migração
APP_NAME="ex01"

echo "Criando migração para o aplicativo $APP_NAME"
# Execute o comando makemigrations para criar a migração
python $PROJECT_DIR/manage.py makemigrations $APP_NAME

echo "Aplicando migração para o aplicativo $APP_NAME"
# Execute o comando migrate para aplicar a migração ao banco de dados
python $PROJECT_DIR/manage.py migrate $APP_NAME
