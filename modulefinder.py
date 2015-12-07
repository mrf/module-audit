import os

# Provide list of directories containing modules to scan
def directories():
    locations = ['sites','profiles']
    qualifiedDirs = []
    for location in locations:
        for dirName, subdirList, fileList in os.walk(location):
            if dirName.endswith('modules'):
                qualifiedDirs.append(dirName)
            if dirName.endswith('themes'):
                qualifiedDirs.append(dirName)

    return qualifiedDirs

# Return total module count
def metadata():
    for location in directories():
        for dirName, subdirList, fileList in os.walk(location):
            print('Found directory: %s' % dirName)
            for fname in fileList:
                if fname.endswith('.info'):
                    infoFile = dirName + '/' + fname
                    infoFile = open(infoFile,'r')
                    print infoFile.read() 
