#!/usr/bin/python3
'''HBNB command interprester module'''

import cmd
from models import storage
from models.base_model import BaseModel
import shlex


class HBNBCommand(cmd.Cmd):
    '''entry point for the command interpreter'''
    prompt = "(hbnb) "

    __classes = {
            "BaseModel": BaseModel
            }
    __err_msgs = {
            "cls_missing": "** class name missing **",
            "cls_unexist": "** class doesn't exist **",
            "id_missing": "** instance id missing **",
            "id_unexist": "** no instance found **",
            "attr_missing": "** attribute name missing **",
            "val_missing": "** value missing **"
            }

    @classmethod
    def __cast_attribute(self, value):
        '''casts a string value to appropriate data type
        '''
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return str(value)

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
        prints the id.
        '''
        if not line:
            print(HBNBCommand.__err_msgs["cls_missing"])
            return

        line = line.split()
        if line[0] not in HBNBCommand.__classes:
            print(HBNBCommand.__err_msgs["cls_unexist"])
        else:
            new_obj = HBNBCommand.__classes[line[0]]()
            new_obj.save()
            print(new_obj.id)

    def help_create(self):
        '''displays information about the `create` command
        '''
        print("\nUsage: create <class-name>\n"
              "-> Creates a new instance of a class/model\n"
              "   and displays its id\n"
              "\nDocumented class-names:\n"
              "========================")
        for cls in HBNBCommand.__classes:
            print(cls)
        print()

    def do_show(self, line):
        '''prints the string representation of an instance
        based on the class name and id.
        '''
        all_objs = storage.all()
        if not line:
            print(HBNBCommand.__err_msgs["cls_missing"])
            return

        line = line.split()
        if line[0] not in HBNBCommand.__classes:
            print(HBNBCommand.__err_msgs["cls_unexist"])
        elif len(line) < 2:
            print(HBNBCommand.__err_msgs["id_missing"])
        elif f"{line[0]}.{line[1]}" not in all_objs:
            print(HBNBCommand.__err_msgs["id_unexist"])
        else:
            obj_key = "{}.{}".format(line[0], line[1])
            obj = all_objs[obj_key]
            print(obj)

    def help_show(self):
        '''displays information about the `show` command
        '''
        print("\nUsage: show <class-name> <id>\n"
              "-> prints the string representation of an instance\n"
              "   based on the class-name and id\n"
              "\nDocumented class-names:\n"
              "========================")
        for cls in HBNBCommand.__classes:
            print(cls)
        print()

    def do_all(self, line):
        '''prints the string representation of all instances
        based or not on the class name.
        '''
        all_objs = storage.all()

        if not line:
            print([str(obj) for obj in all_objs.values()])
            return

        line = line.split()
        if line[0] not in HBNBCommand.__classes:
            print(HBNBCommand.__err_msgs["cls_unexist"])
        else:
            cls = line[0]
            print([str(obj) for obj in all_objs.values()
                   if obj.__class__.__name__ == cls])

    def help_all(self):
        '''displays information about `all` command
        '''
        print("\nUsage-1: all"
              "\nUsage-2: all <class-name>\n"
              "-> prints string representation of all instances or based\n"
              "   on their class-name.\n"
              "\nDocumented class-names:\n"
              "========================")
        for cls in HBNBCommand.__classes:
            print(cls)
        print()

    def do_update(self, line):
        '''Updates an instance based on the class name and id
        by adding or updating attributes.
        '''
        if not line:
            print(HBNBCommand.__err_msgs["cls_missing"])
            return

        _cls = _id = _att_name = _att_val = all_objs = ''
        line = shlex.split(line)
        len_line = len(line)
        if line[0] not in HBNBCommand.__classes:
            print(HBNBCommand.__err_msgs["cls_unexist"])
            return
        else:
            _cls = line[0]
        
        if len_line < 2:
            print(HBNBCommand.__err_msgs["id_missing"])
            return

        _id = line[1]
        all_objs = storage.all()
        obj_key = f"{_cls}.{_id}"
        if obj_key not in all_objs:
            print(HBNBCommand.__err_msgs["id_unexist"])
            return

        if len_line < 3:
            print(HBNBCommand.__err_msgs["attr_missing"])
            return
        if len_line < 4:
            print(HBNBCommand.__err_msgs["val_missing"])
            return
        _att_name = line[2].replace(" ", "_")
        _att_val = HBNBCommand.__cast_attribute(line[3])

        if _att_name in ["id", "created_at", "updated_at"]:
            print(f"`{_att_name}` value cannot be changed.")
            return
        setattr(all_objs[obj_key], _att_name, _att_val)
        all_objs[obj_key].save()

    def help_update(self):
        '''displays information about the `update` command
        '''
        print("\nUsage: update <class-name> <id> <attribute-name> "
              "\"<attribute value>\"\n"
              "-> updates an instance/model based on the class-name and id\n"
              "   by adding or updating an attribute.\n"
              "-> Only one attribute can be updated at a time.\n"
              "\nDocumented class-names:\n"
              "========================")
        for cls in HBNBCommand.__classes:
            print(cls)
        print()


    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id
        '''
        all_objs = storage.all()

        if not line:
            print(HBNBCommand.__err_msgs["cls_missing"])
            return

        line = line.split()
        if line[0] not in HBNBCommand.__classes:
            print(HBNBCommand.__err_msgs["cls_unexist"])
        elif len(line) < 2:
            print(HBNBCommand.__err_msgs["id_missing"])
        elif f"{line[0]}.{line[1]}" not in all_objs:
            print(HBNBCommand.__err_msgs["id_unexist"])
        elif all_objs.get(f"{line[0]}.{line[1]}", None):
            del all_objs[f"{line[0]}.{line[1]}"]
            storage.save()
        else:
            print(HBNBCommand.__err_msgs["id_unexist"])

    def help_destroy(self):
        '''displays information about the `destroy` command
        '''
        print("\nUsage: destroy <class-name> <id>\n"
              "-> deletes an instance/model based on the class-name and id.\n"
              "\nDocumented class-names:\n"
              "========================")
        for cls in HBNBCommand.__classes:
            print(cls)
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
