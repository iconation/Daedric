import json
import sys

if __name__ == '__main__':
    network = sys.argv[1]
    value = sys.argv[2]
    score_address_txt = "./config/" + network + "/score_address.txt"

    call = json.loads(open("./calls/post.json", "rb").read())
    call["params"]["to"] = open(score_address_txt, "r").read()

    call["params"]["data"]["params"]["value"] = value

    print(json.dumps(call))
