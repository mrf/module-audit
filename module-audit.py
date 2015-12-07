import filecmp
import os

import drupalchecker
import modulefinder

if drupalchecker.checkme():
    modulefinder.metadata()
