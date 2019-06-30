# Problem 1: LRU Cache #
Solution uses two main data structures:

1. A stack for tracking the most recently-used item.
   A LIFO structure such as a stack is an efficient way of retrieving the most-recently stored values.
2. A map for storing the cache key / value pairs.
   A map affords efficient access to a value, based on its unique identifier (key).
   
The time efficiency of the stack "set" and "get" operations is typically `O(1)`.

If the cache is full, the worst case is that the recently-used stack is completely populated by a single duplicate value. In that case, the worst-case time efficiency for the "set" operation is `O(n)`, where `n` is the size of the stack.

The map (cache) will never grow beyond 5 items. However, there is currently no upper limit on the size of the recently-used stack.

