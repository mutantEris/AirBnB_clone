#!/usr/bin/python3
"""this is, in fact, the console"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """command prompt"""
    prompt = "(hbnb)"

    def do_create(self, args):
        """Creates new instance of BaseModel"""
        if args == "" or None:
            print("** class name missing **")
        elif args != "BaseModel":
            print("** class doesn't exist **")
        else:
            base = BaseModel()
            print(base.id)

    def do_show(self, args):
        """Shows a specific BaseModel instance"""
        if args == "" or None:
            print("** class name missing **")
    def do_quit(self, args):
        """Quits Console"""
        exit()

    def do_EOF(self, args):
        """Quits Console"""
        exit()

    def emptyline(self):
        """you shall not"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
