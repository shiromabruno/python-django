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

# bash my_script.sh
# ./my_script.sh , se der permission denied, rodar: chmod u+x my_script.sh
