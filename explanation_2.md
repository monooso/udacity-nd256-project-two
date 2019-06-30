# Problem 2: File Recursion #
Solution uses a list to store the matching files. A set would also have been suitable, but there's no risk of duplication with the chosen algorithm.

The file tree is searched recursively, with each item in the file tree being examined once. Time efficiency is therefore `O(n)`, where `n` is the number of files or directories in the file tree.

Worst-case space efficiency is also `O(n)` (a situation in which every single item in the file tree matches the given suffix).
