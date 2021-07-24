from commands.posts.show import show
from commands.posts.all import all

def posts(arguments):
    if not arguments:
        all()
        return

    if int(arguments[0]):
        show(arguments[0])
    
