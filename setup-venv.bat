:: Delete any existing virtual environment.
if exist ./venv rmdir /S /Q ./venv

:: Provision fresh venv and enter it.
python3 -m venv venv
./venv/Scripts/activate

:: Upgrade pip, install dependencies and exit venv.
pip install --upgrade pip
pip install -r requirements.txt
deactivate
