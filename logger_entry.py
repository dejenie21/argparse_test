'''
Created on Apr 19, 2023

@author: simonray
'''

import sys
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

import os
from pathlib import Path

from datetime import datetime
import hashlib
import logging

def parseArgs():
    
    try:
        # Setup argument parser
        parser = ArgumentParser(description="parse test", formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument("-y", "--yaml_file", dest="yamlfile", action="store", help="yaml file name [default: %(default)s]")

        global yamlFile

        # Process arguments
        args = parser.parse_args()        
        yamlFile = args.yamlfile
        
    except Exception as e:
        print(e)
        return 2    




def initLogger(md5string):

    ''' setup log file based on project name'''
    logfileBasename = ""

    logfileBasename = Path(yamlFile).stem

    now = datetime.now()
    dt_string = now.strftime("%Y%m%d_%H%M%S")
    logFolder = os.path.join(os.getcwd(), "logfiles")
    if not os.path.exists(logFolder):
        print("--log folder <" + logFolder + "> doesn't exist, creating")
        os.makedirs(logFolder)
    logfileName = os.path.join(logFolder, logfileBasename + "__" + dt_string + "__" + md5string +".log")
    handler = logging.StreamHandler(sys.stdout)
    logging.basicConfig(level=logging.DEBUG)

    fileh = logging.FileHandler(logfileName, 'a')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileh.setFormatter(formatter)

    log = logging.getLogger()  # root logger
    log.setLevel(logging.DEBUG)
    for hdlr in log.handlers[:]:  # remove all old handlers
        log.removeHandler(hdlr)
    log.addHandler(fileh)      # set the new handler
    log.addHandler(handler)
    logging.info("+" + "*"*78 + "+")
    logging.info("project log file is <" + logfileName + ">")
    logging.info("+" + "*"*78 + "+")
    logging.debug("debug mode is on")





def main(argv=None):


    if argv is None:
        argv = sys.argv


    parseArgs(argv)
    
    print("the yaml file was set to <" + yamlFile + ">")



if __name__ == '__main__':

    sys.exit(main())