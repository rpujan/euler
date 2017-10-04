inital = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
cal = []
final = []
for i in range(1,21):
  #print(inital)
  cal.append(1)
  for j in range(1,21):
    cal.append(cal[j-1] + inital[j])
  print(cal)
  inital = cal
  cal = []
