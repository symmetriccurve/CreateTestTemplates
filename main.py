import os
import sys

# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

componentTestTemplate = open('temp/create-test-templates/component-test.js', 'r')
componentTemplateToText = componentTestTemplate.read()

containerTestTemplate = open('temp/create-test-templates/container-test.js', 'r')
containerTemplateToText = containerTestTemplate.read()


readDir = sys.argv[2]
typeOfFile = sys.argv[1]
writeDir = readDir.replace('src/js/','test/unit/')
splittedDirPath = writeDir.split('/')
filePath = writeDir.replace('.jsx','.spec.js')
backSlash = '/'
newFilePath = backSlash.join(splittedDirPath[:-1])

if not os.path.exists(newFilePath):
    os.makedirs(newFilePath)

if typeOfFile == 'component':
    mode = 'a' if os.path.exists(writeDir) else 'w'
    with open(filePath, mode) as componentTestTemplate:
        componentNameLowerCase = splittedDirPath[-1].replace('.jsx','')
        componentNameSplit = componentNameLowerCase.split('-')
        componentNameUpperCase = [eachWord.title() for eachWord in componentNameSplit] # ''.join(componentNameSplit)
        componentCamelCase = ''.join(componentNameUpperCase)
        componentTemplateToText = componentTemplateToText.replace('@ComponentPath',readDir).replace('.jsx','')
        componentTemplateToText = componentTemplateToText.replace('@ComponentName',componentCamelCase).replace('.jsx','')
        componentTestTemplate.write(componentTemplateToText)


# print("writeDir",writeDir.split('/'))
# splittedDirPath = writeDir.split('/')
# print("before", splittedDirPath)
# backSlash = '/'
# print("After", backSlash.join(splittedDirPath))
# os.makedirs(writeDir)
# readDir = './src/js/widgets/efile-dashboard'
# writeDir = './test/unit/widgets/efile-dashboard'

# if not os.path.exists(writeDir):
#     os.mkdir(writeDir)

# for (dirpath, dirnames, filenames) in os.walk(readDir):
#     for file in filenames:
#         if './.git' not in os.path.join(dirpath, file):
#             if './src/js' in os.path.join(dirpath, file):
#                # print('\n')
#                 #print('===========Found File, adding spec file :===========')
#                # print(os.path.join(dirpath, file))
#                 fileToText = open(os.path.join(dirpath, file), 'r').read()
#                 #print(fileToText)
#                 writepath = os.path.join(dirpath, file).replace(readDir, writeDir).replace('.js', '')+'.spec.js'
#                 #print('===========spec file added:=========== fileToText')
#                 #print(writepath)
#                 #print('\n')
#                 mode = 'a' if os.path.exists(writepath) else 'w'
#                 # print(os.path.join(dirpath))
#                 if '@component' in fileToText:
#                     with open(writepath, mode) as componentTestTemplate:
#                             print('\n')
#                             print(writepath)
#                             print('####################### Found Component')
#                             open(writepath, 'w')
#                             componentPath = os.path.join(dirpath, file).replace('.jsx','')
#                             componentTemplateToText = componentTemplateToText.replace('@ComponentPath',componentPath)
#                             componentTemplateToText = componentTemplateToText.replace('@ComponentName',file).replace('.jsx','')
#                             # componentTestTemplate()
#                             componentTestTemplate.write(componentTemplateToText)
#                 elif '@container' in fileToText:
#                     with open(writepath, mode) as containerTestTemplate:
#                             print('\n')
#                             print(writepath)
#                             print('####################### Found Component')
#                             open(writepath, 'w')
#                             componentPath = os.path.join(dirpath, file).replace('.jsx','')
#                             containerTemplateToText = containerTemplateToText.replace('@ContainerPath',componentPath)
#                             containerTemplateToText = containerTemplateToText.replace('@ContainerName',file).replace('.jsx','')
#                             # componentTestTemplate()
#                             containerTestTemplate.write(containerTemplateToText)
#     for d in dirnames:
#         if './.git' not in os.path.join(dirpath, d):
#             if './src' in os.path.join(dirpath, d):
#                 createDirPath = os.path.join(dirpath, d).replace(readDir, writeDir)
#                 if not os.path.exists(createDirPath):
#                     os.mkdir(createDirPath)
