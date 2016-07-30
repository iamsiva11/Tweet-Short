from collections import OrderedDict
import re

text="Learn the basics of web design"

#removes vowels except if first character is a vowel
def put_in_a_list(sentence):  
	
	words=sentence.split()
	words = [w.replace('e', '').replace('a','').replace('i','').
	replace('o','').replace('u','') if (w[0] not in ['a','e','i','o','u'])
	else w[:1]+w[1:].replace('e', '').replace('a','').replace('i','').
	replace('o','').replace('u','') for w in words]
	return words

def remove_rep_consonants(words):
	
	#Removing repeated Consonants
	words=[	re.sub(r'(\w)\1+', r'\1', e ) for e in words]
	rep_consonants_removed =' '.join(map(str, words))
	return rep_consonants_removed

print remove_rep_consonants(put_in_a_list(text))