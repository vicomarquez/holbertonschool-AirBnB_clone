#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, line):
        """exits program"""
        print("")
        exit()

    def emptyline(self):
        """shouldn’t execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
