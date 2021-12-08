import argparse

parser = argparse.ArgumentParser(description='Scan Tool for Internals')
parser.add_argument('-c','--create',help='Create sqlite database')
parser.add_argument('-db','--database', help='Database to be used')
parser.add_argument('-f','--file',help='Import data from an xml file')
parser.add_argument('-d','--directory',help='Import data from a directory with xml files')
parser.add_argument('-os', '--operating-system', help='Indicate our operating system')

args = parser.parse_args()