from command_list import command_list
from helpers.rich import printr

def dos_help(arguments):
    printr("<blue>MH DOS Commands<end>")
    for command in command_list.keys():
        printr(f"<blue>{command}<end>-{command_list[command][1]}")
