colors=input("enter comma seperater color names:").split(",")
colors=[color.strip() for color in colors]
print("first color:",colors[0]) 
print("last color:",colors[-1])
