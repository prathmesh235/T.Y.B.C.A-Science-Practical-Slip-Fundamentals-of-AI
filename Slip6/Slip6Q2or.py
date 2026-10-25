
# Alpha-Beta Pruning with Depth Limit and Heuristic

def alpha_beta(depth, node, alpha, beta, maximizing, tree):
    # Stop at the depth limit or leaf node
    if depth == 0 or node not in tree:
        return tree.get(node, node)

    if maximizing:
        best = float('-inf')

        for child in tree[node]:
            value = alpha_beta(
                depth - 1, child, alpha, beta, False, tree
            )
            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                print("Pruning remaining branches at node", node)
                break

        return best

    else:
        best = float('inf')

        for child in tree[node]:
            value = alpha_beta(
                depth - 1, child, alpha, beta, True, tree
            )
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                print("Pruning remaining branches at node", node)
                break

        return best


# Game tree with heuristic values at leaf nodes
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [3, 5],
    'E': [6, 9],
    'F': [1, 2],
    'G': [0, -1]
}

depth_limit = 3

result = alpha_beta(
    depth_limit, 'A',
    float('-inf'), float('inf'),
    True, tree
)

print("Best value:", result)
