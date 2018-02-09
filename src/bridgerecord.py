import bridgedef as bd
from bridgescoremgr import BridgeScoreMgr as BSMgr

class BridgeRecord:
    def __init__(self,num,decl,cont,pen,result) :
        self.data = {
        "Number" : num,
        "Declarer" : decl,
        "Contract" : cont,
        "Penalty"  : pen,
        "Result"   : result,
        }
        if(self.data["Contract"] == "AP") :
            self.score = 0
        scoreMgr = BSMgr()
        self.score = scoreMgr.score(self.data["Number"],self.data["Contract"],self.data["Penalty"],self.data["Result"],self.data["Declarer"])
    def __str__(self) :
       rec = "{:>2}".format(str(self.data["Number"]))
       rec = rec + "{:>7}".format(bd.position[(self.data["Number"]-1)%4])
       rec = rec + "{:>6}" .format(bd.getVul(self.data["Number"]))
       rec = rec + "{:>7}".format(bd.pos_dict[self.data["Declarer"]])
       rec = rec + "{:>5}" .format(self.data["Contract"][0]+bd.suit_dict[self.data["Contract"][1]][0])
       rec = rec + "{:^12}".format(bd.penalty[self.data["Penalty"]])
       rec = rec + "{:>+2}".format(self.data["Result"])
       rec = rec + "{:>+8}".format(self.score)
       rec = rec + "{:>+8}".format(-self.score)
       return rec

#record = BridgeRecord(1,"E","2c",0,3)
#record2 = BridgeRecord(2,"E","6S",2,-2)
#record3 = BridgeRecord(3,"E","2S",1,0)
#record4 = BridgeRecord(4,"E","4c",2,-6)
#record5 = BridgeRecord(5,"E","2H",1,3)
#print "N   D  Vul.  Dec  Con. Penalty   R.     N-S "
#print record
#print record2
#print record3
#print record4
#print record5
