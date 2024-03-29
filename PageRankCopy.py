'''
This is an attempt to recreate the "Trillion Dollar Algorithm" known as PageRank using Python.
'''
import sys
class Node():
    # CONSTRUCTORS
    def __init__(self, name, edges = [], pr = 0.0):
        self.page = name
        self.links = edges
        self.page_rank = pr

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
            print("\t" + l.get_name())

class Graph():
    nodes = []
    def add_node(self, name: str):
        n = Node(name)
        Graph.nodes.append(n)
        '''print(str(len(Graph.nodes)) + " NODES IN GRAPH")
        print("NODES:")
        for n in Graph.nodes:
            print(n.get_name(), end=" ")
        print("") '''

    def add_edge(self, p1: str, p2: str):
        node1 = 0
        node2 = 0
        for page in Graph.nodes:
            if(page.get_name() == p1):
                print("HIT1: " + p1)
                node1 = page
            elif(page.get_name() == p2):
                print("HIT2: " + p2)
                node2 = page
        if(node1 and node2):
            print("ADDED " + p2 + " TO " + p1)
            node1.add_link(node2)
            #print(p1 + " NOW HAS " + str(len(node1.get_links())) + " LINKS")

    def get_nodes(self):
        return self.nodes

    def to_string(self):
        for n in self.nodes:
            print(str(n.get_name()) + ",\t" + str(n.get_pr()) + ",\t" + "links:", end=" ")
            for l in n.get_links():
                print(l.get_name(), end=" ")
            print("")

def page_rank(g: Graph):
    nodes = g.get_nodes()
    map = {}
    size = len(nodes)
    damp = 0.85
    #page_rank = float((1 - damp) / size)
    page_rank = float(1 / size)
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
                try:
                    map[link] = map.get(link) + float(n.get_pr() / n.get_num_links())
                except:
                    map[link] = float(n.get_pr() / n.get_num_links())

        convergence = True
        #for node in nodes:
            #print(node.get_name(), end=" - ")
        for node in nodes:
            try:
                map[node] = float(page_rank + s + (damp * map.get(node)))
            except:
                map[node] = float(page_rank + s)
            if(abs(map.get(node) - node.get_pr()) > error_margin):
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

    for page in pages:
        g.add_node(page)

    g.add_edge("a", "e")
    g.add_edge("b", "e")
    g.add_edge("b", "f")
    g.add_edge("c", "f")
    g.add_edge("e", "g")
    g.add_edge("e", "h")
    g.add_edge("f", "h")

    page_rank(g)

    for n in g.get_nodes():
        print(n.get_name() + " edges: { ", end=" ")
        for e in n.get_links():
            print(e.get_name(), end=", ")
        print(" }")

    g.to_string()



__main__()
