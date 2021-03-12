"""
Created on Wed Jul  25 13:30:42 2018

@author: mshaik
"""

import os,sys
import subprocess
import argparse
from processLog import is_in_file

class JtagFlasher(object):
    def __init__(self):
        self.src_IC5000 = "03_Tools\Ultrascale_Flasher_B1_Dual_v4.0"
        self.src_Xilinx = "03_Tools\Xilinx_flasher"

    def flash_IC5000(self, srcpath, arguments):
        progstatus = False
        os.chdir("..")
        os.chdir(srcpath)
        print os.getcwd()
        # srcpath = str(folderName) + '/' + srcpath
        for fname in os.listdir(os.getcwd()):
            if fname.endswith('.bat') and arguments in fname:
                # os.chdir(srcpath)
                prc = subprocess.Popen(fname)
                prc.communicate()
                if prc.returncode == 0:
                    progstatus = True
        if not progstatus:
            print "ERROR: No correct batch file found to proceed flashing process or flashing process failed!"
            sys.exit(1)

    def flash_Xilinx(self, srcpath, arguments):
        progstatus = False
        currentWorkingDir = os.getcwd()
        os.chdir("..")
        os.chdir(srcpath)
        print os.getcwd()
        # srcpath = str(folderName) + '/' + srcpath
        for fname in os.listdir(os.getcwd()):
            if fname.endswith('.bat') and arguments in fname:
                # prc = subprocess.Popen(fname + r' > ..\..\flashLog.log')
                # prc = subprocess.Popen(fname)
                prc = subprocess.Popen(fname + r' > ..\..\flashLog.log',stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
                prc.communicate()

                # while True:
                #     # out = prc.stdout.read(100)
                #     out = prc.stdout.readline()
                #     if out == '' and prc.poll() != None:
                #         break
                #     if out != '':
                #         print "test:", out.rstrip()
                #         sys.stdout.write(out)
                #         sys.stdout.flush()
                #         prc.stdout.xreadlines()
                #         print str(out)

                if prc.returncode == 0:
                    # print prc.returncode, "Here222!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                    progstatus = True
        if not progstatus:
            print "ERROR: No correct batch file was found to proceed flashing process!"
            sys.exit(1)
        # if is_in_file(r'..\..\flashLog.log', 'ERROR'):
        #     print "ERROR: Flashing process failed, Please check the hardware connection!"
        #     sys.exit(1)
        print os.getcwd()
        os.chdir(currentWorkingDir)
        # print os.getcwd(), "Here333!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

    def jtagFlash(self):
        description = "Flashing Automation on ECU via JTAG, example commandline: -fn 182200 -at Xilinx -ft every"
        parser = argparse.ArgumentParser(description=description)
        # parser.add_argument("-fn","--folder name", action='store', dest='folderName', nargs = '?', help=r'The folder name of the software release, for example: 181803 or "D:\_Ye_\Automatic Flash\181803"')
        parser.add_argument("-at","--adapter type", action='store', dest='adapterType', nargs = '?', help='Option for the adapter, for example: IC5000 or Xilinx')
        parser.add_argument("-ft","--flashtype", action='store', dest='flashType', nargs = '?', help= 'Option for flashing, for example: Application Flashing:[app];   Flash everything:[All] for IC5000 and [every] for Xilinx;   Bootloader Flashing:[boot];   FSBL Flashing:[fsbl];   Identity Flashing:[Ident]')

        args = parser.parse_args()

        if args.adapterType == "IC5000":
            self.flash_IC5000(self.src_IC5000, args.flashType)
        elif args.adapterType == "Xilinx":
            self.flash_Xilinx(self.src_Xilinx, args.flashType)
        else:
            print "ERROR: Please check the input arguments like IC5000 or Xilinx! e.g. in cmd: ..\Automatic Flash>python JtagFlasher.py -fn 182200 -at Xilinx -ft every. You can get more help by doing this in cmd: ..\Automatic Flash>python JtagFlasher.py -h"
            sys.exit(1)

if __name__ == "__main__":
    JtagFlasher().jtagFlash()
