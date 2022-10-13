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

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, 
        saves it (to the JSON file) and prints the id"""

    def do_show(self, arg):
        """Prints the string representation of an instance 
        based on the class name and id"""

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""

    def do_all(self, arg):
        """Prints all string representation of all instances 
        based or not on the class name."""

    def do_update(self, arg):
        """ Updates an instance based on the class name and 
        id by adding or updating attribute"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()
