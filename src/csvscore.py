import os.path
from bridgematchrecord import BridgeMatchRec as BMRec

class CsvScoreKeeper:
    def run(self):
        print "Bridge Score Calculator - CSV Version"
        print "-------------------------------------"
        filename = raw_input("Enter CSV File Name :")
        while True:
            if not os.path.isfile(filename):
                print "ERROR: File Does Not Exist!"
                print
                filename = raw_input("Enter CSV File Name :")
                continue
            match = BMRec(filename)
            if match.done :
                print
                print "Match Score Table:"
                match.printRecord()
                match.printTotal()
                break
        print
        print "Code By Ou,Han-Mo  2018"
        print "All Rights Reserved"
