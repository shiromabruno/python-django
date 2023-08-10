# Diretório para a criação do ambiente virtual
VENV_NAME="day05_env"

# Ativar o ambiente virtual
. $VENV_NAME/bin/activate

# Navegar para o diretório do projeto Django
cd d05
# Iniciar o projeto Django (substitua 'projectname' pelo nome do seu projeto)
python manage.py runserver