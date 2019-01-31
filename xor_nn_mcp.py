from operator import add
w11 = int(input("Enter weight w11: "))
w12 = int(input("Enter weight w12: "))
w21 = int(input("Enter weight w21: "))
w22 = int(input("Enter weight w22: "))
v1 = int(input("Enter weight v1: "))
v2 = int(input("Enter weight v2: "))
theta = 2#int(input("Enter Threshold value, theta : "))
x1 = [0,0,1,1]
x2 = [0,1,0,1]
z = [0,1,1,0]
c = 1;
y1=[0,0,0,0]
y2=[0,0,0,0]
y=[0,0,0,0]
while(c):
    Zin1 = list( map(add,[x * w11 for x in x1], [x * w21 for x in x2]) )
    Zin2 = list( map(add,[x * w21 for x in x1], [x * w22 for x in x2]) )
    for i in range(4):
        if Zin1[i] >= theta:
            y1[i] = 1
        else:
            y1[i] = 0
        if Zin2[i] >= theta:
            y2[i] = 1
        else:
            y2[i] = 0
    Yin = list( map(add,[x * v1 for x in y1], [x * v2 for x in y2]) )
    for i in range(4):
        if Yin[i] >= theta :
            y[i] = 1
        else:
            y[i] = 0
    print("Output of the Neural network : ")
    print(y)
    if y == z :
        c = 0
    else:
        print("Output does not matches with expected value.")
        print("Enter another set of values")
        w11 = int(input("Enter weight w11: "))
        w12 = int(input("Enter weight w12: "))
        w21 = int(input("Enter weight w21: "))
        w22 = int(input("Enter weight w22: "))
        v1 = int(input("Enter weight v1: "))
        v2 = int(input("Enter weight v2: "))
        theta = int(input("Enter Threshold value, theta : "))
print("McCulloch Pitts NET for XOR fucntion implementation")
print("Weight of Neuron Z1 : " , w11 , " , " , w21)
print("Weight of Neuron Z2 : " , w12 , " , " , w22)
print("Weight of Neuron Y : " , v1 , " , " , v2)
print("Threshold value : ",theta)


        
