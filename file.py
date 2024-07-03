# File Basic Operations

import os
import sys


sourceDir = os.getcwd();
print(sourceDir)


## Check if the specific directory is existed
isDir = os.path.isdir(sourceDir+'lucas')
print(isDir)
# sys.exit('mixed string')


#CHANEG  DIR
os.chdir('f://')
print(os.getcwd())


# List Dir
print(os.listdir())

## Create Directory
os.chdir(sourceDir)
if not os.path.isdir(sourceDir+"/lucas"):
    os.mkdir('lucas')
else:
    print(sourceDir+"/lucas")