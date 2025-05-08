import string
import re

data ='''After World War II, the British greatly reduced the use of the full stop and other punctuation points after abbreviations in at least semi-formal writing, while the Americans more readily kept such use until more recently, and still maintain it more than Britons. The classic example, considered by their American counterparts quite curious, was the maintenance of the internal comma in a British organisation of secret agents called the "Special Operations, Executive", "S.O., E", which is not found in histories written after about 1960.
But before that, many Britons were more scrupulous at maintaining the French form. In French, the period only follows an abbreviation if the last letter in the abbreviation is not the last letter of its antecedent: "M." is the abbreviation for "monsieur" while "Mme" is that for "madame". Like many other cross-channel linguistic acquisitions, many Britons readily took this up and followed this rule themselves, while the Americans took a simpler rule and applied it rigorously.
Over the years, however, the lack of convention in some style guides has made it difficult to determine which two-word abbreviations should be abbreviated with periods and which should not. The U.S. media tend to use periods in two-word abbreviations like United States (U.S.), but not personal computer (PC) or television (TV). Many British publications have gradually done away with the use of periods in abbreviations.
Minimization of punctuation in typewritten material became economically desirable in the 1960s and 1970s for the many users of carbon-film ribbons since a period or comma consumed the same length of non-reusable expensive ribbon as did a capital letter.
Widespread use of electronic communication through mobile phones and the Internet during the 1990s allowed for a marked rise in colloquial abbreviation. This was due largely to increasing popularity of textual communication services such as instant- and text messaging. SMS, for instance, supports message lengths of 160 characters at most (using the GSM 03.38 character set). This brevity gave rise to an informal abbreviation scheme sometimes called Textese, with which 10% or more of the words in a typical SMS message are abbreviated. More recently Twitter, a popular social networking service, began driving abbreviation use with 140 character message limits.'''

words=re.findall(r'\w+|\?|\,|\!|\.|\"|\(|\)|\:|\S+', data)
print(words)



def stems(word):
   word= re.sub(r'sses$', 'ss', word)
   word= re.sub(r'ies$', 'i', word) 
   word= re.sub(r'ss$', 'ss', word) 
   word= re.sub(r's$', '', word) 
   word= re.sub(r'eed$', 'ee', word) 
   word= re.sub(r'ed$', '', word) 
   word= re.sub(r'ing$', '', word)
   word= re.sub(r'less$', '', word) 
   word= re.sub(r'ship$', '', word) 
   word= re.sub(r'ing$', '', word) 
   word= re.sub(r'les$', '', word) 
   word= re.sub(r'ly$', '', word) 
   word= re.sub(r'es$', '', word)
   word= re.sub(r'ful$', '', word)
   word= re.sub(r'ness$', '', word) 
   word= re.sub(r'alize$', 'al', word)
   word= re.sub(r'tional$', 'tion', word)
   word= re.sub(r'tion$', '', word)
   word= re.sub(r'an$', '', word)
   word= re.sub(r'ational$', 'ate', word)
   word= re.sub(r'izer$', 'ize', word)
   word= re.sub(r'ator$', 'ate', word)
   word= re.sub(r'al$', '', word)
   word= re.sub(r'able$', '', word)
   word= re.sub(r'ate$', '', word)
   word= re.sub(r'tive$', '', word)
   return word

words= " ".join([stems(word) for word in words])
print(words)





words=words.lower()

words = re.sub(r'[!:,()".;\'?]', '', words)

words=re.sub(r'\ba\b\s+',"",words)
words=re.sub(r'\bthe\b\s+',"",words)
words=re.sub(r'\bor\b\s+',"",words)
words=re.sub(r'\bin\b\s+',"",words)
words=re.sub(r'\bto\b\s+',"",words)
words=re.sub(r'\bfrom\b\s+',"",words)
words=re.sub(r'\ball\b\s+',"",words)
words=re.sub(r'\bis\b\s+',"",words)
words=re.sub(r'\bam\b\s+',"",words)
words=re.sub(r'\ban\b\s+',"",words)
words=re.sub(r'\bare\b\s+',"",words)
words=re.sub(r'\bas\b\s+',"",words)
words=re.sub(r'\bin\b\s+',"",words)
words=re.sub(r'\bat\b\s+',"",words)
words=re.sub(r'\bbe\b\s+',"",words)
words=re.sub(r'\bdid\b\s+',"",words)
words=re.sub(r'\bdo\b\s+',"",words)
words=re.sub(r'\bthat\b\s+',"",words)
words=re.sub(r'\bthis\b\s+',"",words)
words=re.sub(r'\bar\b\s+',"",words)
words=re.sub(r'\bi\b\s+',"",words)
words=re.sub(r'\bof\b\s+',"",words)
words=re.sub(r'\band\b\s+',"",words)
words=re.sub(r'\bit\b\s+',"",words)
words=re.sub(r'\babout\b\s+',"",words)
words=re.sub(r'\bother\b\s+',"",words)
words=re.sub(r'\bfor\b\s+',"",words)
words=re.sub(r'\bhas\b\s+',"",words)

words=re.sub(r'\bs  o   e\b\s+'," Special Operations, Executive ",words)
words=re.sub(r'\bu  s\b\s+'," united state ",words)
words=re.sub(r'\bm\b\s+'," monsieur",words)
words=re.sub(r'\bmme\b\s+'," madame ",words)
words=re.sub(r'\bpc\b\s+'," personal computer ",words)
words=re.sub(r'tv\b\s+'," television ",words)


words=re.sub(r'\b\d+\b', '', words)

words = re.sub(r'\s+', ' ', words)
print(words)