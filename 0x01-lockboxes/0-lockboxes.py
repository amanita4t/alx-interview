#!/usr/bin/python3
<<<<<<< HEAD
"""Script will unlock list of lists"""


def canUnlockAll(boxes):
    """This function will take a list of lists and the content
       of a list will unlock other lists
    """

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
=======
def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n  # Create a list to keep track of visited boxes
    visited[0] = True     # The first box is unlocked initially
    queue = [0]           # Initialize a queue with the first box

    while queue:
        current_box = queue.pop(0)

        # Check the keys in the current box and add unvisited boxes to the queue
        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    # If all boxes have been visited, return True, else return False
    return all(visited)

# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # False
>>>>>>> 0cd09a5b1d68e020a94a0a6a776e5eb1308f61d9
