data = [[5,3,3,4],[6,2,5,8],[8,3,4,5],[3,1,2,4],[6,2,4,9],[7,5,6,1],[4,4,5,3],[6,3,7,4],[2,5,8,4],[7,7,2,5]]

for i in range(len(data)):
    one = -1
    mini = 10
    for j in range(len(data)):
        if i != j:
            dist = ((data[i][0]-data[j][0])**2+(data[i][1]-data[j][1])**2+(data[i][2]-data[j][2])**2+(data[i][3]-data[j][3])**2)**.5
            if dist < mini:
                mini = dist
                one = j
    print(data[i])
    print(data[one])
    print(mini)
