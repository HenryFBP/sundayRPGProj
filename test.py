def readFileToList(filePath, commentMark='#'):
    with open(filePath, 'r') as myfile:
        
        rawData = myfile.read() #for clarity
        #print(rawData) #for debugging purposes
        
        
        dataStep1 = rawData.split('\n')
        
        data = []
        
        for elem in dataStep1:
            if commentMark != '':
                if len(elem) > 0:
                    if elem[0] != commentMark:
                        data.append(elem)
            
    return data;


def createTreeForBody(test):
    
    return test



testBody = [
            "head",
            "head:face"
            "head:face:eyes"
            "head:face:eyes:left eye"
            "head:face:eyes:right eye"
            "head:face:ears"
            "head:face:ears:left ear"
            "head:face:ears:right ear"
            "head:face:nose"
            "torso",
            "torso:chest",
            "torso:waist",
            "torso:back",
           ]

print(testBody)


#testBleh = [
#            ['A1', 'A2', 'A3'],
#            ['B1','B2','B3'],
#            ['C1','C2','C3']
#           ]

#print(testBleh[1][2])

#lumpy = [
#         ["Arrow", ["10","Damaged"]],         #this is 0,???
#         ["Chestplate", ["1","Ok","Leather"]] #this is 1,???
#        ]

#print(lumpy[0][1][0][0])
#gender = readFileToList("gender.txt")


weapon_types = readFileToList("weapon_type.txt")
global_modifiers = readFileToList("global_modifiers.txt",'*')
clothe_types = readFileToList("clothe_types.txt")
clothe_areas = readFileToList("clothe_areas.txt")

#print(global_modifiers[0])


# ayy lmao im a comment
# item types
# enchantments





