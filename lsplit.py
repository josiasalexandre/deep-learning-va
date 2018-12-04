import random
import glob
import os

def readLabels(source):
	labelsSet = set()

	for filename in glob.glob(source + '*.txt'):
		if os.path.isfile(filename.replace('txt', 'png')):
			labelsSet.add(filename);
	return labelsSet

def main:
	labelSet = set()
	for f in ['kitti', 'iara', 'cityscapes', 'udacity']:
		labelsSet.union(readLabels('/mnt/DADOS/dlva/datasets/' + f))
	labels = list(labelSet)
	for i in range(3):
		random.shuffle(labels)

	s = len(labels);
	s75 = int(s * 0.75)
	s15a = s75 + int(s * 0.15);
	s15b = s15a + int(s * 0.15);

	with open('training.txt', 'w') as file, open('testing.txt', 'w') as gile, open('validation.txt', 'w') as hile:
		file.write("\n".join(s[0:s75]))
		gile.write("\n".join(s[s75:s15a]))
		hile.write("\n".join(s[s15b:]))

if __name__ == "__main__":
	main()
