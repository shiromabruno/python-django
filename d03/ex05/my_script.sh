# Keep in mind that this script assumes you have a valid Python interpreter (/usr/bin/python3), pip package manager, and Git installed on your system. The script creates a virtual environment, activates it, installs the path package from the specified Git repository, and then runs a small Python program named my_program.py. The virtual environment allows you to have isolated Python environments and avoid conflicts between different projects and their dependencies.

# Set the path to the Python executable (Python 3 in this case)
PYTHON_PATH="/usr/bin/python3"

# Set the name of the virtual environment directory
DIRETORIO_AMBIENTE="django_venv" # dentro do ex04, ira criar a pasta django_venv

# Create a virtual environment using the specified Python executable
$PYTHON_PATH -m venv $DIRETORIO_AMBIENTE

# Activate the virtual environment, making it the current Python environment
source $DIRETORIO_AMBIENTE/bin/activate # aqui tera o activate.csh, activate.fish, arquivos pip3, pip3.8 etc...


# Check the version of pip installed in the virtual environment
python -m pip --version

# Install the 'path' Python package from the specified Git repository.
# The '--log' flag is used to specify the log file for the installation process.
# The '--force-reinstall' flag is used to ensure the package is installed, even if it's already installed.
python -m pip install --force-reinstall -r requirement.txt

echo "requirement.txt instalada com sucesso"

# PASSOS:
# 1- bash my_script.sh
# 2- executar comando: source django_venv/bin/activate
# 3- iniciando um project
#   django-admin startproject Django
# 4- dar um cd Django, e depos inicar um app
#   django-admin startapp helloworld
# 5- Alterar o url.py da pasta ex05/Django/Django path('helloworld/', include('helloworld.url')), + from django.urls.conf import include)
# 6- Criar o url.py da pasta ex05/Django/helloworld (ver abaixo no 6.1)
# 7- Alterar o views.py da pasta ex05/Django/helloworld (ver abaixo o 7.1)
# 8- Entrar no cd Django, Rodar o python3 manage.py runserver
# 9- Vai ter a info Starting development server at http://127.0.0.1:8000/
# 10- Jogar no navegador http://127.0.0.1:8000/helloworld/
# 11- depois do teste, rodar: deactivate

# 6.1) url.py
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.index, name='index'),
# ]

# 7.1)
# from django.shortcuts import render
# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse("Hello World!")

