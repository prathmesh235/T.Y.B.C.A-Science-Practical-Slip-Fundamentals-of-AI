
# Alpha-Beta Pruning Algorithm

def alpha_beta(depth, node, is_max, scores, alpha, beta, height):
    if depth == height:
        return scores[node]

    if is_max:
        best = float('-inf')

        for i in range(2):
            value = alpha_beta(
                depth + 1, node * 2 + i, False,
                scores, alpha, beta, height
            )
            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            value = alpha_beta(
                depth + 1, node * 2 + i, True,
                scores, alpha, beta, height
            )
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


scores = [3, 5, 6, 9, 1, 2, 0, -1]
height = 3

result = alpha_beta(
    0, 0, True, scores,
    float('-inf'), float('inf'), height
)

print("Optimal value:", result)
