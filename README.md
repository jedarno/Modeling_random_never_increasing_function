# Modeling uniformly never increasing function

## Intro
This is a short python file using markov chain with absorbing states to model the number of steps for a uniform random distribution to count down to 1, when the next upper bound is decided by the current value returned.

## The problem
An arbitrary upper bound ![equation](https://latex.codecogs.com/svg.image?x_%7B0%7D) is chosen. An integer,![equation](https://latex.codecogs.com/svg.image?x_%7Bt%7D), is generated from a discrete uniform distribution ![equation](https://latex.codecogs.com/svg.image?U%5C%7B1,x_0%5C%7D) A number is then is then generated from ![equation](https://latex.codecogs.com/svg.image?U%5C%7B1,x_1%5C%7D). This value will be used as the next upper bound...
This is repeated untilthe integer 1 is generated. What is the average number of steps to generate 1. It is important to take into account that the distribution
<img src="https://latex.codecogs.com/gif.latex?O_t=\text {U~(1,x)} t " /> is inclusive, so can return 
<img src="https://latex.codecogs.com/gif.latex?O_t=\text {x} t " />.
