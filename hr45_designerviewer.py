def designerPdfViewer(h, word):
	letters = 'abcdefghijklmnopqrstuvwxyz'
	hmap = {}
	for i in range(len(h)):
		hmap[letters[i]] = h[i]
	a = hmap[word[0]]
	for i in word:
		if hmap[i] > a:
			a = hmap[i]
	return a*len(word)




hh = []
h = input().split()
word = input()
for i in h:
	hh.append(int(i))
print(designerPdfViewer(hh,word))