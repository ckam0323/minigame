from  random  import  randint, choice

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def exam():
    "pls  give a question"
    cmsd = {'+':add,'-':sub}
    nums = [randint(1,100) for i in range(2)]
    nums.sort(reverse=True)
    op = choice('+-')
    # if op == '+':
    #     result = nums[0] + nums[1]
    # else:
    #     result = nums[0] - nums[1]
    result = cmsd[op](*nums)

    prompt = '%s %s %s =' % (nums[0], op, nums[1])
    counter = 0

    while counter < 3 :
        try:
            answer = int(input(prompt))
         # except:     # 不填写异常, 可以捕获所有异常,不推荐
         #    print()
         #    continue
        except (ValueError,IndexError,UnboundLocalError):
            continue
        except (KeyboardInterrupt, EOFError):
            print('\033[31;1m\nSee you\033[0m')
            yn = 'n'
        else:
            if answer == result:
                print('\033[36;1mU r So Smart\033[0m')
                break

            print('\033[31;1mError,pls try again\033[0m')
            counter += 1
    else:
        print('\033[34;1m%s%s\033[0m' % (prompt,result))

def main():
    "调用出题函数,控制程序是否继续运行"
    while True:
        exam()
        # 将用户输入的两端空白字符删除,再取出第一个字符
        try:
            yn = input('\033[35;1mContinue(y/n)?\033[0m ').strip()[0]

        except IndexError:
            continue

        except (KeyboardInterrupt,EOFError):
            yn = 'n'

        if yn in 'nN':
            print('\033[32;1m\nSee you\033[0m')
            break



if __name__ == '__main__':
    main()









