# Cerberus

Deploy password-protected static websites.

![cerberus](https://work.minimill.co/static/img/favicon-64.png) 

Cerberus is built with [Flask][flask], [Flask-SQLAlchemy][flask-sqlalchemy], [Gulp][gulp], and [SCSS][scss].

## Installation

1. Install node package manager (npm) by going to [nodejs.org][nodejs] and click INSTALL.
2. Install python package manager (pip) by going to [the pip install page](http://pip.readthedocs.org/en/stable/installing/#install-pip) and following the instructions there.

3. Check that `npm` is installed:

    ```bash
    npm -v
    ```

4. Check that `pip` is installed:

    ```bash
    pip -v
    ```

5. Install gulp globally

    ```bash
    npm install -g gulp
    ```

6. Install requirements

    ```bash
    cd cerberus/
    npm install
    gem install sass scss_lint
    pip install virtualenv
    ```

7. Setup secrets file

    ```bash
    cp config/example.secrets.py config/secrets.py
    ```

    Then, edit `config/secrets.py` to contain the appropriate secret keys.

8. Setup the SQLAlchemy database

    ```bash
    python manage.py
    ```

[nodejs]: https://nodejs.org/

## Development

With one Gulp command, you can start the Flask server, and reload SCSS, JS, HTML, images, and fonts with Browserify:

```bash
gulp serve
```

## Gulp

An overview of Gulp commands available:

### `gulp build`

Builds the static parts of the site from the `app/static/src` into the `app/static/dist` directory.  This includes:

- SCSS w/ linting, sourcemaps and autoprefixing
- JS linting and uglification
- Image and font copying

### `gulp build:optimized`

This is used for distributing an optimized version of the site (for deployment).  It includes everything from `gulp build` as well as SCSS minification.

### `gulp watch`

Watchs for changes in local files and rebuilds parts of the site as necessary, into the `app/static/dist` directory.

### `gulp run`

Runs the Flask app in a virtual environment.

### `gulp serve`

Runs `gulp watch` in the background, and runs `gulp run`, proxying it to `localhost:3000` with automatic reloading using [Browsersync][browsersync].

## Structure

```
├── Gulpfile.js             # Controls Gulp, used for building the website
├── README.md               # This file
├── app                     # Root of the Flask application
│   ├── __init__.py         # Init the Flask app using the factory pattern
│   ├── forms.py            # Flask-WTForms forms and validators
│   ├── models.py           # Flask-SQLAlchemy models
│   ├── routes.py           # All URL routes
│   ├── static              # Static files
│   │   ├── dist            # The live static folder
│   │   └── src             # Source static files, will be copied into dist/
│   │       ├── font        # Font files
│   │       ├── img         # Images and SVGs
│   │       ├── js          # JavaScript libraries and scripts
│   │       └── sass        # Stylesheets
│   └── templates           # All Jinja templates / html
├── config                  
│   ├── example.secrets.py  # Example secrets file
│   ├── flask_config.py     # Global Flask config variables
│   ├── requirements.txt    # Python dependencies
│   ├── runserver.sh        # A script used by `gulp run` to run Flask
│   └── secrets.py          # .gitignore'd, file containing your secrets
├── manage.py               # Run this file to recreate the database
├── package.json            # JavaScript dependencies
└── run.py                  # Runs the Flask app.
```

[browsersync]: http://www.browsersync.io/
[gulp]: http://gulpjs.com/
[flask]: http://flask.pocoo.org/
[flask-sqlalchemy]: http://flask-sqlalchemy.pocoo.org/2.0/
[npm-install]: https://nodejs.org/en/download/
[scss]: http://sass-lang.com/
