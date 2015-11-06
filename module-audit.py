import filecmp
import os

import drupalchecker

home = os.getenv("HOME")
print home 

drupalchecker.checkme()
