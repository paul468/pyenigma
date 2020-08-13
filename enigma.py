abc = "abcdefghijklmnopqrstuvwxyz"
rolle1 = abc

endrolle = True
word = input()

rollingindex1 = int(input("Einstellung des ersten Rades: "))
rollingindex2 = int(input("Einstellung des zweiten Rades: "))
rollingindex3 = int(input("Einstellung des dritten Rades: "))
def enigma(word):
	global rollingindex1, rollingindex2,rollingindex3
	word2 = ""		
	for letter in word.lower():
		if endrolle:	
			letter = rolkod(rolle1,rollingindex1,letter)
			letter = rolkod(rolle1,rollingindex2,letter)
			letter = rolkod(rolle1,rollingindex3,letter)
		elif endrolle != True:
			letter = rolkod(rolle1,rollingindex3 * -1,letter)
			letter = rolkod(rolle1,rollingindex2 * -1,letter)
			letter = rolkod(rolle1,rollingindex1 * -1,letter)
		word2 += letter
		rollingindex1+=1
		if rollingindex1 > 25:
			rollingindex1 = 0
			rollingindex2 += 1
		if rollingindex2 > 25:
			rollingindex2 = 0
			rollingindex3 += 1
		if rollingindex3 > 25:
			rollingindex3 = 0
	return word2
def rolkod(rolle, status, letter):
	letter = abc.index(letter)
	index = letter + status
	if index > 25:
		index = index % 26
	elif index < 0:
		index = index % 26
	out = rolle[index]
	return out
test = enigma(word)
print(test)
rollingindex1=1
rollingindex2=1
rollingindex3=1
endrolle = False
test2 = enigma(input())
print(test2)
