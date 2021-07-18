import csv


def csvExtractCoord(path, begin=0):
    """
    This method takes as parameter a path the csv file
    and returns a list of dictionaries containing
    the coordinates xmax, ymax and xmin, ymin.

    PARAMETERS
    ==========
    path : str
        csv file directory.
    
    begin : int
        valou from the first coordinate.

    """

    with open(path, encoding='utf-8') as csvfile:
        table = csv.reader(csvfile, delimiter=',')

        listBox = []
        for l in table:
            coordDict = dict({})

            coordDict["xmin"] = int(l[begin])
            coordDict["ymin"] = int(l[begin+1])
            coordDict["xmax"] = int(l[begin+2])
            coordDict["ymax"] = int(l[begin+3])

            listBox.append(coordDict)

    return listBox
    