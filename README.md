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
- After it finishes, open http://localhost on your browser.
- Enjoy!