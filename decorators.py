# def function1():
#     print("Hello")
#
# func2 = function1
# del function1
# func2()



# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return int
# a=funcret(0)
# print(a)

# def executor(func):
#     func("This")
#
# executor(print)


def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec
@dec1  #ye line ya to 34 line , both works same
def whoisak():
    print("Ashish is a a good boy")

# whoisak = dec1(whoisak)
whoisak()
