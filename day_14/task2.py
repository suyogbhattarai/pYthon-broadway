#Q. Create a new list of repeated items from a provided list:

# nums=[3,4,2,2,1,3,3,3]
# output=[3,2]
new=[]
nums=[3,4,2,2,1,3,3,3]

for each in nums:
    if nums.count(each) > 1 and each not in new:
        new.append(each)

print(new)

