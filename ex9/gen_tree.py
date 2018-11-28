from random import random, choice


def gen_tree(n, left, right):
    can_left = set([1])
    can_right = set([1])
    tree = [[-1, -1] for i in range(n)]
    for i in range(2, n + 1):
        edge_pos = random()
        if edge_pos < left or left + right < edge_pos <= (1.0 - left - right) / 2:
            node = choice(tuple(can_left))
            can_left.remove(node)
            tree[node - 1][0] = i
        elif left <= edge_pos <= left + right or (1.0 - left - right) / 2 < edge_pos < 1:
            node = choice(tuple(can_right))
            can_right.remove(node)
            tree[node - 1][1] = i
        can_left.add(i)
        can_right.add(i)
    return tree
