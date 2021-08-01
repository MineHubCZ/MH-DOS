from os.path import exists, expanduser, join
import json

def config():

    home = expanduser("~")

    path = join(home, ".mhdosrc")

    if not exists(path):
        f = open(path, "w")
        f.close()

    config = open(path, "r")
    data = config.read()
    config.close()
    
    ps1 = "$ "
    welcome_message = ""

    if not data:
        return [ps1, welcome_message]
    data = json.loads(data)

    ps1 = data["PS1"] if "PS1" in data.keys() else "$"
    welcome_message = data["welcome"] if "welcome" in data.keys() else ""

    return [ps1, welcome_message]
