# Django boilerplate
This is a super simple boilerpalte for starting django projects.

It includes, besides django (obviously):
* A fully dockerized structure, with the webserver running behind nginx
* Whitenoise already configured, and set to be used only in production
* Django compressor com libsass and es6 compressing, already configured
* Env vars already set in the configurations file, plus an .env.example file
* Up-to-date dependencies


## Setup
After cloning the project, replace every 'puc_refugiados' in every file with your project name. **Please note that the project name has to be in lower case, with only letters or '_'**. You also need to replace PROJECT_URL in the settings file with the production url for the project. This doesn't need to be something real until you actually deploy to production.

Also, don't forget to rename the puc_refugiados folder, inside src, to the same name you set in the other puc_refugiados occurencies in the project

Then, after that, you need to create a dev.env file and set a secret key for it. You can cd into the main folder for this project and generate a new secret key by running the generate_secret_key.py script:
```bash
  python generate_secret_key.py
```
The secret key only has to be generated once.


## Running in development
To run in development, simply cd into the main directory and run:
```bash
  docker-compose up
```
Django compressor will automagically compile you SASS and JS files for you while in development, every time you reload the page.



## Further reading
You'll probably need to read more on the packages used in this boilerplate. Here you go:
* [Django 3.1 docs](https://docs.djangoproject.com/en/3.1/)
* [Django Compressor docs](https://django-compressor.readthedocs.io/en/stable/)
* [Whitenoise docs](http://whitenoise.evans.io/en/stable/)
* [Django libsass docs](https://github.com/torchbox/django-libsass)
* [Django Compressor JS docs](https://pypi.org/project/django-compressor-js/)


Have fun!
