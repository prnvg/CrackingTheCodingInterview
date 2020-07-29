# Stacks and Queues

1. __Three in One:__ Describe how you could use a single array to implement three stacks.
2. __Stack Min:__ How would you design a stack which, in addition to pus and pop, has a function min which returns the minimum element? Push, pop, and min should all operate in O(1) time.
3. __Stack of Plates:__ Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a datastructure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return the same value as it would if there were just a single stack). FOLLOW UP -> implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
