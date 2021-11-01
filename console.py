#!/usr/bin/python3
"""this is, in fact, the console"""
class HBNBCommand(cmd.Cmd):
    """VVVplaceholder, make nothing happen if empty lineVVV"""
    line = self.cmd
    for line in x:
        if not line.strip():
            pass
    if line = quit or line = EOF:
        quit()
    if line = help:
        help()

    if __name__ == '__main__':
            HBNBCommand().cmdloop()
