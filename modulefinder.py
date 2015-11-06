import os

# Provide list of directories containing modules to scan
# TODO Separate class?
def directories():
  locations = ['modules','sites/all/modules','sites/*/modules','profiles'*'modules']
  # assuming we are alredy in a confirmed drupal root
  for location in locations:
    print location

# Return total module count
def number():
