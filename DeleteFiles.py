import os
import shutil
#os.unlink('DummyShelve.bak')   # Delete File

#os.rmdir('E:\\Python\\LearningPaython3\\deleteme')  # Delete empty Folders
#shutil.rmtree('E:\\Python\\LearningPaython3\\deleteme2')  #Delete folder and files inside

print(os.getcwd())

# Remove files from directory
for fileName in os.listdir():
    if fileName.endswith('.txt'):
        #print(fileName)
        #os.unlink(fileName)

# Soft Delete using send2trace
