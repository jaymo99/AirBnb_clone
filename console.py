#!/usr/bin/python3
'''HBNB command interprester module'''

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    '''entry point for the command interpreter'''
    prompt = "(hbnb) "

    __classes = {
            "BaseModel": BaseModel
            }
    __err_msgs = {
            "cls_missing": "** class name missing **",
            "cls_unexist": "** class doesn't exist**",
            "id_missing": "** instance id missing **",
            "id_unexist": "** no instance found **"
            }

    def emptyline(self):
        '''ignore empty lines'''
        pass

    def do_EOF(self, line):
        '''a clean way to exit the command interpreter'''
        return True

    def do_quit(self, line):
        '''a clean way to exit the command interpreter'''
        return True

    def do_create(self, line):
        '''creates a new instance of <BaseModel> and
        prints the id
        '''
        if not line:
            print(HBNBCommand.__err_msgs["cls_missing"])
        elif line[0] not in HBNBCommand.__classes:
            print(HBNBCommand.__err_msgs["cls_unexist"])

    def do_show(self, line):
        '''prints the string representation of an instance
        based on the class name and id
        '''
        obj_dict = storage.all()
        if not line:
            print(HBNBCommand.__err_msgs["cls_missing"])

        line = line.split()
        if line[0] not in HBNBCommand.__classes:
            print(line[0])
            print(HBNBCommand.__err_msgs["cls_unexist"])
        elif len(line) < 2:
            print(HBNBCommand.__err_msgs["id_missing"])
        elif f"{line[0]}.{line[1]}" not in obj_dict:
            print(HBNBCommand.__err_msgs["id_unexist"])
        else:
            obj_str = obj_dict["{}.{}".format(line[0], line[1])]
            new_obj = HBNBCommand.__classes[line[0]](obj_str)
            print(new_obj)

    def help_show(self):
        print("\n".join(["Usage: show <class_name> <id>",
                        "prints the string representation of an instance\
                        based on the class-name and id"
                         ]
                        ))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
