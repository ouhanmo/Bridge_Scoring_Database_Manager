import os.path
from bridgematchrecord import BridgeMatchRec as BMRec
import util as ut

current_match = [None]
matches = []
filenames = set()

class Init():
    def __init__(self):
        print "Initializing Program..."
        print "Loading File From Previous Work..."
        if not os.path.isfile("data/load.bsk"):
            print "Cannot Find Saved Work..."
            file = open("data/load.bsk","w")
            file.close()
            print "Creating Empty Database..."
        else :
            file = open("data/load.bsk")
            filelist = list(file)
            for filename in filelist :
                filename = filename.rstrip("\n")
                if not os.path.isfile("records/"+filename):
                    print "ERROR: Cannot Find "+ filename
                else :
                    current_match[0] = BMRec(filename)
                    if not current_match[0].done:
                        print "ERROR: Cannot Load "+filename
                    else :
                        filenames.add(filename)
                        matches.append(current_match[0])
                        print "Successfully Read "+filename
                    current_match[0] = None
        print

class Read:
    def exe(self):
        filename = raw_input("Enter CSV File Name :")
        filename = filename.strip()
        if filename in filenames:
            print "ERROR: File Already in Database!"
            return False
        if not os.path.isfile("records/"+filename):
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
                    print "Removed "+ matches[int(num)-1].file + " From Datebase"
                    filenames.remove(matches[int(num)-1].file)
                    del matches[int(num)-1]
                else :
                    print "Removed "+ current_match[0].file + " From Datebase"
                    filenames.remove(current_match[0].file)
                    matches.remove(current_match[0])
                    current_match[0] = None
            else :
                print "ERROR: Incorrect Number..."
            return False

class Save:
    def exe(self):
        file = open("data/load.bsk","w")
        for filename in filenames :
            file.write(filename+"\n")
        print "Progress Saved"
        return False

class Clear :
    def exe(self):
        current_match[0] = None
        del matches[:]
        filenames.clear()
        return False

cmd_dict = {
"read" : Read(),
"print" : Print(),
"stats" : Stats(),
"write" : Write(),
"list" : List(),
"switch" : Switch(),
"delete" : Delete(),
"save" : Save(),
"clear" : Clear(),
}
