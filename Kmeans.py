import random
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def kmeans(data, bound, seeds, iterations,reseed):
    centroids = []
    for i in range(seeds):
        centroids.append([0,0])
        rand = int(random.random()*len(data))
        centroids[i][0] = data[rand][0]
        centroids[i][1] = data[rand][1]
    print(centroids)
    for i in range(iterations):
        for j in range(len(centroids)):
            total_x = 0
            total_y = 0
            amount = 0
            for k in range(len(data)):
                if ((data[k][0]-centroids[j][0])**2+(data[k][1]-centroids[j][1])**2)**.5 < bound:
                    total_x = total_x + data[k][0]
                    total_y = total_y + data[k][1]
                    amount += 1
            centroids[j][0] = total_x/amount
            centroids[j][1] = total_y/amount
        overlap = False
        iter = 0
        while not overlap and iter < reseed:
            overlap = True
            j=0
            while j < len(centroids):
                k = len(centroids)-1
                while k > j:
                    if ((centroids[j][0]-centroids[k][0])**2+(centroids[j][1]-centroids[k][1])**2)**.5 < 2*bound:
                        if i == iterations-1:
                            centroids.pop(k)
                        else:
                            rand = int(random.random()*len(data))
                            centroids[k][0] = data[rand][0]
                            centroids[k][1] = data[rand][1]
                        overlap = False
                    k -= 1
                j += 1
            iter += 1

        print("ITERATION ",i+1)
        for i in centroids:
            cluster = []
            for j in data:
                if ((j[0]-i[0])**2+(j[1]-i[1])**2)**.5 < bound:
                    cluster.append([j[0],j[1]])
            print(f"Cluster ({i[0]},{i[1]}): {cluster}")
    print("ITERATION DONE")
    col = 0
    xs = []
    ys = []
    cs = []
    for i in centroids:
        cluster = []
        for j in reversed(range(len(data))):
            if ((data[j][0]-i[0])**2+(data[j][1]-i[1])**2)**.5 < bound:
                cluster.append([data[j][0],data[j][1]])
                xs.append(data[j][0])
                ys.append(data[j][1])
                cs.append(col)
                data.pop(j)
        col += 1/len(centroids)

    for i in data:
        xs.append(i[0])
        ys.append(i[1])
        cs.append(1)

    
    print(f"Cluster ({i[0]},{i[1]}): {cluster}")
    print(f"Outliers: {data}")
    fig, ax = plt.subplots(1)
    ax.plot(xs,ys, "ro")
    
    ax.set_aspect("equal")
    for i in centroids:
        circ = Circle((i[0],i[1]),bound,fill=False)
        ax.add_artist(circ)
    plt.savefig("out.png")

data = []
option = ""
while option != "d" and option != "f" and option != "r":
    option = input("will you be entering a file (f), data manually (d), or random values (r): ")
if option == "f":
    file_name = input("enter data file name: ")
    with open(file_name, 'r') as f:
        for line in f:
            words = line.split(',')
            data.append([float(words[0]),float(words[1])])
elif option == "d":
    nums = ""
    while nums != "done":
        nums = input("Input comma separated coordinates, or done when finished: ")
        try:
            if nums != "done":
                words = nums.split(",")
                data.append([float(words[0]),float(words[1])])
        except:
            print("invalid input")
else:
    states = -1
    while states < 1:
        option = input("how many points are there: ")
        try:
            states = int(option)
        except:
            print("not valid")
    while len(data) < states:
        data.append([random.random()*100,random.random()*100])
print("data points: ",data)

bounds = float(input("what is the radius of the clusters: "))
seeds = int(input("how many seed points: "))
iterations = int(input("how many iterations: "))
rese = int(input("how many times should I reseed: "))

kmeans(data,bounds,seeds,iterations,rese)