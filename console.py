#!/usr/bin/python3
"""cmd module to create command line interface"""


import cmd


class HBNBCommand(cmd.Cmd):
    """defining HBNBCommand class"""
    prompt = '(hbnb) '

    def do_EOF(self , args):
        """Exits the program when ctr+D is entered"""
        return True

    #def do_greet(self, args):
    #    print("hello")

    def do_quit(self, args):
        """Quits the program when quit is used as the command"""
        return  True

    def emptyline(self):
        """This is called when an empty line is
        entered.If not overriden, the last non empty command
        entered previously is executed"""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
