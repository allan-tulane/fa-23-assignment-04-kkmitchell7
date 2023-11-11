# CMPS 2200 Assignment 4
## Answers

**Name:** Kailen Mitchell


Place all written answers from `assignment-04.md` here for easier grading.

1a)

1.Start with the largest 2^k that is less than or equal to N. We can find this by incrementing k in 2^k until we discover the first
value greater than N. Then we subtract 1 from k to reach the largest 2^k that is less than or equal to N.

2.Add 2^k to our solution array of coins and then subtract 2^k we just found from N to get our new N.

3.While N is not 0, repeat the process with the new value until we get 0.

1b)

This algorithm is the greedy choice because at each step we choose the largest possible coin.
Proof by contradiction: Assume that at a step, the algorithm chooses a coin 2^k which is not the largest denomination possible. Since 2^k is not the largest denonmiation there must exist a larger one 2^l where 2^l >2^k. If we had chosed 2^l instead of 2^k we would have used fewer coins because 2^l is larger and would give us fewer total coins. This contradicts how our algorithm works because it always chooses the largest possible coin, so the greedy choice property holds.

The optimal substructure property says that an optimal solution to the problem contains an optimal solution to subproblems. In the algorithm I wrote, each step of choosing a coin is a subproblem. In each choosing of a coin, the greedy method is applied by choosing the greatest possible coin, so therefore all the subproblems are optimal solutions.

Because the greedy choice property and optimal substructure property hold, we know that the algorithm is the optimal chocie.

1c)

W(n) = O(logn)
S(n) = O(logn)


2a)

Suppose we only have coins for {$1,$4,$5} and we want to make change for $8 with the fewest coins, then our algorithm from above would select 5 then 1 then 1 then 1 again, which is 4 total coins. But the optimal solution is selecting $4 and $4 for a total of 2 coins. 

Because we are no only purely working in powers of 2, the algorithm no longer works because sometimes we have instances where choosing the largest possible value makes the optimal solution not longer viable (in above example choosing 4 no longer allows us to choose 3)



2b)

Optimal Substructure property: An optimal solution to the problem contains an optimal solution to subproblems. If it is possible to make change for N dollars using a set of denoninations, then it is also possible to make change for (N-D_i) for any denonimation.



2c)
k = number of coins
N = dollar amount we are deviding up
1. Create a 2D array of k+1 rows and N+1 columns. Initialize the first row and columb of the table with 0s.

2. For every spot in the 2D array, consider each coin one by one and each dollar amount up to N. Consider each coin first. Decide whether we can include the coin and how many repitions of the coin we can include by calculating coin_amount*max_numcoins <= curr_dollar_amount

3. Determine the optimal amount by using the value in the index [k][N]

4. After filling in the entire table, backtrack to find the items for the optimal solution. Start from the bottom-right corner of the table, and if the value at index [k][N] is the same as the value at index [k-1][N], it means that coing was not included in the solution. If they are different, it means the coin was included. Continue through the column in this way deciding if each item was included and adding the added items to an array.

W(n) = O(n)
S(n) = O(n)