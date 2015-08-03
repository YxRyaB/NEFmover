__author__ = 'yxryab'
import sys
import re
import os
import optparse
import logging
from time import gmtime, strftime

def main():
    logging.info('Create a list of directories and files')
    dirlist = check_dir(targetdir)
    logging.debug('%s' % [dir for dir in dirlist])
    logging.info('                                          ...[OK]')
    logging.info('Create NEF directory')
    create_dir(dirlist)
    logging.info('                                          ...[OK]')
    logging.info('Move NEF files')
    mv_NEF(dirlist)
    logging.info('                                          ...[OK]')

def mv_NEF(dirlist):
    for dir in dirlist:
        for neffi in dir['neffi']:
            if os.path.isfile(dir['Path'] + os.sep + 'NEF' + os.sep + neffi):
                if not os.path.isfile(dir['Path'] + os.sep + 'NEF' + os.sep + prefix + '_' + neffi):
                    logging.info('File ' + neffi + ' is exist, rename to: ' + prefix + '_' + neffi)
                    os.rename(dir['Path'] + os.sep + neffi, dir['Path'] + os.sep + 'NEF' + os.sep + prefix + '_' + neffi)
                else:
                    logging.info('File ' + neffi + ' is exist, rename to: ' + prefix + '_' + (strftime("%Y-%m-%d %H:%M", gmtime()) + '_' + neffi))
                    os.rename(dir['Path'] + os.sep + neffi, dir['Path'] + os.sep + 'NEF' + os.sep + prefix + '_' + (strftime("%Y-%m-%d %H:%M", gmtime()) + '_' + neffi))
            else:
                os.rename(dir['Path'] + os.sep + neffi, dir['Path'] + os.sep + 'NEF' + os.sep + neffi)

def create_dir(dirlist):
    for dir in dirlist:
        if not os.path.isdir(dir['Path'] + os.sep + 'NEF'):
            os.mkdir(dir['Path'] + os.sep + 'NEF')
        else:
            logging.debug(dir['Path'] + os.sep + 'NEF is exist')

def check_dir(targetdir):
    hidenrege = re.compile('^\..*')
    nefpattern = re.compile('.*\.NEF$')
    nefdirlist = []
    for dirNames, subdirs, filenames in os.walk(targetdir):
        subdirs[:] = [dirs for dirs in subdirs if dirs not in hidenrege.findall(dirs)]
        filenames[:] = [filenamessname for filenamessname in filenames if filenamessname not in hidenrege.findall(filenamessname)]
        count = 0
        files = []
        for fi in filenames:
            if nefpattern.match(fi):
                files.append(fi)
                count += 1

        if count >= 1 \
            and not 'NEF' == os.path.basename(dirNames):
            data = []
            data = {
                "Path": dirNames,
                "neffi": files,
            }
            nefdirlist.append(data)
    return nefdirlist

if __name__ == "__main__":
    parser = optparse.OptionParser("usage: %prog [options] arg1 ...")
    parser.add_option("-d", "--dir",
                      dest="path_to_dir",
                      default=os.path.dirname(sys.argv[0]),
                      type="string",
                      help="The directory path to digital negatives (NEF)(default: path to script)")
    parser.add_option("-p", "--prefix",
                      dest="prefix",
                      default=strftime("%Y-%m-%d %H:%M", gmtime()),
                      type="string",
                      help="Prefix applicable to similar files (default : date and time_{ file })")
    (options, args) = parser.parse_args()
    targetdir = options.path_to_dir
    prefix = options.prefix
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S',
                        level=logging.DEBUG,
                        stream=sys.stdout,)
    main()
