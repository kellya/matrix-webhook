# Matrix Webhook

Post a message to a matrix room with a simple HTTP POST

This is my own fork of https://github.com/nim65s/matrix-webhook
It adds a yaml configuration with multi-api key endpoints and moves the filtes
to more of a plugin-based system

## Install

For now, clone this repo and run `pip install .`

## Start

Create a matrix user for the bot, and launch this app with the following arguments and/or environment variables
(environment variables update defaults, arguments take precedence):

```
matrix-webhook -h
# OR
python -m matrix_webhook -h
# OR
docker run --rm -it nim65s/matrix-webhook -h
```

```
usage: python -m matrix_webhook [-h] [-H HOST] [-P PORT] [-u MATRIX_URL]
                                [-i MATRIX_ID] [-p MATRIX_PW] [-k API_KEYS]
                                [-c CONFIG] [-v]

Configuration for Matrix Webhook.

options:
  -h, --help            show this help message and exit
  -H HOST, --host HOST  host to listen to. Default: `''`. Environment
                        variable: `HOST`
  -P PORT, --port PORT  port to listed to. Default: 4785. Environment
                        variable: `PORT`
  -u MATRIX_URL, --matrix-url MATRIX_URL
                        matrix homeserver url. Default: `https://matrix.org`.
                        Environment variable: `MATRIX_URL`
  -i MATRIX_ID, --matrix-id MATRIX_ID
                        matrix user-id. Required. Environment variable:
                        `MATRIX_ID`
  -p MATRIX_PW, --matrix-pw MATRIX_PW
                        matrix password. Required. Environment variable:
                        `MATRIX_PW`
  -k API_KEYS, --api-keys API_KEYS
                        comma separated list of shared secrets to use this
                        service. Required. Environment variable: `API_KEYS`
  -c CONFIG, --config CONFIG
                        configuration file. Default: `config.yaml`
  -v, --verbose         increment verbosity level
```


## Dev

```
poetry install
# or python3 -m pip install --user markdown matrix-nio
python3 -m matrix_webhook
```

## Prod

A `docker-compose.yml` is provided:

- Use [Traefik](https://traefik.io/) on the `web` docker network, eg. with
  [proxyta.net](https://framagit.org/oxyta.net/proxyta.net)
- Put the configuration into a `.env` file
- Configure your DNS for `${CHATONS_SERVICE:-matrixwebhook}.${CHATONS_DOMAIN:-localhost}`

```
docker-compose up -d
```

## Test / Usage

```
curl -d '{"body":"new contrib from toto: [44](http://radio.localhost/map/#44)", "key": "secret"}' \
  'http://matrixwebhook.localhost/!DPrUlnwOhBEfYwsDLh:matrix.org'
```
(or localhost:4785 without docker)

### Formatters

These formatters will output custom messages depending on the specific formatter.  Generally to set these up, on the remote provider you would create a webhook with `https://your.webhook.domain/?formatter=<formatter columun below>&api_key=<your apikey>`

| formatter | description                                                                      | key location                                                                             |
| --        | -                                                                                | -                                                                                        |
| github    | for github.com                                                                   | in github JSON webhook settings as `secret`                                              |
| grafana   | for grafana                                                                      | in webhook URL with `api_key=<yourkey>`                                                  |
| pingdom   | for pingdom.com                                                                  | in webhook URL with `api_key=<yourkey>`                                                  |
| buildbot  | buildbot reporter                                                                | in webhook URL with `api_key=<yourkey>` or in master.cfg credentials header as `api_key` |
| generic   | returns raw JSON that was recieved.  For developing additional formatter plugins | in URL with api_key=<yourkey>                                                            |
  
For example, if your matrix-webhook was hosted at https://webhooks.example.com, and you were setting up pingdom and you have an api_key of "123", you would use the following URL for your webhook call from pingdom:
`https://webhooks.example.com/?formatter=pingdom&api_key=123`

### For Gitlab

At a group level, Gitlab does not permit to setup webhooks. A workaround consists to use Google
Chat or Microsoft Teams notification integration with a custom URL (Gitlab does not check if the url begins with the normal url of the service).

#### Google Chat

Add a Google Chat integration with an URL ending with `?formatter=gitlab_gchat&key=API_KEY`

#### Microsoft Teams

Add a Microsoft Teams integration with an URL ending with `?formatter=gitlab_teams&key=API_KEY`

## Test room

[#matrix-webhook:tetaneutral.net](https://matrix.to/#/!DPrUlnwOhBEfYwsDLh:matrix.org)

## Unit tests

```
docker-compose -f test.yml up --exit-code-from tests --force-recreate --build
```
