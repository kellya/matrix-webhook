"""Configuration for Matrix Webhook."""
import argparse
import os
import sys
import yaml


def get_numeric_log_level(log_level):
    """Return a number that will calculate to the verbosity level"""
    if log_level.lower() == "debug":
        return 4
    elif log_level.lower() == "info":
        return 3
    elif log_level.lower() == "warning":
        return 2
    elif log_level.lower() == "error":
        return 1
    elif log_level.lower() == "critical":
        return 0
    else:
        return 2


parser = argparse.ArgumentParser(description=__doc__, prog="python -m matrix_webhook")
parser.add_argument(
    "-H",
    "--host",
    default=os.environ.get("HOST", ""),
    help="host to listen to. Default: `''`. Environment variable: `HOST`",
)
parser.add_argument(
    "-P",
    "--port",
    type=int,
    default=os.environ.get("PORT", 4785),
    help="port to listed to. Default: 4785. Environment variable: `PORT`",
)
parser.add_argument(
    "-u",
    "--matrix-url",
    default=os.environ.get("MATRIX_URL", "https://matrix.org"),
    help="matrix homeserver url. Default: `https://matrix.org`. "
    "Environment variable: `MATRIX_URL`",
)
parser.add_argument(
    "-i",
    "--matrix-id",
    help="matrix user-id. Required. Environment variable: `MATRIX_ID`",
)
parser.add_argument(
    "-p",
    "--matrix-pw",
    help="matrix password. Required. Environment variable: `MATRIX_PW`",
)
parser.add_argument(
    "-k",
    "--api-keys",
    help="comma separated list of shared secrets to use this service. Required. Environment variable: `API_KEYS`",
)
parser.add_argument(
    "-c",
    "--config",
    help="configuration file. Default: `config.yaml`",
)

parser.add_argument(
    "-v", "--verbose", action="count", default=0, help="increment verbosity level"
)

args = parser.parse_args()

if args.config:
    with open(args.config) as f:
        config = yaml.safe_load(f)
    SERVER_ADDRESS = (config["host"], config["port"])
    MATRIX_URL = config["matrix"]["url"]
    MATRIX_ID = config["matrix"]["id"]
    MATRIX_PW = config["matrix"]["pw"]
    API_KEYS = config["api_keys"].keys()
    ROOM_KEYS = config["api_keys"]
    VERBOSE = get_numeric_log_level(config["log"]["level"])
else:
    SERVER_ADDRESS = (args.host, args.port)
    MATRIX_URL = args.matrix_url
    if not args.matrix_id:
        print("Missing matrix user-id. Use -i or --matrix-id or specify in config.yaml")
        sys.exit(1)
    else:
        MATRIX_ID = args.matrix_id

    if not args.matrix_pw:
        print(
            "Missing matrix password. Use -p or --matrix-pw or specify in config.yaml"
        )
        sys.exit(1)
    else:
        MATRIX_PW = args.matrix_pw

    if not args.api_keys:
        print("Missing api keys. Use -k or --api-keys or specify in config.yaml")
        sys.exit(1)
    else:
        API_KEYS = args.api_keys.split(",")
    VERBOSE = args.verbose
