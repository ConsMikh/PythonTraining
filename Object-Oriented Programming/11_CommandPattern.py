'''
The command pattern adds a level of abstraction between actions that must be done and
the object that invokes those actions, normally at a later time. In the command pattern,
client code creates a  Command  object that can be executed at a later date. This object knows
about a receiver object that manages its own internal state when the command is executed
on it. The  Command  object implements a specific interface (typically, it has an  execute  or
do_action  method, and also keeps track of any arguments required to perform the action.
Finally, one or more  Invoker  objects execute the command at the correct time.
'''

import sys

class Document:
    def __init__(self, filename):
        self.filename = filename
        self.contents = "This file cannot be modified"
    def save(self):
        with open(self.filename, "w") as file:
            file.write(self.contents)


class KeyboardShortcut:
    def keypress(self):
        self.command()


class SaveCommand:
    def __init__(self, document):
        self.document = document
    def __call__(self):
        self.document.save()


document = Document("a_file.txt")
shortcut = KeyboardShortcut()
save_command = SaveCommand(document)
shortcut.command = save_command