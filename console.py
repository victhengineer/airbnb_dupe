#!/usr/bin/env python3
""" Command-line interpreter to manage applications objects
"""
import cmd


class HBNBCommand(cmd.Cmd):
    ''' HBNBCommand - A command-line interpreter to manage objects
    '''
    prompt = '(hbnb) '

    def do_quit(self, arg):
        ''' Exits the command-line interpreter: quit
        '''
        return True

    def do_EOF(self, arg):
        ''' Exits the command-line interpreter by handling EOF: Ctrl + D
        '''
        return True

    def emptyline(self):
        ''' Overrides default emptyline behaviour
        '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
