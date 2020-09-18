import shutil

shutil.copy('test.txt', 'E:\\Python\\LearningPaython3\\parent')   # ('source', 'destination')
shutil.copy('E:\\Python\\LearningPaython3\\parent\\test.txt','E:\\Python\\LearningPaython3\\parent\\CopyAndRenamed.txt')   # Copy file and renammed
#shutil.copytree('E:\\Python\\LearningPaython3\parent','E:\\Python\\LearningPaython3\parentbkup')   # Copy folder and renamed.

#shutil.move('E:\\Python\\LearningPaython3\\parent\\test.txt', 'E:\\Python\\LearningPaython3\\MakeFolder')   # Move File
shutil.move('E:\\Python\\LearningPaython3\\MakeFolder\\test.txt', 'E:\\Python\\LearningPaython3\\parent\\fileMoveAndRenamed.txt')   # Move and Rename