import os

def checkme():
  print "Am i a drupal root?"
  d7files =['includes/common.inc','misc/drupal.js','modules/field/field.module']
  d8files =['core/includes/common.inc','core/core.services.yml','core/misc/drupal.js']

  # Don't even start if we aren't in something resembling a drupal root
  if os.path.isfile('index.php'):
    d7score = 0;
    d8score = 0;
    for file in d7files:
      if os.path.isfile(file):
        d7score = d7score + 1
      else:
        break
    for file in d8files:
      if os.path.isfile(file):
        d8score = d8score + 1
      else:
        break

    if d7score == 3:
      print "We have a drupal 7"
      return "drupal7"
    if d8score == 3:
      print "We have a drupal 8"
      return "drupal8"
  else:
    print "Not in a drupal root directory: goodbye"
    return False
