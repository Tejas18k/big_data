# Define the list
my_list = [1, 2, 3, 2, 4, 2, 5]

# Define the element to find
element_to_find = 2

# Initialize a counter and a list to store indexes
count = 0
indexes = []

# Loop through the list using enumerate
for x, item in enumerate(my_list):
    if item == element_to_find:
        count += 1  # Increment the counter
        indexes.append(x)  # Add the index to the list

# Print the results
print ("The element {} occurs {} times in the list.".format(element_to_find, count))
print ("It is present at indexes: {}".format(indexes))