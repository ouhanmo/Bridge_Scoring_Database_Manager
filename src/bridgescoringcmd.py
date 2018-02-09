import os.path
from bridgematchrecord import BridgeMatchRec as BMRec

current_match = []
class Read:
    def exe(self):
        filename = raw_input("Enter CSV File Name :")
        filename = filename.strip()
        if not os.path.isfile(filename):
            print "ERROR: File Does Not Exist!"
            return False
        current_match.append(BMRec(filename))
        if not current_match[-1].done:
            current_match.pop()
        else :
            print "Successfully Read File."
        return False

class Print:
    def exe(self):
        if len(current_match) == 0 :
            print "ERROR: Current Match is empty..."
        else :
            print
            current_match[-1].printRecord()
        return False

class Stats:
    def exe(self):
        if len(current_match) == 0 :
            print "ERROR: Current Match is empty..."
        else :
            print
            current_match[-1].printTotal()
        return False

cmd_dict = {
"read" : Read(),
"print" : Print(),
"stats" : Stats(),
}
