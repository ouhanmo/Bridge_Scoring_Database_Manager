import bridgedef as bd
class BridgeScoreMgr :
    def score(self,gameN,contract,penalty,result,declarer) :
        suit = contract[1]
        rank = contract[0]
        vul = bd.getVul(gameN)
        isvul = self.isVul(declarer,vul)
        if(result >= 0) :
            points = self.contract_N_bonus(suit,rank,isvul,penalty) + self.overtricks(suit,result,isvul,penalty)
        else :
            points = -self.penaltypoints(-int(result),isvul,penalty)
        if(declarer == "E" or declarer == "e" or declarer == "W" or declarer == "w"):
            points = -points
        return points
    def contract_N_bonus(self,suit,rank,isvul,penalty):
        #contract points
        if(suit == "N" or suit == "n"):
            contract = 30*int(rank)+10
        if(suit == "S" or suit == "s" or suit == "H" or suit == "h"):
            contract = 30*int(rank)
        if(suit == "D" or suit == "d" or suit == "C" or suit == "c"):
            contract = 20*int(rank)
        if(penalty > 0) :
            contract = 2 * penalty * contract
        #bonus points
        if(contract < 100) :
            bonus = 50
        else :
            if(isvul) :
                bonus = 500
            else :
                bonus = 300
        if(int(rank)==6):
            if(isvul):
                slam = 750
            else :
                slam = 500
        if(int(rank)==7):
            if(isvul):
                slam = 1500
            else :
                slam = 500
        else :
            slam = 0
        return contract + penalty*50 + bonus + slam
    def overtricks(self,suit,result,isvul,penalty):
        if(penalty == 0 ):
            s = bd.suit_dict[suit][0]
            if(s == "N" or s == "H" or s == "S"):
                return 30 * result
            else :
                return 20 * result
        else :
            if(isvul):
                return 200 * result * penalty
            else :
                return 100 * result * penalty
        return 0
    def penaltypoints(self,under,isvul,penalty):
        if(penalty == 0) :
            if(isvul) :
                return under * 100
            else :
                return under * 50
        else :
            if(isvul) :
                return (under * 300 - 100) * penalty
            else :
                if(under < 3) :
                    return (under * 200 - 100) * penalty
                else :
                    return (under * 300 - 400) * penalty
    def isVul(self,dec,vul):
        if(vul == "NONE"):
            return False
        if(vul == "BOTH"):
            return True
        if(vul == "N-S"):
            if(bd.pos_dict[dec] == "North" or bd.pos_dict[dec] == "South"):
                return True
            else :
                return False
        if(vul == "E-W"):
            if(bd.pos_dict[dec] == "East" or bd.pos_dict[dec] == "West"):
                return True
            else :
                return False
