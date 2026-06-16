array = [2,13,10,15,12,11,10,5,7,8,1,3,4]

min_value = array[0] # O(1)
max_value = array[0] # O(1)

for num in array: # runs n times -> O(n)
    if num < min_value: # O(1)
        min_value = num # O(1)
    elif num > max_value: # O(1)
        max_value = num # O(1)

# The loop runs n times, and each iteration does constant work:
# n × O(1) = O(n)

print("min:", min_value) # O(1)
print("max:", max_value) # O(1)