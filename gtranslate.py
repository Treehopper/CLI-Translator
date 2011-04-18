#!/usr/bin/python

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program. If not, see <http://www.gnu.org/licenses/>.

#Usage:
# ./gtranslate.py "Hello World" en it

import signal
import sys
import urllib
import re
import os

class BreakHandler:
    def __call__(self, signame, sf):
        print "interrupted"
        sys.exit(1)
        return

signal.signal(signal.SIGINT, BreakHandler())

TO_TRANSLATE=sys.argv[1]
LANG=sys.argv[2]
TARGET_LANG=sys.argv[3]

LANG_PAIR=LANG + "|" + TARGET_LANG
params = urllib.urlencode({'v': '1.0', 'q': TO_TRANSLATE, 'langpair': LANG_PAIR})
try:
    f = urllib.urlopen("http://ajax.googleapis.com/ajax/services/language/translate?%s" % params)
except IOError, e:
    print "IOError"
    sys.exit(2)


result=f.read()

p = re.compile('{"responseData": {"translatedText":"([^"]*)')
m = p.match(result)
ANSWER = m.group(1)
print ANSWER

#    TODO: write and READ cache for faster access to common words
#HOME = os.environ['HOME']
#GTRANLATE_DIR = os.path.join(HOME, ".gtranslate")
#if os.path.exists(GTRANLATE_DIR) and os.path.isdir(GTRANLATE_DIR) and os.access(GTRANLATE_DIR, os.F_OK | os.W_OK):
#    file_open_mode = "a"
#else:
#    os.mkdir(GTRANLATE_DIR)
#    file_open_mode = "w"

#DB_FILE = os.path.join(GTRANLATE_DIR, LANG + "2" + TARGET_LANG + ".csv")
#with open(DB_FILE, file_open_mode) as fobj:
#    fobj.write('"'+ TO_TRANSLATE +'"'+ ';'+ '"'  + ANSWER + '"')

