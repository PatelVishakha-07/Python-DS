""" C2) The Undo Machine
You're building a lightweight text editor for a startup. Every time a user types a character, it gets recorded When they press Ctrl+Z (Undo) the last action must be reversed. The editor must support.

type(char)-records a character
. undo() removes the last typed character
getText()returns the current text
"""

class TextEditor:

    def __init__(self):
        self.stack = []

    def writeChar(self):
        c = input("enter a charcter: ")
        self.stack.append(c)

    def undo(self):
        self.stack.pop()

    def getText(self):
        return "".join(self.stack)
    
editor = TextEditor()
editor.writeChar()
editor.writeChar()
editor.writeChar()
print("Current text: ",editor.getText())

editor.undo()
editor.writeChar()
print("Current text: ",editor.getText())
