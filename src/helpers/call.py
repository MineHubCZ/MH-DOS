from command_list import command_list
from helpers.rich import printr
import commands.dos_help
import commands.clear
import commands.posts.kernel
import commands.exit
import commands.changelog

def call(command: str, arguments: list):
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
        eval(f"{command_list[command][0]}({arguments})")
    else:
        printr("<red>Command not found!<end>")
