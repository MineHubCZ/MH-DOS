from helpers.call import call
from config import config
from helpers.rich import printr

def run():
    """
    Runner
    =================
    Runs whole dos
    """ 

    config_data = config()
    printr(config_data[1])
    while True:
        try:
            command = input(config_data[0]).split(" ")
            call(command[0], command[1:])
        except KeyboardInterrupt:
            print("")
     
