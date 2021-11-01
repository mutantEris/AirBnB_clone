#!/usr/bin/python3
"""this is, in fact, the console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """command prompt"""
    prompt = "(hbnb)"

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
