from __future__ import division
from collections import OrderedDict
import re
#import nltk
import sys

#Test Strings
text="Learn the basics of web design"
text2="""Clashes broke out between protesters and security forces in Anantnag
and Shopian districts of south Kashmir."""

#removes vowels except if first character is a vowel
def put_in_a_list(sentence):  
	split_words=sentence.split()
	# #remove vowels , if they are not the first characters in the string
	# words = [w.replace('e', '').replace('a','').replace('i','').\
	# replace('o','').replace('u','') if (w[0] not in ['a','e','i','o','u'])\
	# else w[:1]+w[1:].replace('e', '').replace('a','').replace('i','').\
	# replace('o','').replace('u','') for w in words]
	return split_words

def remove_vowels(split_words):
	#remove vowels , if they are not the first characters in the string
	removed_words = [w.replace('e', '').replace('a','').replace('i','').\
	replace('o','').replace('u','') if (w[0] not in ['a','e','i','o','u'])\
	else w[:1]+w[1:].replace('e', '').replace('a','').replace('i','').\
	replace('o','').replace('u','') for w in split_words]
	return removed_words	

#Removing repeated Consonants
def remove_rep_consonants(words):
	words=[	re.sub(r'(\w)\1+', r'\1', e ) for e in words]
	rep_consonants_removed =' '.join(map(str, words))
	return rep_consonants_removed

def getme_proper_Nouns(text_data):
	tokenised_text = nltk.word_tokenize(text_data)
	tagged_set = nltk.pos_tag(tokenised_text)
	propernouns = [word for word,pos in tagged_set if pos == 'NNP']
	return propernouns

def words_compressed_stat(text2):
	orginal_str=text2
	result_str=Do_shorten(text)
	#result_str = remove_rep_consonants(put_in_a_list(text2))
	num = 1-(len(result_str)/len(orginal_str))
	#print len(result_str),len(orginal_str)
	print "Compressed the text by", int(num*100) ,"percent"

def get_small_words_index(words_list):
	#skip words that
	lessthan3=[]
  	for i in range(len(words_list)):
  		if len(words_list[i])<=3:
  			lessthan3.append(i)
  	return lessthan3		
	#if (len(text))

# def skip_small_words(words_list):
# 	small_index = get_small_words_index(words_list)
# 	print small_index
# 	new_list=[]

# 	for i in range(len(words_list)):
# 		if i not in small_index:
# 			new_list.append(words_list[i])
# 		# 	pass#continue
# 		# else:
# 	return new_list		
				
def Do_shorten(text):
	list_of_words = put_in_a_list(text)
	#debug
	#print get_small_words_index(list_of_words)
	list_after_vowels_removed = remove_vowels(list_of_words)
	result = remove_rep_consonants(list_after_vowels_removed)	
	return result

#print skip_small_words(Do_shorten(sys.argv[1]))

#print remove_rep_consonants(put_in_a_list(text2))
#words_compressed_stat(text2)
#print remove_rep_consonants(put_in_a_list(sys.argv[1]))

print Do_shorten(sys.argv[1])
words_compressed_stat(sys.argv[1])

#print getme_proper_Nouns(sys.argv[1])


#Two roads diverged in a yellow wood,
# And sorry I could not travel both
# And be one traveler, long I stood
# And looked down one as far as I could
# To where it bent in the undergrowth;
