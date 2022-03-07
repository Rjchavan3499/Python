import random
print("welcome to head tail game")
x =  int(input("enter the number  how many times you want to toss"))
head =0
tail=1
head_count=0
tail_count=0

for i in range(x):
    k = random.randint(0, 1)
    if k == 0:
        print("head", head)
        head_count = head_count+1
    else:
        tail+1
        print("tail", tail)
        tail_count = tail_count+1


head_per = (head_count  / 100)*100
tail_per = (tail_count /100 ) * 100
if head_per > tail_per:
    print("head is won ",head_count)
    print("the per of head  is", head_per)
    print("the per of tail  is", tail_per)

else:
    print("tail is won",tail_count)
    print("the per of head  is", head_per)
    print("the per of tail  is", tail_per)







