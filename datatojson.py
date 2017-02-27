import data
import json



translation = 'esv'
versecountsdict = {}
abbrsdict = {}

thedata = data.bible_data(translation=translation)
for book in thedata:
	bookname = book['name']
	abbrs = book['abbrs']
	
	#printtoscreen; for debug only
	#print(bookname)
	#print(book['abbrs'])
	#print(book['verse_counts'])

	#verse_counts to dict. 
	versecountsdict[bookname] = book['verse_counts']

	#abbr to dict. 
	for abbr in abbrs:
		abbrsdict[abbr] = bookname

	#addtojsonfile
with open(translation+'verse_counts.json', 'w') as outfile:
	json.dump(versecountsdict, outfile)
with open(translation+'abrs.json', 'w') as outfile:
	json.dump(abbrsdict, outfile)

	