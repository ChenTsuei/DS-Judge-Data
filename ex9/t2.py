import sys
from cyaron import *
from gen_tree import gen_tree

sys.setrecursionlimit(30000)


def vis_tree(tree):
    def pre_vis(u):
        pre_ans.append(u + 1)
        if tree[u][0] != -1:
            pre_vis(tree[u][0] - 1)
        if tree[u][1] != -1:
            pre_vis(tree[u][1] - 1)

    def mid_vis(u):
        if tree[u][0] != -1:
            mid_vis(tree[u][0] - 1)
        mid_ans.append(u + 1)
        if tree[u][1] != -1:
            mid_vis(tree[u][1] - 1)

    pre_ans = []
    mid_ans = []
    pre_vis(0)
    mid_vis(0)
    return pre_ans, mid_ans


_n = ati([0, 1, 10, 50, 100, 500, 1000, 2000, 5000, 10000, 20000])

for i in range(1, 11):
    test_data = IO(file_prefix="binary_tree_2_", data_id=i)
    n = _n[i]
    tree = None
    if i == 10:
        tree = gen_tree(n, 1, 0)
    else:
        tree = gen_tree(n, 0, 0)
    pre_ans, mid_ans = vis_tree(tree)
    test_data.input_writeln(n)
    test_data.input_writeln(' '.join(map(str, pre_ans)))
    test_data.input_writeln(' '.join(map(str, mid_ans)))
