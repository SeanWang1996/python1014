import graphviz as gv

# # manual create a directory graph
# # format='svg'|'png'|'pdf'
# g1 = gv.Graph(format='svg')
# g1.node('A')
# g1.node('B')
# g1.node('C')
# g1.edge('A', 'B')
# g1.edge('A', 'A')
# g1.edge('B', 'B')
# g1.edge('B', 'C')
# print(g1.source)
# g1.render("graph/demo33")

# manual create a directory graph
# format='svg'|'png'|'pdf'
g1 = gv.Digraph(format='pdf')
# nodes = ['A', 'B', 'C','D', 'E']
# for node in nodes:
#     g1.node(node)
g1.edge('A', 'B')
g1.edge('A', 'A')
g1.edge('B', 'B')
g1.edge('B', 'B')
g1.edge('C', 'B')
g1.edge('A', 'D')
g1.edge('E', 'F', '132546')
g1.edge('E', 'A')
print(g1.source)
g1.render("graph2/demo33_3")