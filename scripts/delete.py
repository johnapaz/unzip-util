# Replace {folder-name} with the output name from the .zip file generated by Paligo.
import os, glob

try:
    os.rmdir('../{folder-name}/out')
    os.rmdir('../{folder-name}')
    os.remove('../{folder-name}_-Upload_to_GitHub.zip')
    print('Deleted unneeded sub-directories...')
    
except:
   print('[ERROR!] Unable to delete files.')

# Version 1 of unzip-util, see https://github.com/johnapaz/unzip-util for details.