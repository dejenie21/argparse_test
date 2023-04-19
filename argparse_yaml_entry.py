'''
Created on Apr 19, 2023

@author: simonray
'''

import sys
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

from datetime import datetime
import hashlib
import yaml


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


def load_yaml():
    print("loading YAML run configuration file <" + yamlFile + ">")

    with open(yamlFile, 'r') as c:
        seedAnalysisSettings = yaml.safe_load(c)

        # Make datetime stamp
        for key, val in seedAnalysisSettings.items():
            print(str(key) + "|" + str(val))
            
        if 'fasta_file' in seedAnalysisSettings   :
            fastaFile = seedAnalysisSettings['fasta_file']
            print("the fasta file was set to <" + fastaFile + ">")
        else:
            print("no fasta file specified")
            sys.exit( 1)
            
            
def main(argv=None):


    if argv is None:
        argv = sys.argv


    parseArgs()
    
    print("the yaml file was set to <" + yamlFile + ">")
    load_yaml()
    
    
    



if __name__ == '__main__':

    sys.exit(main())