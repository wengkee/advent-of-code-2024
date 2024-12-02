from data_file import DataFile

data_file = DataFile("data/d2.data")

def isSorted(l):
    return all( l[i] <= l[i+1] for i in range(len(l)-1) ) or all( l[i] >= l[i+1] for i in range(len(l)-1) )

def isGapSafe(l):
    return all( 1 <= abs(l[i] - l[i+1]) <= 3 for i in range(len(l)-1) )

def isSafe(l):
    return isSorted(l) and isGapSafe(l)
        
safeReport = 0
otherSafeReport = 0 
for line in data_file.lines:

    nums = [ int(n) for n in line.split()]
    # print(nums,"isSorted:", isSorted(nums),"isGapSafe:", isGapSafe(nums))
    if isSorted(nums) and isGapSafe(nums):
        safeReport += 1
    else:
        print(nums)
        if any( isSafe( nums[:i] + nums[i+1:] ) for i in range(len(nums)) ):
            '''
            a[start:stop]  # items start through stop-1
            a[start:]      # items start through the rest of the array
            a[:stop]       # items from the beginning through stop-1
            a[:]           # a copy of the whole array
            '''
            # print(nums[:i], " and ", nums[i+1:])
            otherSafeReport += 1

print(safeReport)
print(safeReport + otherSafeReport)
