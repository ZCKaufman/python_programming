'''
This is an attempt to recreate the "Trillion Dollar Algorithm" known as PageRank using Python.
'''
import sys
class Node():
    # CONSTRUCTORS
    def __init__(self, name, edges = [], pr = 0.0):
        print("NODE : INIT")
        self.page = name
        self.links = edges
        self.page_rank = pr

    # GET FUNCTIONS
    def get_name(self):
        print("NODE : GETNAME")
        return self.page

    def get_links(self):
        print("NODE : GETLINKS")
        return self.links

    def get_num_links(self):
        print("NODE : GETNUMLINKS")
        return len(self.links)

    def get_pr(self):
        print("NODE : GETPR")
        return self.page_rank

    # MODIFY FUNCTIONS
    def add_link(self, link):
        print("NODE : ADDLINK")
        self.links.append(link)

    def set_pr(self, val: float):
        print("NODE : SETPR")
        self.page_rank = val

    # TO_STRING FUNCTION
    def to_string(self):
        print("NODE : TOSTRING")
        print("Page: " + self.page)
        print("Links: {")
        for l in self.links:
            print("\t" + l.get_name())

class Graph():
    print("GRAPH : -")
    nodes = []
    def add_node(self, name: str):
        print("GRAPH : ADDNODE")
        n = Node(name)
        Graph.nodes.append(n)

    def add_edge(self, p1: str, p2: str):
        print("GRAPH : ADDEDGE")
        node1 = 0
        node2 = 0
        for page in Graph.nodes:
            if(page.get_name() == p1):
                node1 = Graph.nodes.index(page)
            elif(page.get_name() == p2):
                node2 = Graph.nodes.index(page)
        if(node1 and node2):
            Graph.nodes[node1].add_link(Graph.nodes[node2])

    def get_nodes(self):
        print("GRAPH : GETNODES")
        return self.nodes

    def to_string(self):
        print("GRAPH : TOSTRING")
        for n in self.nodes:
            print(str(n.get_name()) + ",\t" + str(n.get_pr()) + ",\t" + "links:", end=" ")
            for l in n.get_links():
                print(l.get_name(), end=" ")
            print("")

def page_rank(g: Graph):
    print("PAGE_RANK : -")
    nodes = g.get_nodes()
    print("PAGE_RANK: NODES: " + str(len(nodes)))
    map = {}
    size = len(nodes)
    damp = 0.85
    #page_rank = float((1 - damp) / size)
    page_rank = float(1 / size)
    error_margin = 0.09
    convergence = False

    for n in nodes:
        print("PAGE_RANK : for n in nodes")
        n.set_pr(float(1/size))

    while(not convergence):
        print("PAGE_RANK : WHILE")
        map.clear()

        s = 0.0
        for node in nodes:
            print("PAGE_RANK : WHILE for node in nodes 1")
            if(node.get_num_links == 0):
                s += float((d * node.get_pr()) / size)

        for n in nodes:
            print("PAGE_RANK : WHILE for node in nodes 2")
            for link in node.get_links():
                print("PAGE_RANK : WHILE for link in node.get_links()")
                try:
                    print("PAGE_RANK : TRY")
                    map[link] = map.get(link) + float(n.get_pr() / n.get_num_links())
                except:
                    print("PAGE_RANK : EXCEPT")
                    map[link] = float(n.get_pr() / n.get_num_links())

        convergence = True
        #for node in nodes:
            #print(node.get_name(), end=" - ")
        for node in nodes:
            print("PAGE_RANK : WHILE for node in nodes 3")
            try:
                print("PAGE_RANK : WHILE for node in nodes 3 try 2")
                map[node] = float(page_rank + s + (damp * map.get(node)))
            except:
                print("PAGE_RANK : WHILE for node in nodes 3 try 2")
                map[node] = float(page_rank + s)
            if(abs(map.get(node) - node.get_pr()) > error_margin):
                print("PAGE_RANK : WHILE for node in nodes 3 if")
                convergence = False
            node.set_pr(map.get(node))


def __main__():
    g = Graph()

    '''pages = [
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
    g.add_edge("Mspc", "Fb")
    g.add_edge("Amzn", "Fb")
    g.add_edge("Twtr", "Fb")
    g.add_edge("Medm", "Fb")
    g.add_edge("Fb", "Twtr")'''

    pages = {
        "a",
        "b",
        "c",
        "e",
        "f",
        "g",
        "h"
    }



    g.add_edge("a", "e")
    g.add_edge("b", "e")
    g.add_edge("b", "f")
    g.add_edge("c", "f")
    g.add_edge("e", "g")
    g.add_edge("e", "h")
    g.add_edge("f", "h")

    page_rank(g)

    g.to_string()


__main__()
