# django_tasks_challenge

By Oscar Castro

## Requirements
Make sure you have docker and docker compose installed, configured and running.

## Setup instructions
- Clone the repository.
- At the root level, create an `.env` file with following variables (Add your own values if you want)
    ```
    SECRET_KEY=your_secret_key
    DEBUG=True
    DJANGO_LOGLEVEL=info
    DB_NAME=tasks_project_db
    DB_USER=dbuser
    DB_PASSWORD=dbpassword
    DB_HOST=db
    DB_PORT=5432
    ```
- If you are using Mac or Linux, run the script `./deploy_n_run.sh`. If using windows, run each of its commands manually.
- Go for a cofee, it can take a while.
- After it finishes, open http://localhost on your browser.
- There won't be any users, so feel free to sign up and log in so you can use the app.
- Profit (?).

## Now What?

- To check the REST API, go to http://localhost/swagger, where you can see (and use) the available endpoints. Just make sure to authenticate using any of the registered users.

- To run the django tests, execute following command on your shell:
    ```
    docker compose run web python manage.py test apps.tasks.tests
    ```

## How it works?
Based on the phylosophy of DRYI (Don't Repeat Yourself Idiot), I tried to use as much as I can all the tools that django already offers, like authentication, class based views, forms, serializers, etc. 

Applying a bit of styling using Tailwind, I managed to create an small yet a complete task management application.
