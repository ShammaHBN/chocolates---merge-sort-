# Define a function to sort chocolates using the Merge Sort algorithm
def merge_sort(chocolates, key=lambda x: x[1]):
    # Base case: if the list of chocolates has 1 or fewer elements, return it as it is already sorted
    if len(chocolates) <= 1:
        return chocolates

    # Calculate the midpoint of the list
    mid = len(chocolates) // 2

    # Recursively sort the left half of the list
    left_half = merge_sort(chocolates[:mid], key)

    # Recursively sort the right half of the list
    right_half = merge_sort(chocolates[mid:], key)

    # Merge the sorted halves together
    return merge(left_half, right_half, key)


# Define a function to merge two sorted lists
def merge(left, right, key):
    result = []  # Initialize an empty list to store the merged result
    left_index, right_index = 0, 0  # Initialize indices for the left and right lists

    # Merge the two lists by comparing elements and adding the smaller one to the result
    while left_index < len(left) and right_index < len(right):
        if key(left[left_index]) < key(right[right_index]):
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add any remaining elements from the left and right lists
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    # Return the merged result
    return result


# Define a function to sort chocolates by weight or price
def sort_chocolates(chocolates, sort_by='weight'):
    if sort_by == 'weight':
        # Sort the chocolates by weight using the merge_sort function
        return merge_sort(chocolates, key=lambda x: x[1])
    elif sort_by == 'price':
        # Sort the chocolates by price using the merge_sort function
        return merge_sort(chocolates, key=lambda x: x[2])
    else:
        # Print an error message if an invalid sorting criteria is provided
        print("Invalid sorting criteria. Please choose 'weight' or 'price'.")
        return None


# Test cases to verify the sorting functionality
def test_sort_chocolates():
    # Test case 1: Sorting by weight
    chocolates_1 = [("Dark", 50, 2), ("Milk", 30, 1), ("White", 40, 3)]
    sorted_chocolates_1 = sort_chocolates(chocolates_1, sort_by='weight')
    print("Sorted by weight:", sorted_chocolates_1)

    # Test case 2: Sorting by price
    chocolates_2 = [("Dark", 50, 2), ("Milk", 30, 1), ("White", 40, 3)]
    sorted_chocolates_2 = sort_chocolates(chocolates_2, sort_by='price')
    print("Sorted by price:", sorted_chocolates_2)

    # Test case 3: Sorting an empty list of chocolates
    chocolates_3 = []
    sorted_chocolates_3 = sort_chocolates(chocolates_3, sort_by='price')
    print("Sorted empty list:", sorted_chocolates_3)


# Run the test cases to verify the sorting functionality
test_sort_chocolates()
