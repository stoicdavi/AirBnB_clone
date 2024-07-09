#!/usr/bin/python3
from cmd import Cmd

class MyInterpreter(Cmd):
    '''Simple command processor example.'''
    # Introduction text displayed when the interpreter starts
    intro1 = "(hbnb) help\n\nDocumented commands (type help <topic>):\n========================================\nEOF  help  quit\n\n"
    # Full intro including command prompt
    intro = f'{intro1}(hbnb)\n(hbnb)\n(hbnb) quit\n' 
    # Command prompt symbol
    prompt = "$ "

    def do_EOF(self, line):
        '''EOF command to exit the program\n'''
        return True
    
    def do_quit(self, line):
        '''Quit command to exit the program\n'''
        return True
    
    def do_help(self, line):
        '''Help command to display the help\n'''
        print(self.intro1)
    
    def do_echo(self, line):
        '''Echo command to display the input\n'''
        print(line)

if __name__ == "__main__":
    # Create an instance of the interpreter and start the command loop
    interpreter = MyInterpreter()
    interpreter.cmdloop()
