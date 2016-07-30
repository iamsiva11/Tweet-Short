from collections import OrderedDict
import re

#Text to shorten
#tweets="I have successfully ordered my food today"
text="Thank you for have successfully ordered your purchase.Thank you fro choosing us"

#removes vowels except if first character is a vowel
def put_in_a_list(sentence):  
	words=sentence.split()
	#print words
	words = [w.replace('e', '').replace('a','').replace('i','').\
	replace('o','').replace('u','') if (w[0] not in ['a','e','i','o','u'])\
	else w[:1]+w[1:].replace('e', '').replace('a','').replace('i','').
	replace('o','').replace('u','') for w in words]
	return words

def remove_rep_consonants(words):
	#Rempving repeated Consonants
	words=[	re.sub(r'(\w)\1+', r'\1', e ) for e in words]
	#print '%s ' % ' '.join(map(str, words))#print "%s" % words
	rep_consonants_removed =' '.join(map(str, words))#print "%s" % words
	return rep_consonants_removed

print remove_rep_consonants(put_in_a_list(text))


# Coded this up for a project in Compliers course.

# Provides a shortened version of the text in cases.
# where letter constraints are involved - for instance, twitter. 

