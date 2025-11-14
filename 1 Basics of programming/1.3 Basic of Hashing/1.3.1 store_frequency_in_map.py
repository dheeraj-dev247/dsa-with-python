def store_frequency_of_numbers(nums,x):
    length = len(nums)
    freq_map = {}
    for i in range(0,length):
        if nums[i] in freq_map:
            freq_map[nums[i]] += 1
        else:
            freq_map[nums[i]] = 1
    print(freq_map)
    return freq_map[x]

print(store_frequency_of_numbers([1,2,3,1,2,2],2))