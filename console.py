#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB clone project."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_help(self, arg):
        """List available commands with "help" or detailed help with "help cmd"."""
        if arg:
            # Get the method for the command if it exists
            cmd_method = getattr(self, 'do_' + arg, None)
            if cmd_method:
                print(cmd_method.__doc__)
            else:
                print(f"No help for '{arg}'")
        else:
            super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
