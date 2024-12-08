import random

def hiddenmarkovmodel(initial, transition, signals, pattern):
    pos = [[[],1]]
    for i in range(len(pattern)):
        newpos = []
        for j in range(len(pos)):
            for k in range(len(initial)):
                prob = 1
                if i == 0:
                    prob = initial[k]*signals[k][pattern[i]]
                else:
                    prob = transition[pos[j][0][-1]][k]*signals[k][pattern[i]]
                if pos[j][1]*prob != 0:
                    newpos.append([pos[j][0]+[k],pos[j][1]*prob])
        pos = newpos
    return pos


states = -1
initial = []
transition = []
signal = []
pattern = []
option = ""
print("INITIAL PROBABILITIES")
while option != "d" and option != "f" and option != "r":
    option = input("will you be entering a file (f), data manually (d), or random values (r): ")
if option == "f":
    file_name = input("enter data file name: ")
    with open(file_name, 'r') as f:
        for line in f:
            words = line.split(',')
            states = len(words)
            for i in words:
                initial.append(float(i))
elif option == "d":
    while states < 1:
        option = input("how many states are there: ")
        try:
            states = int(option)
        except:
            print("not valid")
    while len(initial) < states:
        try:
            initial.append(float(input(f"enter the initial probability of state {(len(initial)+1)}: ")))
        except:
            print("not valid")
else:
    states = -1
    while states < 1:
        option = input("how many states are there: ")
        try:
            states = int(option)
        except:
            print("not valid")
    while len(initial) < states:
        initial.append(random.random())
print("initial probabilties: ",initial)
print("TRANSITION PROBABILITIES")
while option != "d" and option != "f" and option != "r":
    option = input("will you be entering a file (f), data manually (d), or random values (r): ")
if option == "f":
    file_name = input("enter data file name: ")
    with open(file_name, 'r') as f:
        for line in f:
            words = line.split(',')
            transition.append([])
            for i in words:
                transition[-1].append(float(i))
elif option == "d":
    for i in range(states):
        transition.append([])
        while len(transition[i]) < states:
            try:
                inp = input(f"enter probability from state {(i+1)} to {(len(transition[i])+1)}: ")
                transition[i].append(float(inp))
            except:
                print("not valid")
else:
    for i in range(states):
        transition.append([])
        for j in range(states):
            transition[i].append(random.random())
            
print("transition probabilties:")
for i in transition:
    print(i)
sigs = -1
option = ""
print("SIGNAL PROBABILITIES")
while option != "d" and option != "f" and option != "r":
    option = input("will you be entering a file (f), data manually (d), or random values (r): ")
if option == "f":
    file_name = input("enter data file name: ")
    with open(file_name, 'r') as f:
        for line in f:
            words = line.split(',')
            signal.append([])
            for i in words:
                signal[-1].append(float(i))
elif option == "d":
    sigs = -1
    while sigs < 1:
        option = input("how many signals are there: ")
        try:
            sigs = int(option)
        except:
            print("not valid")
    for i in range(states):
        signal.append([])
        while len(signal[i]) < sigs:
            try:
                signal[i].append(float(input(f"enter probability from state {(i+1)} to signal {(len(signal[i])+1)}: ")))
            except:
                print("not valid")
else:
    sigs = -1
    while sigs < 1:
        option = input("how many signals are there: ")
        try:
            sigs = int(option)
        except:
            print("not valid")
    for i in range(states):
        signal.append([])
        for j in range(sigs):
            signal[i].append(random.random())
            
print("signal probabilties:")
for i in signal:
    print(i)

print("SIGNAL SEQUENCE")
while len(pattern) == 0:
    seq = input("input signal sequence in comma separated values: ")
    try:
        words = seq.split(",")
        for i in words:
            pattern.append(int(i))
    except:
        print("invalid sequence")
option = ""
while option != "q":
    res = hiddenmarkovmodel(initial,transition,signal,pattern)
    mini = [res[0][0],res[0][1]]
    for i in res:
        if mini[1] > i[1]:
            mini[1] = i[1]
            mini[0] = i[0]
    
    print(res)
    print("Most probable path: ", mini[0])
    print("Probability: ",mini[1])
    option = input("would you like to change initial (i), transition (t), signal (s), pattern(p), or quit(q)")
    if option == "i":
        val = int(input("which state would you like to change: "))
        initial[val] = float(input("what is the new value: "))
        print("new initial vector:")
        print(initial)
    elif option == "t":
        vala = int(input("what is the start state: "))
        valb = int(input("what is the end state: "))
        transition[vala][valb] = float(input("what is the new value: "))
        print("new transition vector:")
        for i in transition:
            print(i)
    elif option == "s":
        vala = int(input("what is the state: "))
        valb = int(input("what is the signal: "))
        signal[vala][valb] = float(input("what is the new value: "))
        print("new signal vector:")
        for i in signal:
            print(i)
    elif option == "p":
        seq = input("input signal sequence in comma separated values: ")
        try:
            words = seq.split(",")
            for i in words:
                pattern.append(int(i))
        except:
            print("invalid sequence")