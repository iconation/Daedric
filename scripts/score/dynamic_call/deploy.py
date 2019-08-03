import json
import sys

if __name__ == '__main__':
    network = sys.argv[1]
    medianizer = sys.argv[2]

    config_file = "./config/" + network + "/tbears_cli_config.json"
    config = json.loads(open(config_file, "rb").read())

    config["deploy"]["scoreParams"]["medianizer_score"] = medianizer

    print(json.dumps(config))
