import os.path
from bridgematchrecord import BridgeMatchRec as BMRec

current_match = [None]
class Read:
    def exe(self):
        filename = raw_input("Enter CSV File Name :")
        filename = filename.strip()
        if not os.path.isfile(filename):
            print "ERROR: File Does Not Exist!"
            return False
        current_match[0] = BMRec(filename)
        if not current_match[0].done:
            current_match[0] = None
        else :
            print "File Successfully Read."
        return False

class Print:
    def exe(self):
        if current_match[0] is None :
            print "ERROR: Current Match is empty..."
        else :
            current_match[0].printRecord()
        return False

class Stats:
    def exe(self):
        if current_match[0] is None:
            print "ERROR: Current Match is empty..."
        else :
            current_match[0].printTotal()
        return False

class Write():
    def exe(self):
        if current_match[0] is None:
            print "ERROR: Current Match is empty..."
        else :
            filename = raw_input("Enter Output File Name :")
            filename = filename.strip()
            current_match[0].write(filename)
        return False
cmd_dict = {
"read" : Read(),
"print" : Print(),
"stats" : Stats(),
"write" : Write(),
}
def bridgeScoreInit():
    pass
