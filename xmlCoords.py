import xml.etree.ElementTree as Et


def xmlExtractCoord(path, item, child):
    """
    This method takes as parameter the root element of
    the XML file and returns a list of dictionaries containing
    the coordinates xmax, ymax and xmin, ymin.

    PARAMETERS
    ==========
    path : str
        XML file directory.

    item : str
        searched xml tag.

    child : str
        searched object.

    """
    tree = Et.parse(path)
    root = tree.getroot()

    listBox = []

    for obj in root.iter(item):
        for box in obj.iter(child):
            coordDict = dict({})
            cont = 0
            for coords in box:
                coordDict[coords.tag] = int(coords.text)
                cont += 1
                if cont == 4:
                    listBox.append(coordDict)

    return listBox
