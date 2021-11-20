with open("input.txt") as file:
    lines = file.read().splitlines()

hour = []
minutes = []
seconds = []
time = []

for line in lines:
    line = line.split(':')
    hour.append(line[0])
    minutes.append(line[1])
    seconds.append(line[2])

addH = int(hour[0]) + int(hour[1])
addM = int(minutes[0]) + int(minutes[1])
addS = int(seconds[0]) + int(seconds[1])

time.append(addH)
time.append(addM)
time.append(addS)
day = 0


while(time[2] >= 60):
    time[2] -= 60
    time[1] += 1

while(time[1] >= 60):
    time[1] -= 60
    time[0] += 1

while(time[0] >= 24):
    time[0] -= 24
    day += 1

if(time[0] < 10):
    time[0] = "0" + str(time[0])
if(time[1] < 10):
    time[1] = "0" + str(time[1])
if(time[2] < 10):
    time[2] = "0" + str(time[2])


finalStr = str(time[0]) + ":" + str(time[1]) + ":" + str(time[2]) + "+" + str(day) + " days."
print(finalStr)

f = open("output.txt", "w")
f.write(finalStr)
f.close()
