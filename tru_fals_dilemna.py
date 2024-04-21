
def func1(given_num):
    if given_num%3==0:
        return True
    # if given_num%5==0:
    #     return False

if __name__ == "__main__":
    for i in range(0,10):
        var1 = func1(i)
        if var1:
            # print(f"num is {i} and it is True")
            print(f"num is {i} and it is {var1}")
        else:
            # print(f"num is {i} and it is False or None")
            print(f"num is {i} and it is {var1}")
        # if not func1(i):
        #     print(f"num is {i} and it is False")
    