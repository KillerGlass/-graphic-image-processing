import csv


def csvExtractCoord(path):
    """
    This method takes as parameter a path the csv file
    and returns a list of dictionaries containing
    the coordinates xmax, ymax and xmin, ymin.

    PARAMETERS
    ==========
    path : str
        csv file directory.

    """

    with open(path, encoding='utf-8') as csvfile:
        table = csv.reader(csvfile, delimiter=',')

        listBox = []
        for l in table:
            coordDict = dict({})

            coordDict["xmin"] = int(l[0])
            coordDict["ymin"] = int(l[1])
            coordDict["xmax"] = int(l[2])
            coordDict["ymax"] = int(l[3])

            listBox.append(coordDict)

    return listBox
