import binaryfile
import sys

'''
Created on Jul 14, 2012

@author: jon
'''


def main():
    if len(sys.argv) < 2:
        sys.exit('Usage: %s input-file' % sys.argv[0])

    data = file(sys.argv[1], "rb")

    for message in binaryfile.parse(data):
        print "ITCH message type: " + message[0]

if __name__ == '__main__':
    main()
