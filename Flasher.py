"""
Created on Thu Jul  25 13:30:42 2018

@author: mshaik
"""



import os
import subprocess
import argparse




class FlashingBatchFiles(object):
    def __init__(self):
        self.src_IC5000 = ("C:/scala 2/proj1432_ap_dai_src/03_Tools/"
                           "Ultrascale_Flasher_B1_Dual_v4.0")
        self.src_Xilinx = "C:/scala 2/proj1432_ap_dai_src/03_Tools/Xilinx flasher"
        return

    def flash_IC5000(self, srcpath, arguments):
        progstatus = False
        """print("\nWelcome to Ultra-Scale Flashing Automation ...")
        print("\nYou have the following options to flash : ")
        print("\nApplication Flashing  ---->>  select choice type [app]")
        print("\nApplication Flashing  ---->>  select choice type [All]")
        print("\nBootloader Flashing   ---->>  select choice type [boot]")
        print("\nFSBL Flashing         ---->>  select choice type [fsbl]")
        print("\nIdentity Flashing     ---->>  select choice type [Iden]")

        usrin= raw_input("Please select your choice :\n")"""
        for fname in os.listdir(srcpath):
            if fname.endswith('.bat') and arguments in fname:
                os.chdir(srcpath)
                prc = subprocess.Popen(fname)
                prc.communicate()
                if prc.returncode == 0:
                    progstatus = True        
        return progstatus 

    def flash_Xilinx(self, srcpath, arguments):
        progstatus = False
        """print("\nWelcome to Xilinx Flashing Automation ...")
        print("\nYou have the following options to flash : ")
        print("\nApplication Flashing  ---->>  select choice type [app]")
        print("\nBootloader Flashing   ---->>  select choice type [boot]")
        print("\nEverything Flashing   ---->>  select choice type [every]")
        print("\nFSBL Flashing         ---->>  select choice type [fsbl]")
        print("\nIdentity Flashing     ---->>  select choice type [Iden]")

        usrin= raw_input("Please select your choice :\n")"""
        for fname in os.listdir(srcpath):
            if fname.endswith('.bat') and arguments in fname:
                os.chdir(srcpath)
                prc = subprocess.Popen(fname)
                prc.communicate()
                if prc.returncode == 0:
                   progstatus = True        
        return progstatus                

    """  def main1(self):
        curprogstat = False
       ## canoe_filepth=(os.path.join(os.getcwd(), "launch_canoe.bat"))
        print("\nWelcome to the Program Flashing Automation on ECU via JTAG... ")
        print("\nYou have the following options of flashing JTAG :")
        print("\nBy IC5000  ---->>  select choice type [IC5000]")
        print("\nBy Xilinx  ---->>  select choice type [Xilinx]")
        
        usrin = raw_input("\nPlease select your choice:")
        if usrin.startswith('IC5000'):
            curprogstat = self.flash_IC5000(self.src_IC5000)
        elif usrin.startswith('Xilinx'):
            curprogstat = self.flash_Xilinx(self.src_Xilinx)
        """"""if curprogstat:
            prc = subprocess.Popen(canoe_filepth)
            prc.communicate()"""

    def main(self):
        description = "Program Flashing Automation on ECU via JTAG"
        parser = argparse.ArgumentParser(description=description)   
        parser.add_argument("IC5000", action='store',
                            nargs = '?', help='ICdebugger option')
        parser.add_argument("Xilinx",	action='store', nargs = '?', help='Flashing with Xilinx')
        parser.add_argument("-ft","--flashtype", action= 'store',
                            dest='flashtype', default = "",help= 'different flashing option')
        args = parser.parse_args()
        
        if args.IC5000:
            self.flash_IC5000(self.src_IC5000,args.flashtype)
        elif  args.Xilinx:
            self.flash_Xilinx(self.src_Xilinx,args.flashtype)

if __name__ == "__main__":
    FlashingBatchFiles().main() 
   
                


    
