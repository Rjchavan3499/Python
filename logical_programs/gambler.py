import random
print("welcome to gambler game")
amount = 10
win =1
loss=0
win_count=0
loss_count=0
c = 0

while amount > 0:
    c = c+1
    for  i in range(amount):
        k = random.randint(0, 1)
    if k == 0:
        win = win+1
        print("win", win)
        win_count = win_count+1
        amount = amount+1
    else:
        loss = loss+1
        print("loss", loss)
        loss_count = loss_count+1
        amount = amount - 1


win_per = (win_count / 100)*100
loss_per = (loss_count /100 ) * 100
if win_per > loss_per:
    print("No of times gambler bet is",c)
    print("gambler is won ",win_count)
    print("the per of won  is", win_per)
    print("the per of loss  is", loss_per)


else:
    print("No of times gambler bet is", c)
    print("gamber is loss",loss_count)
    print("the per of won  is", win_per)
    print("the per of loss  is",loss_per)







