def trapped_water(height,width):
    """
    Calculates the amount of trapped rain water using the Two Pointers technique.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    
    # 1. Edge Case Handling
    if not height:
        print(0)
        return 0
    
    # 2. Initialize Pointers
    l, r = 0, len(height) - 1
    
    # 3. Initialize Max Height Trackers
    max_left, max_right = height[l], height[r]
    
    res = 0
    
    # 4. Main Loop
    while l < r:
        
        # 5. Determine the Limiting Factor (Bottleneck)
        if max_left < max_right:
            
            # Move the left pointer inward
            l += 1
            max_left = max(max_left, height[l])
            
            # Calculate trapped water for the current position (l).
            res += (max_left - height[l]) * width[r]
            
        else:
            r -= 1
            # Update the max height seen from the right.
            max_right = max(max_right, height[r])
            # Calculate trapped water for the current position (r).
            res += (max_right - height[r])*width[r]
    
    return res

trapped_water([3, -4, 2, -1, 5, -3, 0],[2, 3, 1, 2, 1, 2, 3])