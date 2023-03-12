#!/usr/bin/python3
"""The entry point of the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """representation of cmd in action"""

    prompt = "(hbnb) "
    def do_quit(self, arg):
        """Quit cammd to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal the exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
