##
# 姓名:王昱翔
# 座位號碼:07
# 修改檔名到你的座位號碼
##


import graphviz as gv

nodes = ['A', 'B', 'C', 'D', 'E']

g1 = gv.Graph(format='pdf')

for i in range(5):
    for j in range(i + 1, 5):
        g1.edge(nodes[i], nodes[j])
g1.render("graph5/hw3")
