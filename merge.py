"""
    Simple script for merging all the ExtJS App project files to one
    :author: Petr Vecera <vecera.petr@gmail.com>

"""
from os import path
from os import walk
import argparse
import re


def load_all_files(myPath, extensions, verbose):
    fullPathList = []
    fileList = []
    ignoreFileList = []

    for (dirpath, dirnames, filenames) in walk(path.join(myPath, 'app')):
        for x in filenames:
            if x.lower().endswith(extensions):
                fullPathList.append(path.join(dirpath, x))
                fileList.append(x)
            else:
                ignoreFileList.append(x)

    fullFilesList = []

    for x in fullPathList:
        f = open(x, 'r')
        fullFilesList.append(f.read())
        f.close()

    f = open(path.join(myPath, 'app.js'), 'r')
    fullFilesList.insert(0, f.read())
    f.close()

    if verbose:
        print('Loaded files: ', fullPathList)
        print('Loaded files: ', fileList)
        print('Ignore files: ', ignoreFileList)

    return fullFilesList


def write_to_file(file, loadedFiles, verbose):
    f = open(file, 'w')
    for x in loadedFiles:
        f.write(x)
    f.close()
    if verbose:
        print('Code saved to: ', file)


def remove_comments(files):
    newFiles = []
    for file in files:
        lines = file.splitlines()
        finalString = ""
        for line in lines:
            if not (re.match('^\s\*',
                             line) and '*/' not in line and 'File:' not in line):
                finalString += line + '\n'
        finalString += '\n'
        newFiles.append(finalString)

    return newFiles


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
            description="Merge all Ext App files to one",
            epilog="python merge.py path/to/root/of/my/project")
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        dest='verbose', help="Print additional info")
    parser.add_argument('-nrc', action='store_true', default=True,
                        dest='remove_comments',
                        help="Do not remove SA comments")
    parser.add_argument('-o', '--output', action='store', default='output.js',
                        dest='output',
                        help='Define the output file, output.js is default')
    parser.add_argument('path', nargs=argparse.REMAINDER,
                        help="Path to the root of the project folder")

    # TODO Add extension filter argument
    extensions = '.js'

    args = parser.parse_args()

    if not len(args.path):
        print('Error - you did not specify the path to the project folder')
        exit(1)

    files = load_all_files(args.path[0],extensions, args.verbose)

    if args.remove_comments:
        files = remove_comments(files)

    write_to_file(args.output, files, args.verbose)

    remove_comments(files)
