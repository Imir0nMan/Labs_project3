from time import sleep

def check_inp(hour):
    if hour[0] >= 0:
        if 59 >= hour[1] >= 0:
            if 59 >= hour[2] >= 0:
                return True
            else:
                print("Invalid time format!!!")
                return False
        else:
            print("Invalid time format!!!")
            return False
    else:
        print("Invalid time format!!!")
        return False


def main():
    inp = input('Input time (h:m:s): ')
    try:
        hour = [int(inp[:inp.find(':')]), int(inp[inp.find(':')+1: inp.rfind(':')]), int(inp[inp.rfind(':')+1:])]
    except:
        print("Invalid format!!! ")
        return

    condition = check_inp(hour)
    while condition:
        if sum(hour) >= 0:
            if hour[2] == 0:
                if hour[1] == 0:
                    if hour[0] == 0:
                        break
                    else:
                        hour[0] -= 1
                        hour[1] = 59
                        hour[2] = 59
                else:
                    hour[1] -= 1
                    hour[2] = 59
            else:
                hour[2] -= 1
        else:
            print('invalid input')
        sleep(1)
        print(hour)


if __name__ == '__main__':
    main()