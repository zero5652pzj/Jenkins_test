#This is Jenkins test documents

file = "e:/sanwen.txt"

def document(filepath):
	with open(filepath, 'r') as f:
		for _ in range(30):
			text = f.readline()
			yield text

print("Begin!!")
doc = document(file)
words = 'Treat the image'
for _ in range(30):
	texts = next(doc)
	if words in texts:
		print(texts)
