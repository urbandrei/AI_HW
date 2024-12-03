def linreg(data, inp):
    avg_x = 0
    avg_y = 0
    for i in data:
        avg_x += i[0]
        avg_y += i[1]
    avg_x = avg_x/len(data)
    avg_y = avg_y/len(data)

    sd_x = 0
    sd_y = 0
    for i in data:
        sd_x += (i[0]-avg_x)**2
        sd_y += (i[1]-avg_y)**2
    sd_x = (sd_x/(len(data)-1))**.5
    sd_y = (sd_y/(len(data)-1))**.5

    cov=0
    for i in data:
        cov += (i[0]-avg_x)*(i[1]-avg_y)
    cov = (cov/(len(data)-1))

    r = cov/(sd_x*sd_y)

    a = r*sd_y/sd_x
    b = avg_y-a*avg_x

    print("Slope:",a)
    print("Intercept:",b)
    print("Prediction:",a*inp+b)

data = []
option = ""
while option != "d" and option != "f":
    option = input("will you be entering a file (f) or data manually (d): ")
if option == "f":
    file_name = input("enter data file name: ")
    with open(file_name, 'r') as f:
        for line in f:
            words = line.split(',')
            data.append([float(words[0]),float(words[1])])
else:
    nums = ""
    while nums != "done":
        nums = input("enter comma separated values, or (done) if finished: ")
        try:
            if nums != "done":
                words = nums.split(',')
                data.append([float(words[0]),float(words[1])])
        except:
            print("the values you entered were not formatted correctly")
x = input("enter independent variable: ")



linreg(data,2)