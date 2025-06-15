# Imports at the beginning:
import matplotlib.pyplot as plt


def assign(new_list, i, old_list, j):
    """
    This function isn't needed. It only saves the given smaller value from either the list
    "left" or "right" in the new_list, which is always the "orig_list".

    Also, function names should be lowercase.
    """
    new_list[i] = old_list[j]


def merge_sort(orig_list: list) -> None:
    """
    This is the merge sort algorithm. An unsorted list is sorted by dividing the list into two parts recursively
    until only single elements are the parts. Then the parts are repeatedly merged with their respective counterparts
    from the step before, but sorted.
    :param orig_list: The list that is to be sorted.
    """
    # Base case: only one element.
    # If not (len > 1), rest of the code runs.
    if len(orig_list) <= 1:
        return

    mid = len(orig_list) // 2
    left = orig_list[:mid]
    right = orig_list[mid:]

    # Recursive function call for both halves
    merge_sort(left)
    merge_sort(right)

    # (Re)setting variables needed for loops
    ind_left = 0
    ind_right = 0
    i = 0

    # All elements in the two separate lists are gone through and compared to the next element in the other list.
    # As long as we haven't seen every element in both lists ...
    while ind_left < len(left) and ind_right < len(right):
        # ... we compare the next elements in the lists
        # and add the smaller one to the list of the recursive level above at the corresponding index.
        if left[ind_left] <= right[ind_right]:
            orig_list[i] = left[ind_left]
            # assign(new_list=orig_list, i=i, old_list=left, j=l)
            ind_left += 1
        else:
            orig_list[i] = right[ind_right]
            # assign(new_list=orig_list, i=i, old_list=right, j=r)
            ind_right += 1
        i += 1

    # In case either left or right are already completely gone through, the rest of the remaining list/side is added
    # to the list of the recursive level above.
    while ind_left < len(left):
        orig_list[i] = left[ind_left]
        ind_left += 1
        i += 1

    while ind_right < len(right):
        orig_list[i] = right[ind_right]
        ind_right += 1
        i += 1


# Example with visualisations
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

fig, axes = plt.subplots(
    nrows=1,
    ncols=2,
    figsize=(10, 4),
    # In case we don't need the values on the y-axis of the second plot:
    sharey=True
)

# Before sorting
axes[0].bar(
    x=range(len(my_list)),
    height=my_list,
)
axes[0].set_title("Original list", fontsize=16)
axes[0].set_ylabel("Value", fontsize=12)

# Sort
merge_sort(my_list)

# After sorting
axes[1].bar(
    x=range(len(my_list)),
    height=my_list,
)
axes[1].set_title("Sorted list", fontsize=16)

# Same for both subplots:
for ax in axes:
    ax.set_xlabel("Index", fontsize=12)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

fig.tight_layout()
plt.show()
