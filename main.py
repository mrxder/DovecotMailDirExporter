import os
import sys
import datetime

def editMail(basePaht : str, filename :str):

    try:
        fullPath = os.path.join(basePaht, filename)

        rawDate = ""
        rawSubject = ""
        with open(fullPath, 'r') as file_in:
            for line in file_in:

                if len(line) > 6 and line[0 : 5] == "Date:":
                    rawDate = line
                
                if "Subject:" in line:
                    rawSubject = line
                
                if len(rawDate) > 1 and len(rawSubject) > 1:
                    break

        rawDate = rawDate[6:-1]
        partsDate = rawDate.split(',')
        rawDate = partsDate[1]
        partsDate = rawDate.split(' ')
        rawDate = ""
        for pdel in partsDate:
            if len(pdel) > 0 and (pdel[0] == "+" or pdel[0] == '-'):
                break
            if len(pdel) > 0:
                rawDate += pdel + "_"
        os.rename(fullPath, os.path.join(basePaht, rawDate + ".eml"))
    except UnicodeDecodeError:
        print("UnicodeError skip")
    except IndexError:
        print("Date in wrong format")


def travers(dir : str):
    elems = os.listdir(dir)
    for elem in elems:
        if elem[0] != '.':
            
            elemPath = os.path.join(dir, elem)
            if os.path.isfile(elemPath):
                if ".mail" in elem and "W=" in elem:
                    editMail(dir, elem)
                else:
                    os.remove(elemPath)
            
            if os.path.isdir(elemPath):
                travers(elemPath)



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Specify directory")
    else:
        travers(sys.argv[1])