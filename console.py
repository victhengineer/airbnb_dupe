#!/usr/bin/env python3
""" Command-line interpreter to manage applications objects
"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel

CLASSES = {
    'BaseModel': BaseModel
}

class HBNBCommand(cmd.Cmd):
    ''' HBNBCommand - A command-line interpreter to manage objects
    '''
    prompt = '(hbnb) '

    def do_create(self, arg):
        ''' Create a new instance of BaseModel, saves it to JSON file
        & print id
        '''
        args = arg.split()

        if not args:
            print('** class name missing **')
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
        else:
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)

    def do_show(self, arg):
        ''' Print string representation of an instance based on class
        name and id
        '''
        args = arg.split()
        if not args:
            print('** class name missing **')
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f'{args[0]}.{args[1]}'
            all_objs = storage.all()

            if key in all_objs:
                print(all_objs.get(key))
            else:
                print('** no instance found **')

    def do_destroy(self, arg):
        ''' Deletes an instance based on class name and id
        '''
        args = arg.split()
        if not args:
            print('** class name missing **')
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f'{args[0]}.{args[1]}'
            all_objs = storage.all()

            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print('** no instance found **')

    def do_all(self, arg):
        ''' Print string representation of all instances
        based or not on the class name
        '''
        args = arg.split()
        all_objs = storage.all()
        if args:
            if args[0] in CLASSES:
                model_class = CLASSES[args[0]]
                instances = [
                        str(instance) for instance in all_objs.values()
                        if isinstance(instance, model_class)
                        ]
            else:
                print("** class doesn't exist **")
                return
        else:
            instances = [
                    str(instance) for instance in all_objs.values()
                    ]
        print(instances)

    def do_update(self, arg):
        ''' Updates and instance based on class name and id
        by adding or updating attribute
        '''
        args = shlex.split(arg)
        if not args:
            print('** class name missing **')
            return

        class_name = args[0]
        if class_name not in CLASSES:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{class_name}.{args[1]}"
        obj = storage.all().get(key)

        if not obj:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing  **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = self._parse_value(args[3])

        setattr(obj, attr_name, attr_value)
        storage.save()

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

    def _parse_value(self, value):
        ''' Preserve integer and float values and fallback strings
        '''
        if value.isdigit():
            return int(value)
        try:
            return float(value)
        except ValueError:
            return value.strip('"')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
