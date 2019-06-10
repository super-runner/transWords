# process Chinese file:
# python reform.py CHINESE_FILE_PATH  ANYTHING_BUT_en
#
# process English file:
# python reform.py ENGLISH_FILE_PATH  en
#

import os
import sys

FILE_PATH = sys.argv[1]
FILE_TYPE = sys.argv[2]
FILE_PATH_NEW = FILE_PATH + ".new"

if FILE_TYPE=='en':
    SPLIT = '.'
elif FILE_TYPE=='cn':
    SPLIT = '。'
else:
    print("The second argument is wrong, only 'cn' or 'en' are acceptable.")
    exit()
 
f = open(FILE_PATH, encoding='utf-8')
lines = f.read().replace("e.g.", "e^g^").replace("vs.", "vs^").replace(SPLIT, "\n").splitlines()
f.close()

lines = [x.strip() for x in lines]
lines = list(filter(None, lines))

with open(FILE_PATH_NEW, "w", encoding='utf-8') as f:
    for x in lines:
        f.write(x.replace("e^g^", "e.g.").replace("vs^", "vs.") + '\n')
    f.close()

            
           
