class CmdMgr :
    def __init__(self,cd):
        self.prompt = "Enter Command: "
        self.cmd_dict = cd
    def run(self):
        while self.read() == False :
            print
            pass
    def read(self):
        cmd = raw_input(self.prompt)
        cmd = cmd.strip()
        if cmd.lower() in self.cmd_dict :
            return self.cmd_dict[cmd.lower()].exe()
        else :
            print "Incorrect Command"
            return False
