'''
Created on Apr 19, 2023

@author: simonray
'''

import sys
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter



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



def main(argv=None):


    if argv is None:
        argv = sys.argv


    parseArgs(argv)
    
    print("the yaml file was set to <" + yamlFile + ">")



if __name__ == '__main__':

    sys.exit(main())