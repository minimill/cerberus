virtualenv --quiet .
source bin/activate
pip install --quiet -r config/requirements.txt
python run.py debug
