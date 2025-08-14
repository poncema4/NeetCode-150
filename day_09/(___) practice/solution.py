def has_subarray(nums, k):
    # does not always mean it is sorted
    # if two or more consecutive elements sum to k
    hash_set = set()
    curr = 0

    for i in range(len(nums)):
        curr += nums[i]
        if (curr - k) in hash_set:
            return True
    
        hash_set.add(curr)

    return False

if __name__ == "__main__":
    l1 = [3,5,7,8,98,9,4,687,5]
    k1 = 4
    
    assert has_subarray(l1, k1) == True