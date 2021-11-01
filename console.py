#!/usr/bin/python3
import cmd
"""this is, in fact, the console"""


class HBNBCommand(cmd.Cmd):
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
