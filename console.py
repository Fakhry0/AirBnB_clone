#!/usr/bin/python3
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
    'BaseModel': BaseModel,
    'User': User,
    'Place': Place,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Review': Review
}


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Destroy an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Print all string representation of all instances based or not on the class name"""
        args = shlex.split(arg)
        if len(args) > 0 and args[0] not in classes:
            print("** class doesn't exist **")
            return
        objects = []
        for obj in storage.all().values():
            if len(args) == 0 or args[0] == obj.__class__.__name__:
                objects.append(str(obj))
        print(objects)

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) == 3:
            print("** attribute name missing **")
            return
        if len(args) == 2:
            print("** value missing **")
            return

        obj = storage.all()[key]

        if len(args) == 4:
            attr_name = args[2]
            attr_value = args[3]

            if attr_name in obj.__class__.__dict__:
                attr_type = type(obj.__class__.__dict__[attr_name])
                setattr(obj, attr_name, attr_type(attr_value))
            else:
                setattr(obj, attr_name, attr_value)

        elif len(args) == 3 and isinstance(eval(args[2]), dict):
            update_dict = eval(args[2])
            for key, value in update_dict.items():
                if key in obj.__class__.__dict__:
                    attr_type = type(obj.__class__.__dict__[key])
                    setattr(obj, key, attr_type(value))
                else:
                    setattr(obj, key, value)

        obj.save()

    def default(self, line):
        """Handle default cases for <class name>.all(), <class name>.count(), etc."""
        args = line.split('.')
        if len(args) != 2:
            print("*** Unknown syntax: {}".format(line))
            return

        class_name, method = args[0], args[1]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if method == "all()":
            self.do_all(class_name)
        elif method == "count()":
            count = sum(1 for obj in storage.all().values()
                        if obj.__class__.__name__ == class_name)
            print(count)
        elif method.startswith("show(") and method.endswith(")"):
            id = method[5:-1].strip('"').strip("'")
            self.do_show(f"{class_name} {id}")
        elif method.startswith("destroy(") and method.endswith(")"):
            id = method[8:-1].strip('"').strip("'")
            self.do_destroy(f"{class_name} {id}")
        elif method.startswith("update(") and method.endswith(")"):
            args = method[7:-1].split(", ")
            if len(args) == 3:
                id = args[0].strip('"').strip("'")
                attr_name = args[1].strip('"').strip("'")
                attr_value = args[2].strip('"').strip("'")
                self.do_update(f"{class_name} {id} {attr_name} {attr_value}")
            elif len(args) == 2:
                id = args[0].strip('"').strip("'")
                dict_repr = eval(args[1])
                if isinstance(dict_repr, dict):
                    for attr_name, attr_value in dict_repr.items():
                        self.do_update(
                            f"{class_name} {id} {attr_name} {attr_value}")
                else:
                    print("** invalid dictionary **")
            else:
                print("** invalid update syntax **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
