#!python
'''
List untranslated pages
'''
from __future__ import print_function
from os import walk
import os.path

__all__ = ['untranslated']

def untranslated(path=os.path.curdir, recursive=False):
    '''Returns untranslated pages in path
    '''
    r = []
    for root, dirs, files in walk(path):
        for fil in files:
            if (os.path.splitext(fil)[1]=='.md'
                    and not fil.endswith('_ru.md')
                    and not fil.replace('.md', '_ru.md') in files):
                r.append(os.path.normpath(os.path.join(root, fil)))
        if not recursive:
            break
    return r

if __name__ == '__main__':
    import getopt
    import sys

    def usage():
        shortname = os.path.basename(sys.argv[0])
        print('usage: %s [-h] [-r] [FOLDER]' % shortname)
        print('\nList untranslated *.md pages in current or specified folder')
        print('page.md is treated as untranslated if there is no page_ru.md')
        print('\noptional arguments:')
        print(' -h, --help       Prints help')
        print(' -r, --recursive  Finds pages also in subfolders')

    kwargs={}
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hr', ['help','recursive'])
    except getopt.GetoptError as err:
        print(err, file=sys.stderr)
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            sys.exit()
        elif o in ('-r', '--recursive'):
            kwargs['recursive']=True
        else:
            usage()
            sys.exit(2)
    if len(args)==1:
        kwargs['path']=args[0]
    elif len(args)>1:
        print('Incorrect arguments', file=sys.stderr)
        usage()
        sys.exit(2)

    for fil in untranslated(**kwargs):
        print(fil)
