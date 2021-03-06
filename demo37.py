# import graphviz as gv
# import functools
#
# graph = functools.partial(gv.Graph, format='svg')
# digraph = functools.partial(gv.Digraph, format='svg')
# g3 = graph()
# g4 = digraph()
#
#
# def add_nodes(g, nodes):
#     for n in nodes:
#         if isinstance(n, tuple):
#             g.node(n[0], **n[1])
#         else:
#             g.node(n)
#     return g
#
#
# def add_edges(g, edges):
#     for e in edges:
#         if isinstance(e[0], tuple):
#             g.edge(*e[0], **e[1])
#         else:
#             g.edge(*e)
#     return g
#
#
# nodes1 = ['A', 'B', 'C']
# edges1 = [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'C')]
# g3 = add_nodes(g3, nodes1)
# g3 = add_edges(g3, edges1)
# g3.render("graph/demo36_g3")
# nodes2 = [('A', {'label': "Node A"}), ('B', {'label': "Node B"}), ('C', {'label': "中文"}), ('D', {})]
# edges2 = [(('A', 'B'), {'label': 'edge1'}),
#           (('A', 'C'), {'label': 'edge2'}),
#           (('B', 'C'), {'label': '某種關係'}),
#           (('B', 'D'), {})]
# g4 = add_nodes(g4, nodes2)
# g4 = add_edges(g4, edges2)
# g4.render('graph/demo36_g4')
# # TB ==> Top->Bottom, BT, LR, RL
# styles = {
#     'graph': {
#         'label': '展示用的圖片',
#         'fontsize': '18',
#         'fontcolor': '#000099',
#         'bgcolor': '#C0FFEE',
#         'rankdir': "LR",
#     },
#     'nodes': {
#         'shape': 'box',
#         'fontcolor': 'black',
#         'style': 'filled',
#         'fillcolor': '#FFC0EE'
#     }
# }
#
#
# def apply_styles(g, s):
#     g.graph_attr.update(('graph' in s and s['graph']) or {})
#     g.node_attr.update(('nodes' in s and s['nodes']) or {})
#     return g
#
#
# g5 = apply_styles(g4, styles)
# g5.render('graph/demo36_g5')
import os
import time

print(os.getcwd())
DIR_NAME = "dir1"
os.mkdir(DIR_NAME)
os.chdir(DIR_NAME)
print(os.getcwd())
print("doing something.....")
time.sleep(10)
os.chdir("..")
os.rmdir(DIR_NAME)
print(os.getcwd())