# Tic-Tac-Toe, Minimax, and Alpha–Beta Pruning

## Introduction

*Tic-Tac-Toe*, also known as Noughts and Crosses, is a deterministic, discrete, and symmetric game. Players ('X' and 'O') take turns placing their symbols on an initially empty grid. The game concludes when a player achieves three consecutive marks in a row, column, or diagonal, or when the grid is fully occupied.

*Minimax* is a decision rule used in artificial intelligence, decision theory, game theory, statistics, and philosophy. It minimizes possible loss for a worst-case scenario, aiming to maximize the minimum gain. In the context of Tic-Tac-Toe, Minimax helps determine the best move for a player.

*Alpha–beta pruning* is an optimization technique applied to the Minimax algorithm. It reduces the number of nodes evaluated in the search tree by discarding portions that are known to be irrelevant for the final decision.

## Minimax Algorithm - Step-by-Step Explanation

1. **Understanding the Game Tree:**
   - The game state is represented as a tree, with nodes corresponding to possible game states.
   - Even-depth nodes represent the maximizing player ('X'), odd-depth nodes represent the minimizing player ('O').
   - The tree is built by considering all possible moves.

2. **Recursive Evaluation of Leaf Nodes:**
   - Terminal nodes have their utility or score evaluated.
   - Positive score for 'X' win, negative for 'O' win, and zero for a tie.

3. **Backpropagation of Scores:**
   - Scores are propagated back up the tree, with Maximizer choosing the maximum score and Minimizer choosing the minimum.

4. **Selecting the Best Move:**
   - The algorithm chooses the move leading to the node with the best score.
   - Maximizer selects the move with the maximum score; Minimizer selects the move with the minimum score.

## Alpha–Beta Pruning Algorithm - Step-by-Step Explanation

1. **Understanding Alpha and Beta:**
   - Alpha represents the best value for the maximizing player.
   - Beta represents the best value for the minimizing player.

2. **Initial Values:**
   - Alpha starts at negative infinity; beta starts at positive infinity.

3. **Pruning Conditions:**
   - If a Maximizer node's value is greater than or equal to beta, prune the branch.
   - Update alpha to the maximum of its current value and the node's value.
   - If a Minimizer node's value is less than or equal to alpha, prune the branch.
   - Update beta to the minimum of its current value and the node's value.

4. **Efficient Exploration:**
   - Alpha–beta pruning allows the algorithm to explore only relevant branches, discarding irrelevant portions of the tree.
   - Pruning conditions eliminate the need to evaluate nodes that cannot affect the final decision.

## Pseudocode

```plaintext
function alphabeta(node, depth, alpha, beta, maximizingPlayer):
    if depth is 0 or node is a terminal node:
        return the heuristic value of node

    if maximizingPlayer:
        maxEval = -infinity
        for each child of node:
            eval = alphabeta(child, depth - 1, alpha, beta, false)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  // Beta cutoff
        return maxEval

    else:
        minEval = +infinity
        for each child of node:
            eval = alphabeta(child, depth - 1, alpha, beta, true)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  // Alpha cutoff
            return minEval
```

## Visualisation

![image](https://github.com/Sre-n/NeuroNexus/assets/92539781/9a40b4e3-cbf2-421d-9d25-2e66424079f8)

## DEMO

https://github.com/Sre-n/NeuroNexus/assets/92539781/c791eaaf-8cbc-42a5-ad63-66fbdff99563


## References

- https://en.wikipedia.org/wiki/Minimax

- https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
        
