# Cerberus

Deploy password-protected static websites.

![cerberus](https://work.minimill.co/static/img/favicon-64.png) 

Cerberus is built with [Flask], [Flask-SQLAlchemy], and [LESS].

## Developing

```bash
virtualenv .
source bin/activate
pip install -r config/requirements.txt
python run.py
```

## Reset the Database

```bash
source bin/activate
python manage.py
```

[LESS]: http://lesscss.org/
[Flask-SQLAlchemy]: http://flask-sqlalchemy.pocoo.org/2.0/
[Flask]: http://flask.pocoo.org/
