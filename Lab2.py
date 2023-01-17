# Natasan Chantip   
# 6530611021

# ข้อ 1 
def whichSide(A):    
    positive = 0
    negative = 0
    for num in A:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
    if positive > negative:
        print("positive")
    elif positive < negative:
        print("negative")
    else:
        print("equal")

X = [7, -0.1, 5, -1, 0, -8]
Y = [-6, 25, -10, 1]
whichSide(X)

# ข้อ 2
def startsWith(s1, s2):
    return s1[:len(s2)] == s2
    
x = startsWith("confidential", "confide")
print(x)

# ข้อ 3 
courseIDs = ["968-141", "976-140", "977-270", "140-250"]
courseNames = [ "Data Structures and Algorithms",
                "Software and Computer Programming",
                "Software Architecture",
                "Database Systems"]

def findCourse(courseIDs, courseNames, keyword):
    result = []
    for i in range(len(courseNames)):
        if courseNames[i][:len(keyword)] == keyword:
            result.append((courseIDs[i], courseNames[i]))

    if result:
        for Course in result:
            print(Course[0], Course[1])        
    else:
        print("Not found")

keyword = str(input("Enter Course Name: "))
findCourse(courseIDs, courseNames, keyword)
print("="*30)
