import os.path
from bridgematchrecord import BridgeMatchRec as BMRec
import util as ut

def bridgeScoreInit():
    pass

current_match = [None]
matches = []
filenames = set()

class Read:
    def exe(self):
        filename = raw_input("Enter CSV File Name :")
        filename = filename.strip()
        if filename in filenames:
            print "ERROR: File Already in Database!"
            return False
        if not os.path.isfile(filename):
            print "ERROR: File Does Not Exist!"
            return False
        current_match[0] = BMRec(filename)
        if not current_match[0].done:
            current_match[0] = None
        else :
            filenames.add(filename)
            matches.append(current_match[0])
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

class List():
    def exe(self):
        print "Current Matches in Database:"
        print "----------------------------"
        count = 0
        for mat in matches :
            count = count + 1
            print "[{}] ".format(count)+ mat.file
        return False

class Switch():
    def exe(self):
        if len(matches) == 0 :
            print "ERROR: Database is empty..."
            return False
        List().exe()
        print
        while True:
            num = raw_input("Enter Number to Switch to Match (0 to stay):")
            if ut.checkint(num,len(matches),0):
                if int(num) != 0:
                    current_match[0] = matches[int(num)-1]
                    print "Switched to "+current_match[0].file
            else :
                print "ERROR: Incorrect File Number..."
            return False

class Delete():
    def exe(self):
        if len(matches) == 0 :
            print "ERROR: Database is empty..."
            return False
        List().exe()
        print
        while True:
            num = raw_input("Enter Number to Delete (0 to delete current):")
            if ut.checkint(num,len(matches),0):
                if int(num) != 0 and not current_match[0] is matches[int(num)-1] :
                    del matches[int(num)-1]
                else :
                    matches.remove(current_match[0])
                    current_match[0] = None
            else :
                print "ERROR: Incorrect Number..."
            return False

cmd_dict = {
"read" : Read(),
"print" : Print(),
"stats" : Stats(),
"write" : Write(),
"list" : List(),
"switch" : Switch(),
"delete" : Delete(),
}
