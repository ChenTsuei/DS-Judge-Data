from cyaron import *
from gen_tree import gen_tree

_n = ati([0, 1, 10, 50, 100, 1000, 5000, 10000, 50000, 100000, 100000])

for i in range(1, 11):
    test_data = IO(file_prefix="binary_tree_1_", data_id=i)
    n = _n[i]
    tree = None
    if i == 10:
        tree = gen_tree(n, 1, 0)
    else:
        tree = gen_tree(n, 0, 0)
    tree = '\n'.join(map(lambda x: str(x[0]) + " " + str(x[1]), tree))
    test_data.input_writeln(n)
    test_data.input_writeln(tree)
