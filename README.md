# Modeling uniformly never increasing function

## Intro
This is a short python file using markov chain with absorbing states to model the number of steps for a function to reach 1. Where X_t = U~(1, X_{t-1}).

## The problem
An arbitrary upper bound $x_0$ is chosen. An integer, x_1, is generated from a uniform random distribution of integers $u~(1,x_0)$. The number x
is then used as the upper bound to generate a new number $u~(1,x_1)$. This value will be used as the next upper bound...
This is repeated untilthe integer 1 is generated. What is the average number of steps to generate 1. It is important to take into account that the distribution
$u~(1,x)$ is inclusive, so can return x.
