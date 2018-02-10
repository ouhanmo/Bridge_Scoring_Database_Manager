import bridgedef as bd
from bridgerecord import BridgeRecord as BRec
import csv
import util as ut
class BridgeMatchRec:
    def __init__(self,filename):
        self.games = []
        self.total = 0
        self.file = filename
        with open(filename) as file:
            dealcount = 0
            reader = csv.reader(file)
            for row in reader:
                dealcount = dealcount+1
                if len(row) !=  4 :
                    print "ERROR: Line %d" % dealcount
                    self.done = False
                    return
                if len(row[1]) < 2:
                    print "ERROR: Line %d" % dealcount
                    self.done = False
                    return
                if not row[0] in bd.pos_dict or not row [1][1] in bd.suit_dict:
                    print "ERROR: Line %d" % dealcount
                    self.done = False
                    return
                if not ut.checkint(row[1][0],7,1):
                    print "ERROR: Line %d" % dealcount
                    self.done = False
                    return
                if not ut.checkint(row[2],2,0) or not ut.checkint(row[3],7-int(row[1][0]),-6-int(row[1][0])):
                    print "ERROR: Line %d" % dealcount
                    self.done = False
                    return
                self.games.append(BRec(dealcount,row[0],row[1],int(row[2]),int(row[3])))
                self.total = self.total + self.games[-1].score
            self.done = True
        file.close()
    def printRecord(self):
        print "No. Deal.  Vul.  Decl.  Con. Penalty   Re.    N-S     E-W"
        print "---------------------------------------------------------"
        for rec in self.games:
            print rec
    def printTotal(self):
        print " Total Score "
        print "-------------"
        print "N-S:   %+d"%self.total
        print "E-W:   %+d"%-self.total
    def write(self,filename):
        with open(filename,"w") as file :
            file.write("No. Deal.  Vul.  Decl.  Con. Penalty   Re.    N-S     E-W\n")
            file.write("---------------------------------------------------------\n")
            for rec in self.games:
                file.write(str(rec)+"\n")
            file.write("\nProgram Output by Hanmo Ou")
        file.close()
