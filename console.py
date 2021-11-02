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
        elif args != "BaseModel":
            print("** class doesn't exist **")
        elif id == "":
            print("** instance id missing **")
        elif id != base.id:
            print("** no instance found **")
        else:
            print(base.id)

    def do_destroy(self, args):
        """Destroys an instance of BaseModel"""
        if != args:
            return print("** class name missing **")
	elif args != "BaseModel":
            print("** class doesn't exist **")
        elif id == "":
            print("** instance id missing **")
        elif id != base.id:
            print("** no instance found **")
        else:
            destroy(base.id)

    def do_quit(self, args):
        """Quits Console"""
        exit()

    def do_all(self, args):
        """This prints all instances of BaseModel"""
        if args != "BaseModel":
            print("** class doesn't exist **")
        else:
            getattr(models, args.split(' ')[0])
            print([str(models.storage.all()[key])
                for key in models.storage.all()
                if key.split('.')[0] == args])

    def emptyline(self):
        """you shall not"""
        pass

    def do_EOF(self, args):
        """Quits Console"""
        exit()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
