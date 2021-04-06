D = {1:2, 5:1, 1.21:12, 10:10}
sum_key = 0
sum_content = 0
sum_in_common = []
for i in D:
    sum_key += i
for x in D.values():
    sum_content += x     

sum_in_common.append(sum_key)
sum_in_common.append(sum_content)
print(sum_in_common)