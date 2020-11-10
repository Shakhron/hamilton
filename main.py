import xml.etree.ElementTree as ET

def inputfromxml(filename):
    graph = {}
    tree = ET.parse(filename)
    root = tree.getroot()
    graph_ = root.find('graph')
    for i in range(0, 14):
        node = graph_[i].attrib
        source = node.get('source')
        neighbour = node.get('neighbour')
        neighbour_mas = neighbour.split(',')
        graph[source] = neighbour_mas
    return graph


def startxml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    task = root[1].attrib
    start_id = task.get('start.id')
    return start_id


def get_size(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    gr = root.find('graph')
    s = gr.get('size')
    return int(s)


def gam(graph_, size, start, path):
    if start not in set(path):
        path.append(start)
        if len(path) == size:
            print('Гамильтонов цикл:')
            return path
        for neighbor in graph_.get(start, []):
            res_path = [i for i in path]
            next = gam(graph_, size,neighbor, res_path)
            if next is not None:
                return next

gra = inputfromxml('graph.xml')
si = get_size('graph.xml')
st = startxml('graph.xml')
opened = []
print(gam(gra, si, st, opened))
