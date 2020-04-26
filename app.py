from components import Components

#Main
comp = Components()
x = "99"
count = 0
#c
compcounts = {
    "Server" : 0,
    "SAN" : 0,
    "Switch" : 0,
    "WAP" : 0,
    "Application" : 0

}
#l
initialprint = {
    "1" : "Server",
    "2" : "SAN",
    "3" : "Switch",
    "4" : "WAP",
    "5" : "Application",
    "0" : "Exit"
}
#f
funclist = {
    "Server" : comp.Server,
    "SAN" : comp.SAN,
    "Switch" : comp.Switch,
    "WAP" : comp.WAP,
    "Application" : comp.Application,
}

#W
finalcounts = {
    "Rack Space" : 0,
    "LAN Ports" : 0,
    "iSCSI Ports" : 0,
    "Cat6 Cables" : 0,
    "SFP Modules" : 0,
    "DAC Cables" : 0,
    "WAP" : 0,
    "Labor" : 0
}

#Gather Large Component Counts
while (x != "0"):
    for y,z in initialprint.items():
        print(y,z)
    x = input("Component: ")
    if (x == "0"):
        continue
    else:
        compcounts[initialprint[x]] += 1

#Print to confirm large component counts
for y,z in compcounts.items():
    print(y, z)

'''
    Loop through compcounts to call the associated component function
    For each large component, gather associated small components
    Add small component counts back to finalcounts dict
'''
for y,z in compcounts.items():
    if (z == 0):
        continue
    else:
        tempct = 0
        while(tempct < z):
            d = funclist[y]()
            for a,b in d.items():
                finalcounts[a] += int(b)
            tempct+=1

#Combine iSCSI over Cat6 and LAN Port counts for Cat6 Cable
finalcounts['Cat6 Cables'] += finalcounts['LAN Ports']

#Print finalcounts
print("###Final Counts###")
for y,z in finalcounts.items():
    if (z == 0):
        continue
    else:
        print(y,z)
