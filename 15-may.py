#wap to sum of the indices of a string:"python"
#wap to print the factorial from 1 to 8.
#wap to print only prime no from 1 to 15.

# for i in range(1,15):
#     print(i)
#     if i%i==0:
#         continue


# str="python"
# total=0
# for i in range(len(str)):
#     print(i)
#     total=total+i
#     print("sum of indices:",total)


# for num in range(1,15):
#     # print(num)
#     if num>1 and num%2==1:
#         print(num)


for num in range(1, 15):

    if num > 1:
        for i in range(2, num):

            if num % i == 0:
                break
        else:
            print(num)




