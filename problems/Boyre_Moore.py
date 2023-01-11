def isMajority(candidate, nums):

    count = 0

    for el in nums:
        if el == candidate:
            count += 1
    
    if count > len(nums) // 2:
        return True
    return False

def getCandidate(nums):
    candidate = None
    count = 0

    for el in nums:
        if count == 0:
            candidate = el
        count += (1 if el == candidate else -1)

    return candidate

def majorityElement(nums):

    candidate = getCandidate(nums)
    if isMajority(candidate, nums):
        print(candidate, "is majority element")
    else:
        print("No majority element")


majorityElement([1,1,1,3,3,3,3,3,3])