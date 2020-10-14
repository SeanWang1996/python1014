##
# 姓名:王昱翔
# 座位號碼:07
# 修改檔名到你的座位號碼
##


import graphviz as gv
from itertools import combinations

nodes = ['A', 'B', 'C', 'D', 'E']
edges = list(combinations(nodes, 2))
g1 = gv.Graph(format='pdf')
for node in nodes:
    g1.node(node)
for e1, e2 in edges:
    g1.edge(e1, e2)
g1.render("graph/hw3_07")
