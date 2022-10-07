def csvToDict(yourDict, readFrom):
    csvFile = open(readFrom, "r")
    lines = csvFile.readlines()

    count = 0
    for line in lines:
        if count == 0: # To skip header
            pass
        else:    
            inp = line.split(",")
            yourDict[inp[0]] = inp[1]
        count += 1