# Input: arr[] = [2, 3, 2, 3, 5]
# Output: [0, 2, 2, 0, 1]
# Explanation: We have: 1 occurring 0 times, 2 occurring 2 times, 3 occurring 2 times, 4 occurring 0 times, and 5 occurring 1 time.


def find_freq_in_array(oldarr):
    length = len(oldarr)
    arr = [0] * length
    for num in oldarr:
        arr[num - 1] += 1
    return arr


print(find_freq_in_array([1]))
