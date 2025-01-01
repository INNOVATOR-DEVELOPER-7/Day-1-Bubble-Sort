# Function to perform Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Get the list of numbers from the user
user_input = input("Enter numbers separated by spaces: ")

# Convert the string input to a list of integers
arr = list(map(int, user_input.split()))

# Print the unsorted list
print("Unsorted list:", arr)

# Sort the list using Bubble Sort
sorted_arr = bubble_sort(arr)

# Print the sorted list
print("Sorted list:", sorted_arr)
