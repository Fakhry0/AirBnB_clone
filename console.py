#!/usr/bin/python3
"""
Command interpreter for AirBnB clone project.
"""
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """Creates a new instance of the given class."""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        if not arg:
            print([str(value) for value in storage.all().values()])
            return
        class_name = arg.split()[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        print([str(value) for key, value in storage.all().items()
              if key.split('.')[0] == class_name])

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) == 3 and args[2].startswith('{') and args[2].endswith('}'):
            # Update with dictionary representation
            try:
                update_dict = json.loads(args[2])
                instance = storage.all()[key]
                for attr, val in update_dict.items():
                    if attr not in ["id", "created_at", "updated_at"]:
                        setattr(instance, attr, val)
                instance.save()
            except json.JSONDecodeError:
                print("** invalid dictionary syntax **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]

        # Cast attribute value to the correct type
        try:
            if attribute_value[0] == '"':
                attribute_value = attribute_value.strip('"')
            elif '.' in attribute_value:
                attribute_value = float(attribute_value)
            else:
                attribute_value = int(attribute_value)
        except ValueError:
            pass

        instance = storage.all()[key]
        if attribute_name not in ["id", "created_at", "updated_at"]:
            setattr(instance, attribute_name, attribute_value)
            instance.save()

    def default(self, arg):
        """Handle method calls with format <class name>.all(),
        <class name>.count(), <class name>.show(<id>),
        <class name>.destroy(<id>), or <class name>.update(<id>,
        <attribute name>, <attribute value>)"""
        tokens = arg.split('.')
        if len(tokens) == 2:
            class_name, method = tokens
            if method == 'all()':
                if class_name not in globals():
                    print("** class doesn't exist **")
                    return
                print([str(value) for value in storage.all().values()
                      if isinstance(value, globals()[class_name])])
            elif method == 'count()':
                if class_name not in globals():
                    print("** class doesn't exist **")
                    return
                print(len([value for value in storage.all().values()
                      if isinstance(value, globals()[class_name])]))
            elif method.startswith('show(') and method.endswith(')'):
                instance_id = method.strip('show(').strip(')')
                self.do_show(f"{class_name} {instance_id}")
            elif method.startswith('destroy(') and method.endswith(')'):
                instance_id = method.strip('destroy(').strip(')')
                self.do_destroy(f"{class_name} {instance_id}")
            elif method.startswith('update(') and method.endswith(')'):
                args = method.strip('update(').strip(')').split(',')
                if len(args) == 2:
                    self.do_update(f"{class_name} {args[0]} {args[1]}")
                elif len(args) == 3:
                    self.do_update(
                        f"{class_name} {args[0]} {args[1]} {args[2]}")
                elif len(args) == 1 and args[0].startswith('{') and args[0].endswith('}'):
                    self.do_update(
                        f"{class_name} {method.strip('update(').strip(')')} {args[0]}")
                else:
                    print("** invalid syntax **")
            else:
                print("** invalid syntax **")
        else:
            super().default(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
