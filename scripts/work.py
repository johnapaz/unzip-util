# This file is not in use and is for future improvements to the scripts.

def execfile(filepath, globals=None, locals=None):
    if globals is None:
        globals = {}
    globals.update({
        "__file__": filepath,
        "__name__": "__main__",
    })
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), globals, locals)

# execute the file
print('Unzipping files...')
execfile("unzip.py")

print('Moving files...')
execfile("move.py")

print('Cleaning up...')
execfile("delete.py")

#try:
#    python /unzip.py &
#    python /move.py &
#    python /delete.py
#    print('All done.')
#
#else:
#    print('Unable to complete work.')

# Version 1 of unzip-util, see https://github.com/johnapaz/unzip-util for details.