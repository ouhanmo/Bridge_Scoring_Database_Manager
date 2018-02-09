class Help():
    def exe(self):
        print "The program supports the following commands:"
        print "--------------------------------------------"
        print "Read: Read a File"
        print "Write: Write the scoring table to a file"
        print "Print: Print the scoring of the current file"
        print "Stats: Print the total score"
        return False
class Exit():
    def exe(self):
        return True
cmd_dict = {
"help" : Help(),
"exit" : Exit(),
}
