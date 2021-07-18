from command_list import command_list
from helpers.rich import printr
import commands.dos_help
import commands.clear

def call(command: str):
    """
    Command caller
    =================
    Calls specific command

    Parameters
    =================
    command (str):
        command name

    """ 
    if command in command_list:
        eval(f"{command_list[command][0]}()")
    else:
        printr("<red>Command not found!<end>")
