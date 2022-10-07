# f=open("ashish.txt","a")
# a=f.write("Subhash kumar\n")
# print(a)
# f.close()



# f=open("ashish2.txt","w")
# a=f.write("Subhash kumar\n")
# print(a)
# f.close()

# Handle read and write both

f=open("ashish2.txt","r+")
print(f.read())
f.write("Thank you")

f.close()