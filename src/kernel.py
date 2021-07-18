from helpers.call import call

def run():
    """
    Runner
    =================
    Runs whole dos
    """ 
    while True:
        try:
            command = input("$ ")
            call(command)
        except KeyboardInterrupt:
            print("")
     
