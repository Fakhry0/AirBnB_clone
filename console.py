#!/usr/bin/python3
"""
Command interpreter for AirBnB clone project.
"""
import cmd
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
        args = arg.split(',')
        if len(args) < 2:
            print("** invalid number of arguments **")
            return
        class_name_id = args[0].split()
        if len(class_name_id) != 2:
            print("** invalid syntax **")
            return
        class_name = class_name_id[0]
        instance_id = class_name_id[1]
        key = class_name + '.' + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return

        # Check if the update is with a dictionary
        if '{' in args[1] and '}' in args[1]:
            try:
                update_dict = eval(args[1].strip())
                if not isinstance(update_dict, dict):
                    raise TypeError
            except (SyntaxError, TypeError):
                print("** invalid dictionary syntax **")
                return

            instance = storage.all()[key]
            for attribute, value in update_dict.items():
                setattr(instance, attribute, value)
            instance.save()
        else:  # Update with attribute name and value
            if len(args) < 3:
                print("** invalid number of arguments **")
                return
            attribute_name = args[1].strip()
            attribute_value = args[2].strip()
            instance = storage.all()[key]
            setattr(instance, attribute_name, attribute_value)
            instance.save()

    def default(self, arg):
        """Handle method calls with format<class name>.all(),
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
                if len(args) < 2:
                    print("** invalid syntax **")
                    return
                # Check if updating with dictionary
                if '{' in args[1] and '}' in args[1]:
                    self.do_update(f"{class_name} {args[0]}, {args[1]}")
                else:
                    if len(args) != 3:
                        print("** invalid syntax **")
                        return
                    self.do_update(
                        f"{class_name} {args[0]}, {args[1]}, {args[2]}")
            else:
                print("** invalid syntax **")
        else:
            super().default(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
