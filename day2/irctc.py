""" Merge Sort - The IRCTC Waitlist Merger
IRCTC has two separately sorted waitlists one from its mobile app, one from railway counters. To produce a final unified waitlist, they don't re-sort from scratch. They merge both sorted lists in one pass compare the front of each list, pick the smaller token, advance. This is exactly merge sort's merge step. """

online_list = [3,5,6,8,10,12,13,15]
offline_list = [1,2,7,9,11,14,16]

i=0
j=0
result = []
while i<len(offline_list) and j<len(offline_list):
    if online_list[i] <= offline_list[j]:
        result.append(online_list[i])
        i += 1
    else:
        result.append(offline_list[j])
        j += 1

while i<len(offline_list):
    result.append(online_list[i])
    i += 1

while j<len(offline_list):
    result.append(offline_list[j])
    j += 1

print(result)