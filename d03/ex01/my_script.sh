# Keep in mind that this script assumes you have a valid Python interpreter (/usr/bin/python3), pip package manager, and Git installed on your system. The script creates a virtual environment, activates it, installs the path package from the specified Git repository, and then runs a small Python program named my_program.py. The virtual environment allows you to have isolated Python environments and avoid conflicts between different projects and their dependencies.


# Set the name of the log file for pip install
LOG_FILE="pip_install.log"

# Set the path to the Python executable (Python 3 in this case)
PYTHON_PATH="/usr/bin/python3"

# Set the URL of the Git repository for the 'path' Python package
PATH_PY_URL="https://github.com/jaraco/path.git"

# Set the name of the my Python program to be executed
MY_PROGRAM="my_program.py"

# Set the name of the virtual environment directory
VENE_DIR="local_lib" # dentro do ex01, ira criar a pasta local_lib

# Create a virtual environment using the specified Python executable
$PYTHON_PATH -m venv $VENE_DIR

# Activate the virtual environment, making it the current Python environment
source $VENE_DIR/bin/activate # aqui tera o activate.csh, activate.fish, arquivos pip3, pip3.8 etc...

# Check the version of pip installed in the virtual environment
python -m pip --version

# Install the 'path' Python package from the specified Git repository.
# The '--log' flag is used to specify the log file for the installation process.
# The '--force-reinstall' flag is used to ensure the package is installed, even if it's already installed.
python -m pip install --log $LOG_FILE --force-reinstall git+$PATH_PY_URL

# Check if the 'path.py' library has been installed properly
if [ -f "$VENE_DIR/lib/python3.*/site-packages/path.py" ]; then
    echo "path.py has been installed successfully. Running my_program.py..."
    python my_program.py
else
    echo "Failed to install path.py."
fi

# bash my_script.sh
# ./my_script.sh , se der permission denied, rodar: chmod u+x my_script.sh
