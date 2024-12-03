import random
import math

with open('adult.data', 'r') as f:
    input = []
    output = []
    for line in f:
        words = line.split(',')
        if len(words) > 9:
            male = 1
            if "F" in words[9]:
                male = 0
            input.append([float(words[0]),float(words[2]),float(words[4]),male,float(words[10]),float(words[11]),float(words[12])])
            mon = 1
            if "<" in words[14]:
                mon = 0
            output.append([mon])

for i in range(len(input[0])):
    mini = input[0][i]
    maxi = input[0][i]
    for j in range(len(input)):
        mini = min(input[j][i],mini)
        maxi = max(input[j][i],maxi)
    print(mini,maxi)
    for j in range(len(input)):
        input[j][i] = (input[j][i]-mini)/(maxi-mini)



def neural(m,h,n,num_hidden,bias,maxcycle,thresh,learn,input,output):
    weights = [[]]
    for i in range(m):
        weights[0].append([])
        for j in range(h):
            weights[0][i].append(random.random()*2-1)
    for i in range(num_hidden):
        weights.append([])
        for j in range(h):
            weights[i+1].append([])
            for k in range(h):
                weights[i+1][j].append(random.random()*2-1)
    weights.append([])
    print(len(weights),num_hidden)
    for i in range(h):
        weights[num_hidden+1].append([])
        
        for j in range(n):
            weights[num_hidden+1][i].append(random.random()*2-1)
    
    for cycle in range(maxcycle):
        avg_error = 0
        for d in range(len(input)):
            activations = [input[d]]
            for i in range(len(weights)):
                activations.append([0]*len(weights[i][0]))
                for j in range(len(weights[i])):
                    for k in range(len(weights[i][j])):
                        activations[i+1][k] += activations[i][j]*weights[i][j][k]
                for j in range(len(activations[i+1])):
                    activations[i + 1][j] = 1 / (1 + math.exp(-activations[i+1][j]-bias))

            errors = [0]*len(output[d])
            deltas = [0]*len(output[d])
            total_error = 0
            for i in range(len(errors)):
                errors[i] = (output[d][i] - activations[-1][i])
                total_error += errors[i]**2
                deltas[i] = errors[i] * activations[-1][i] * (1-activations[-1][i])
            avg_error += total_error

            for i in reversed(range(len(weights))):
                new_deltas = []
                for j in range(len(weights[i])):
                    error = 0
                    for k in range(len(deltas)):
                        error += deltas[k] * weights[i][j][k]
                    new_deltas.append(error * activations[i][j] * (1-activations[i][j]))

                    for k in range(len(weights[i][j])):
                        weights[i][j][k] += learn * deltas[k] * activations[i][j]

                deltas = new_deltas
        avg_error = avg_error/len(input)
        if avg_error < thresh:
            print(f"Training complete at cycle {cycle}, total error: {avg_error:.4f}")
            break
        else:
            print(f"Cycle {cycle}, total error: {avg_error:.4f}")



neural(7, 10, 1, 5, -0.5, 10000, 0.001, 0.1, input, output)

