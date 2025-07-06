# MSCS532 Assignment 1
# Author: Mohammed Zakki Chand
# Course: MSCS532
# Description:
# This script implements the Insertion Sort algorithm to sort a list
# of integers in **monotonically decreasing** order.
# Reference: Introduction to Algorithms (4th ed.) by Cormen et al.

def insertion_sort_desc(arr):
    """
    Sorts a list of integers in monotonically decreasing order using Insertion Sort.

    Parameters:
    arr (list): The list of integers to sort.

    Returns:
    list: The sorted list in decreasing order.
    """
    # Loop through the list starting from the second element (index 1)
    for i in range(1, len(arr)):
        key = arr[i]  # Current value to insert into the sorted part
        j = i - 1     # Index of the last element in the sorted part

        # Move elements that are less than the key to one position ahead
        # of their current position
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1               # Move to the previous element

        # Insert the key at its correct position
        arr[j + 1] = key

    return arr


# Test the function with a sample array
if __name__ == "__main__":
    sample_array = [12, 4, 56, 23, 8, 1]
    print("Original array:", sample_array)

    sorted_array = insertion_sort_desc(sample_array)
    print("Sorted in decreasing order:", sorted_array)
