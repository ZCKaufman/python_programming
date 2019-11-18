'''
This is an attempt to recreate the "Trillion Dollar Algorithm" known as PageRank using Python.
'''
class Node():
    # CONSTRUCTORS
    def __init__(self, name, edges = []):
        self.page = name
        self.links = edges
        self.page_rank = 0

    # GET FUNCTIONS
    def get_name(self):
        return self.page

    def get_links(self):
        return self.links

    def get_num_links(self):
        return len(self.links)

    def get_pr(self):
        return self.page_rank

    # MODIFY FUNCTIONS
    def add_link(self, link):
        self.links.append(link)

    def set_pr(self, val: float):
        self.page_rank = val

    # TO_STRING FUNCTION
    def to_string(self):
        print("Page: " + self.page)
        print("Links: {")
        for l in self.links:
            print("\t" + l.to_string())

class Graph():
    nodes = []
    def add_node(self, name: str):
        n = Node(name)
        Graph.nodes.append(n)

    def add_edge(self, p1: str, p2: str):
        node1 = ""
        node2 = ""
        for page in Graph.nodes:
            if(page.get_name() == p1):
                node1 = page
            if(page.get_name() == p2):
                node2 = page
        if(node1 and node2):
            node1.add_link(node2)
    def get_nodes(self):
        return self.nodes

    def to_string(self):
        print("Nodes: ")
        for n in self.nodes:
            print(str(n.get_name()) + ": " + str(n.get_pr()))

def page_rank(g: Graph):
    nodes = g.get_nodes()
    map = {}
    size = len(nodes)
    damp = 0.85
    page_rank = float((1 - damp) / size)
    error_margin = 0.09
    convergence = False

    for n in nodes:
        n.set_pr(float(1/size))

    while(not convergence):
        map.clear()

        s = 0.0
        for node in nodes:
            if(node.get_num_links == 0):
                s += float((d * node.get_pr()) / size)

        for n in nodes:
            for link in node.get_links():
                map[link] = float(n.get_pr() / n.get_num_links())

        convergence = True
        for node in nodes:
            map[node] = float(page_rank + s + (damp * map.get(node)))
            if(abs(map.get(node) - node.get_pr()) > error_margin):
                convergence = False
            node.set_pr(map.get(node))


def __main__():
    g = Graph()

    pages = [
        "Mspc",
        "Twtr",
        "Amzn",
        "Medm",
        "Fb"
    ]

    for page in pages:
        g.add_node(page)

    g.add_edge("Mspc","Twtr")
    g.add_edge("Twtr","Medm")
    g.add_edge("Amzn","Twtr")
    g.add_edge("Amzn","Medm")
    g.add_edge("Medm","Twtr")
    g.add_edge("Medm","Mspc")
    g.add_edge("Medm","Amzn")
    g.add_edge("Medm","Fb")
    g.add_edge("Fb","Twtr")
    g.add_edge("Fb","Amzn")

    page_rank(g)

    g.to_string()


__main__()
