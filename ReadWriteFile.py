import shelve
# Read Mode
fileContent = open('E:\\Python\\LearningPaython3\\test.txt')
content = fileContent.read()
readLines = fileContent.readlines()
fileContent.close()
print(content)
# print(fileContent.readlines())

# Write Mode
writeFile = open('E:\\Python\\LearningPaython3\\Write.txt','w')
appendFile = open('E:\\Python\\LearningPaython3\\Append.txt','a')
writeFile.write('Hi this is amity timalsina!!! \n')
writeFile.write('Hi this is amity timalsina!!! ')

shelfFile = shelve.open('DummyShelve')    # Binary File
shelfFile['cat'] = ['Coco','Katty','Cloe']


