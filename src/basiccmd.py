class Help():
    def exe(self):
        print "The program supports the following commands:"
        print "--------------------------------------------"
        print "Delete: Delete a match from database"
        print "Exit  : Exit program"
        print "Help  : List commands and usage"
        print "List  : List all matches in database"
        print "Print : Print the scoring of the current match"
        print "Read  : Read a file to database (becomes current match)"
        print "Stats : Print the total score of current match"
        print "Switch: Change current match to a match in database"
        print "Write : Write the scoring table to a file"
        return False
class Exit():
    def exe(self):
        return True
cmd_dict = {
"help" : Help(),
"exit" : Exit(),
}
