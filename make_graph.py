import matplotlib.pyplot as plt

f=open("info.txt",'r')

lines=f.readlines()

x=[]
y=[]

for i in range(len(lines)):
    if (i%2==0):
        x.append(lines[i])
    else:
        y.append(int(lines[i]))

plt.plot(x,y)
plt.title('Number of vehicles over time')
plt.xlabel('Time')
plt.ylabel('Number of vehicles')
plt.gca().axes.xaxis.set_visible(False)
plt.grid(True)
plt.show()