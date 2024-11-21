# CS3342 - Organization of Programming Languages
# Written by Lukas Bozinov
# Due Date: October 9, 2024
# 2-day No-penalty Due Date: October 11, 2024

import sys # import system library to take in command-line arguments

def main(): # this method handles the main cases for single-line and block comments
    inBlock = False
    dslashflag = False
    newLines = [] #this holds all the lines that will be written to inputC_rm.cpp
    blockCommentList = []

    with open(sys.argv[1], "r") as commentedFile: # open the first command line argument after dcom_rm.py in read-only mode

        # lines holds the lines in inputC.cpp, inBlock checks whether or not the program is currently in a block comment, and blockComment holds all of the subsequent lines after the first line in the block comment
        lines = commentedFile.readlines()
        
        blockComment = ''

        #loop through every line in the list of lines
        for filteredLine in lines:
            print(newLines)
            if inBlock: # if in a block comment

                blockComment += filteredLine # add the current line to the total block comment
                blockCommentList.append(filteredLine)

                print("total: ", blockComment)
                print("filtered: ",filteredLine)
                print("list: ", blockCommentList)



                if "//" in blockCommentList[-1]:
                    
                    print("\n\nappended: ", blockComment)
                    print("\n\n\n\n")
                    newLines.append(blockComment)
                    blockComment = ''
                    inBlock = False
                    dslashflag = True


                # if the block comment ends
                if "*/" in filteredLine:

                    #set all values appropriately
                    inBlock = False
                    comment = blockComment
                    isValid = isValidDate(comment, True) #check if there was a valid date in there

                    # if not, append the block comment back into the newLines
                    if not isValid: 
                        newLines.append(blockComment)

                    blockComment = ''
                continue #continue on with parsing

            # check line for any single-line comment
            if "//" in filteredLine and any(char.isdigit() for char in filteredLine):
                comment = filteredLine[filteredLine.index("//"):] #begin validating from the //
                isValid = isValidDate(comment, False) #call helper to check if valid

                # append entire line if no valid date
                if not isValid: 
                    newLines.append(filteredLine)
                else: 
                    newLines.append(filteredLine[:filteredLine.index("//")]) #delete only the comment if valid date

            # check line for single-line BLOCK comment
            elif "/*" in filteredLine and any(char.isdigit() for char in filteredLine) and "*/" in filteredLine:
                comment = filteredLine[filteredLine.index("/*"):] #begin validating from the /*
                isValid = isValidDate(comment, True) #check for valid date

                # if invalid date, delete nothing
                if not isValid: 
                    newLines.append(filteredLine)

            #scan for block comments that go for more than one line
            elif "/*" in filteredLine and any(char.isdigit() for char in filteredLine) and "*/" not in filteredLine:
                inBlock = True
                blockComment = filteredLine
                blockCommentList.append(filteredLine)
            elif "/*" in filteredLine and not any(char.isdigit() for char in filteredLine) and "*/" not in filteredLine:
                inBlock = True
                blockComment = filteredLine
                blockCommentList.append(filteredLine)
            # if there's no comment, delete nothing 
            else: 
                newLines.append(filteredLine)
    #once the for loop has completed, write to the new file (which should be inputC_rm.cpp)
    with open(sys.argv[2], "w") as fixedFile:
        fixedFile.writelines(newLines)


#helper method for validating the date given in the inputC.cpp file
def isValidDate(line, isBlock):

    # start off the filtered line with an empty string
    filteredLine = ""

    # if this comment is not a block, we parse very slightly differently than if it weren't
    if isBlock is False:

        #delete any characters from the given string that aren't in the set
        for char in line:
            if char in set("/1234567890 "):
                filteredLine += char

        #split along blank spaces
        splitSpace = filteredLine.split()

        #look for any string in the split-space list that is length 10 (the length of a date in the proper formatting)
        for e in splitSpace:
            e = e.lstrip("/*").rstrip("/*")
            if len(e) == 10:
                filteredLine = e #set the filtered line to this string if found

        #strip the string just in case
        filteredLine = filteredLine.lstrip("/")
        parts = filteredLine.split("/")

    #if this comment is a block
    else:

        #delete any characters from the string that aren't in the given set
        for char in line:
            if char in set("/1234567890* "):
                filteredLine += char

        #split alongside blank spaces
        splitSpace = filteredLine.split()

        #strip string of all slashes
        for e in splitSpace:
            e = e.lstrip("/*").rstrip("/*")
            if len(e) == 10:
                filteredLine = e  
        
        #strip again justin case
        filteredLine = filteredLine.lstrip("/*")
        filteredLine = filteredLine.rstrip("/*")
        #split along the slashes
        parts = filteredLine.split("/")

    #validate the date format is correct and return the value
    if len(parts) != 3 or filteredLine[2] != "/" or filteredLine[5] != "/": 
        return False
    else: 
        return filteredLine[:2].isdigit() and filteredLine[3:5].isdigit() and filteredLine[6:].isdigit()

main() #call main to execute this py script
