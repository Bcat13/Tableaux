import pickle
#levelList isat each level
def matrixLength(matrix):
    count=0
    for x in range (len(matrix)):
        for y in range (len(matrix[x])):
            count = count + 1
    return count

def partialRec(largeList):
    if largeList[len(largeList)-1] == []:
        file_name=str(len(largeList[0][0])) + "_by_"+str(len(largeList[0][0][0]))

        with open('%s.txt' % file_name, "wb") as fp:
            pickle.dump(largeList[:len(largeList)-1], fp)

        return largeList[:len(largeList)-1]
    else:
        #list of matrices at this level
        levelList = largeList[len(largeList)-1]
        newLevel=[]
        flatten=[]
        for x in range (len(levelList)):
            newLevel.append(partialOrder(levelList[x]))
        for w in range (len(newLevel)):
            for o in range (len(newLevel[w])):
                if newLevel[w][o] not in flatten:
                    flatten.append(newLevel[w][o])
        largeList.append(flatten)

        return partialRec(largeList)




#Takes in a matrix and returns all of the iterations for the next level derived from that.
def partialOrder(matrix):
    levelList=[]
    copy = [[0] * len(matrix[0]) for i in range (len(matrix))]
    #columns - 1 because we don't need to look at the final column since there's nothing to right
    for x in range (len(matrix)):
        for y in range (len(matrix[0])):
            copy[x][y] = matrix[x][y]


    for col in range (len(matrix[0])-1):
        for row in range (len(matrix)):
            current = matrix[row][col]

            for cols in range (col+1, len(matrix[0])):
                for rows in range (len(matrix)):

                    if (copy[rows][cols] == current + 1 and row != rows):

                        temp=current
                        copy[row][col]=copy[rows][cols]
                        copy[rows][cols]=temp



                        copy2 = [[0] * len(matrix[0]) for i in range (len(matrix))]
                        for x in range (len(matrix)):
                            for y in range (len(matrix[0])):
                                copy2[x][y] = copy[x][y]



                        levelList.append(copy2)

                        #resets copy
                        for x in range (len(matrix)):
                            for y in range (len(matrix[0])):
                                copy[x][y] = matrix[x][y]

                        if (current != matrix[row][col]):
                            break
                if (current != matrix[row][col]):
                    break

    return levelList

if __name__ == "__main__":
    print("")
    print("Welcome to Tableau!\n")
    print("")
    print("Enter !discover to add a new tableau to the database")
    print("Enter !research to learn about a tableau in the database")
    print("Enter !quit to end the program\n")
    option=""
    while (option != "!quit"):
        print("")
        print("")
        option = input("Select an option: ")
        print("")
        if(option=="!research"):

            rows = input("Rows of Tableau: ")
            columns = input("Columns of Tableau ")

            file_name=str(rows) + "_by_"+str(columns)
            try:

                with open('%s.txt' % file_name, "rb") as fp:   # Unpickling
                    matrix = pickle.load(fp)
            except:
                print("")
                print("This tableau is not in database")
                continue
            print("Enter !print to print the matrix")
            print("Enter !level to find a print a level of the matrix")
            print("Enter !lookup to find the location of a matrix in the partial order")
            print("Enter !length to find the number of matrices in the partial order")
            print("Enter !depth to find the depth of the partial order")
            print("Enter !quit to end program\n")
            option=input("Select an option: ")
            
            if option == "!level":
                level = input("Select a level: ")
                print(matrix[int(level)-1])
            elif (option == "!depth"):
                print(len(matrix))
            elif (option == "!length"):
                print(matrixLength(matrix))
            elif (option=="!lookup"):
                print("Not yet implemented")
            elif (option=="!print"):
                print(matrix)

        elif (option =="!discover"):

            numRow = int(input("Please enter the number of rows of the tableau "))
            numCol = int(input("Please enter the number of columns of the tableau "))
            matrix = [[0] * numCol for i in range (numRow)]
            for j in range (numCol):
                for i in range (numRow):
                    matrix[i][j] = j*numRow + i+1

            list_mat = partialRec([[matrix]])

    print("Thank you for using Tableau!\n")
