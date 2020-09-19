import time

#string of votes
sortedvotes2 = ''
#for counting how much time the script ran
start_time = time.time()

#votes dictionary
votes = {
'8-Ball':247,
'Balloony':99,
'Barf Bag':69,
'Basketball':114,
'Bell':189,
'Black Hole':74,
'Blocky':87,
'Bomby':86,
'Book':109,
'Bottle':122,
'Bracelety':139,
'Bubble':93,
'Cake':169,
'Clock':122,
'Cloudy':92,
'Coiny':68,
'David':253,
'Donut':85,
'Dora':169,
'Eggy':285,
'Eraser':94,
'Fanny':176,
'Firey':110,
'Firey Jr':262,
'Flower':141,
'Foldy':234,
'Fries':120,
'Gaty':95,
'Gelatin':63,
'Golfball':99,
'Grassy':141,
'Icecube':121,
'Leafy':111,
'Lightning':70,
'Liy':147,
'Lollipop':115,
'Loser':196,
'Marker':93,
'Match':182,
'Naily':94,
'Needle':86,
'Nickel':77,
'Pen':68,
'Pencil':233,
'Pie':100,
'Pillow':196,
'Pin':56,
'Puffball':140,
'Remote':104,
'Robot Flower':171,
'Roboty':263,
'Rocky':140,
'Ruby':52,
'Saw':65,
'Snowball':174,
'Spongy':210,
'Stapy':185,
'Taco':74,
'Teardrop':58,
'Tennis Ball':61,
'Tree':83,
'TV':209,
'Woody':162,
'Yellow Face':154
}

#sorting the votes
sortedvotes = sorted(votes.items(), key=lambda x: x[1], reverse = True)
#opening the file to sort votes
votesfile = open('votes.txt', 'a')

#write votes in file
for i in sortedvotes:
    sortedvotes2 = sortedvotes2 + f'{i[0]}: {i[1]}\n'
    with open('votes.txt', 'w') as votesfile:
        votesfile.write(sortedvotes2)
        
#print the running time and pause the script
print(f'Done in {time.time() - start_time} seconds')
input()