# count=0
# val='rama'
# for x in val:
#     print(x)
#     count=count+1
#     print(count)
# #print(count)
   

# count=0
# for x in range(1,10,2):
#     print(x)
#     count=count+1
# print("total values of odd:",count)

# count=0
# sum=0
# for x in range(1,10,2):
#     print(x)
#     count=count+1
#     sum=sum+x
# print("total values of odd:",count)
# print("total sum of odd:",sum)

count=0
sum=0
product=1
for x in range(1,10,2):
    print(x)
    count=count+1
    sum=sum+x
    product=product*x
print("total values of odd:",count)
print("total sum of odd:",sum)
print("total product of odd:",product)