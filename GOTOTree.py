import os

for folderName, subFolders, fileNames in os.walk('E:\\Python\\LearningPaython3\\parent'):
    # print('The Folder is ' + folderName)
    # print('The subFolders in ' + folderName + ' are ' + str(subFolders))
    # print('THe FileNames in ' + folderName + ' are ' + str(fileNames))
    # print()

    for subfolder in subFolders:
        print(subfolder)
        if 'fish' in subfolder:
            print(subfolder)
            #os.rmdir(subfolder)


    for file in fileNames:
        print(file)
