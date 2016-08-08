from __future__ import division
from collections import OrderedDict
import re
import nltk

#Test Strings
text="Learn the basics of web design"
text2="""Clashes broke out between protesters and security forces in Anantnag
and Shopian districts of south Kashmir."""

#removes vowels except if first character is a vowel
def put_in_a_list(sentence):  
	
	words=sentence.split()
	#remove vowels , if they are not the first characters in the string
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

def getme_proper_Nouns(text_data):
	
	tokenised_text = nltk.word_tokenize(text_data)
	#text/sentence.split()
	tagged_set = nltk.pos_tag(tokenised_text)
	propernouns = [word for word,pos in tagged_set if pos == 'NNP']
	return propernouns

def words_compressed_stat(text2):
	orginal_str=text2
	result_str = remove_rep_consonants(put_in_a_list(text2))
	num = 1-(len(result_str)/len(orginal_str))
	print "Compressed String by ", int(num*100) ,"percent"

print remove_rep_consonants(put_in_a_list(text2))
print words_compressed_stat(text2)











