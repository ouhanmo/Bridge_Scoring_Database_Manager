class Help():
    def exe(self):
        print "The program supports the following commands:"
        print "--------------------------------------------"
        print "Clear : Clear database (without saving)"
        print "Delete: Delete a match from database"
        print "Exit  : Exit program"
        print "Help  : List commands and usage"
        print "List  : List all matches in database"
        # print "Load  : Load database into program"
        print "Print : Print the scoring of the current match"
        print "Read  : Read a file to database (becomes current match)"
        print "Save  : Save loaded files to program for later use"
        print "Stats : Print the total score of current match"
        print "Switch: Change current match to a match in database"
        print "Write : Write the scoring table to a file"
        return False

class Exit():
    def exe(self):
        print "Program by Hanmo Ou"
        print "NTUEE 2018"
        print "All Rights Reserved"
        return True

cmd_dict = {
"help" : Help(),
"exit" : Exit(),
}
