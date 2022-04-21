# Server

The Dockerfile encapsulates the main part of the server. It assumes access to the environment
variables ``PORT` (port on which the server will run), ``SERVICE_ACCOUNT_INFO`` (JSON string of the
Google Cloud service account key for accessing the Google Sheet), ``SPREADSHEET_ID`` (ID of the
Google Sheet) and ``SPREADSHEET_RANGE`` (range of the relevant data in the Google Sheet).

## Local development

To run locally:
1. Get [Docker Compose](https://docs.docker.com/compose/install/)
1. Create an env_secret.dev file with the secret environment variables (everything except ``PORT``)
1. In this directory run `docker-compose up --build`
1. Navigate to `localhost:5000` in a browser

Edits you make to the code should get picked up the next time you refresh the page.

## Deployment

Deployment happens automatically on merges to main via a GitHub Action.
