#!/usr/bin/python3
'''HBNB command interprester module'''

import cmd


class HBNBCommand(cmd.Cmd):
    '''entry point for the command interpreter'''
    prompt = "(hbnb) "

    def emptyline(self):
        '''ignore empty lines'''
        pass

    def do_EOF(self, line):
        '''a clean way to exit the command interpreter'''
        return True

    def do_quit(self, line):
        '''a clean way to exit the command interpreter'''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
