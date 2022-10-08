# l=5
# def function1(n):
#     # l=50
#     m=6
#     print(n,"I have printed")
#     global l
#     l=l+5
#     print(l,m)
#
# function1("This is me")
# # print(m)


x=89
def ashish():
    x=20
    def aklesh():
        global x
        x=88
    # print("Before calling aklesh",x)
    aklesh()
    print("After  calling aklesh",x)
ashish()
print(x)
