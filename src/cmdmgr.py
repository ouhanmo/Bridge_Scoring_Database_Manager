class CmdMgr :
    def __init__(self,cd):
        self.prompt = "BSK> "
        self.cmd_dict = cd
    def run(self,func):
        self.start()
        func()
        while self.read() == False :
            print
    def read(self):
        cmd = raw_input(self.prompt)
        cmd = cmd.strip()
        if cmd.lower() in self.cmd_dict :
            print
            return self.cmd_dict[cmd.lower()].exe()
        else :
            print
            print "Incorrect Command"
            return False
    def start(self):
        print "Bridge Scoring Keeper"
        print "Version 2.1"
        print "Enter `Help` For Assistance"
        print "==========================="
