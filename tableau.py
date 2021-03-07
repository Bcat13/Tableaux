#levelList is a list of lists, which each inner list being a list of matrices at each level
def matrixLength(matrix):
    count=0
    for x in range (len(matrix)):
        for y in range (len(matrix[x])):
            count = count + 1
    return count



def partialRec(largeList):
    if largeList[len(largeList)-1] == []:
        file_name=str(len(largeList[0][0])) + "_by_"+str(len(largeList[0][0][0]))
        text_file=open('%s.txt' % file_name, 'w')

        for x in range(len(largeList)):
            text_file.write(str(largeList[x]) + '\n')
        text_file.close()

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


#Creates the matrix and calls partialRec
if __name__ == "__main__":
    numRow = int(input("Please enter the number of rows of the tableau "))
    numCol = int(input("Please enter the number of columns of the tableau "))
    matrix = [[0] * numCol for i in range (numRow)]
    for j in range (numCol):
        for i in range (numRow):
            #matrix[i][j] = int(input("Please enter entry " + "T" + str(j*numRow + i+1) + " "))
            matrix[i][j] = j*numRow + i+1

    list_mat = partialRec([[matrix]])


#    print(list_mat)
