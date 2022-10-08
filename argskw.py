def function_name_print(a,b,c,d):
    print(a,b,c,d)

def funargs(normal ,*args,**kwarkgs):
    print(normal)

    for item in args:
        print(item)
    print("Now i would like to introduce some of our heroes")
    for key,value in kwarkgs.items():
        print(f"{key} is a {value}")
# function_name_print("Ashish","Aklesh","Prabhakar","Prince")

ak = ["Ashish","Aklesh","Prabhakar","Prince"]
normal = "I am a normal argument"
kw = {"Rohan":"Monitor","Ashish":"Programmer","Akesh":"flutter developer"}
funargs(normal,*ak,**kw)