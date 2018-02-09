from cmdmgr import CmdMgr
import basiccmd as bcmd
import bridgescoringcmd as bscmd

program = CmdMgr(dict(bcmd.cmd_dict , ** bscmd.cmd_dict))
program.run()
