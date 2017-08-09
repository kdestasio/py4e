# Many counters with a dictionary

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqain', 'cwen']
for name in names :
	if name not in counts :
		counts[name] = 1
	else :
		counts[name] = counts[name] + 1
print(counts)