#!/usr/bin/python3
"""entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel
from models import storage


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

        input_ = arg.split()

        if len(input_) == 0:
            print("** class name missing **")
        elif input_[0] not in storage.class_dict():
            print("** class doesn't exist **")
        else:
            new = storage.class_dict()[input_[0]]
            new.save()
            print(new.id)


    def do_show(self, arg):
        """Prints the string representation of an instance 
        based on the class name and id"""
        input_ = arg.split()
        dict_ = storage.all()

        if len(input_) == 0:
            print("** class name missing **")
        elif input_[0] not in storage.class_dict():
            print("** class doesn't exist **")
        elif len(input_) == 1:
            print("** instance id missing **")
        else:
            new_key = "{}.{}".format(input_[0], input_[1])
            try:
                print(dict_[new_key])
            except Exception:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        input_ = arg.split()

        if len(input_) == 0:
            print("** class name missing **")
        elif input_[0] not in storage.class_dict():
            print("** class doesn't exist **")
        elif len(input_) == 1:
            print("** instance id missing **")
        else:
            try:
                del storage.all()["{}.{}".format(input_[0], input_[1])]
                storage.save()
            except Exception:
                print("** no instance found **")


    def do_all(self, arg):
        """Prints all string representation of all instances 
        based or not on the class name."""

    def do_update(self, arg):
        """ Updates an instance based on the class name and 
        id by adding or updating attribute"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()
