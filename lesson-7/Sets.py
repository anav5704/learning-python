# Sets: 4 of 4 Collection types

nums = { 1, 2, 3, 4, 5 }
nums2 = set((1, 2, 3, 4, 5))

print(nums, nums2)
print(type(nums))


# No dupes allowed and in order     

nums3 =  {1 , 2, 2,  3, 4, 4, 5 }
print(nums3)

nums4 =  { 1, True, 2, 3, False, 4, 5 }
print(nums4) # prints: { False, 1, 2, 3, 4, 5 }