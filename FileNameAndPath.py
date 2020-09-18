import os

print(r'C:\Users\amity\OneDrive\Documents\AccountantsWorld\NJ927.cs')
print('\\')

print(os.getcwd())
#os.chdir(r'C:\Users\amity\OneDrive\Documents\AccountantsWorld')

print(os.path.abspath("test.txt"))    #relative path

print(os.path.abspath('..\\test2.txt'))

print(os.path.isabs('..\\test2.txt'))
print(os.path.isabs('E:\\Python\\LearningPaython3\\test.txt'))

print(os.path.dirname('E:\\Python\\LearningPaython3\\test.txt'))
print(os.path.basename('E:\\Python\\LearningPaython3\\test.txt'))

print(os.path.exists('E:\\Python\\LearningPaython3\\test.txt'))
print(os.path.isfile('E:\\Python\\LearningPaython3\\test.txt'))
print(os.path.isdir('E:\\Python\\LearningPaython3\\test.txt'))
print(os.path.getsize('E:\\Python\\LearningPaython3\\test.txt'))

print(os.listdir('E:\\Python\\LearningPaython3'))

os.mkdir('E:\\Python\\LearningPaython3\\MakeFolder')

totalSize = 0
for filename in os.listdir('E:\\Python\\LearningPaython3'):
    if not os.path.isfile(os.path.join('E:\\Python\\LearningPaython3',filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('E:\\Python\\LearningPaython3',filename))

print(totalSize)