import random
all_choice = ['石头','剪刀','布']
win_list=[['石头','剪刀'],['布','石头'],['剪刀','布']]
prompt = """朋友,请出拳 :
(0) 石头
(1) 剪刀
(2) 布
请选择(0|1|2): """
pcwin = 0
renwin = 0
while True:
    pc = random.choice(all_choice)
    ind = int(input(prompt))
    player = all_choice[ind]

    print("Your choice: %s , computer choice: %s" % (player,pc))
    if pc == player :
        print('\033[32;1m平局\033[0m')
    elif [pc,player] in win_list :
        renwin += 1
        print('\033[31;1mYou win!!!\033[0m' )
    else:
        pcwin += 1
        print('\033[33;1mYou Lose!!!\033[0m')
    if pcwin == 3 or renwin == 3:
        break
print("you win %s , lose %s" % (renwin,pcwin))