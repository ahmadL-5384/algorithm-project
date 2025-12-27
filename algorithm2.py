
def trappedW_BF(height,width):
    """
    Calculates the total amount of rainwater that can be trapped.
    Approach: Brute Force - Iterate through every element and find 
    the max boundaries for that specific element.
    """
    
    # 1. Edge Case Handling

    if not height:
        return 0
    
    n = len(height)
    res = 0
    # 2. Iterate through every bar in the elevation map
    for i in range(n):

        leftMax = rightMax = height[i]
        # 3. Scan Left: Find the maximum height from the start up to current index i
        for j in range(i):
            leftMax = max(leftMax, height[j])
        
        # 4. Scan Right: Find the maximum height from current index i to the end
        for j in range(i + 1, n):
            rightMax = max(rightMax, height[j])
        # 5. Calculate Water for current index i
        res += (min(leftMax, rightMax) - height[i]) * width[i]
    print(res)    
    return res


trappedW_BF([-2, 3, -4, 2, -1, 5, -3],[ 2, 2,  3, 1,  2, 1,  2])
