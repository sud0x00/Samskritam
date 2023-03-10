def get_vowels_diacritics(word):
  
    vowels = ['अ','आ', 'इ','ई', 'उ','ऊ', 'ऋ','ॠ', 'ऌ','ॡ', 'ए', 'ऐ', 'ओ', 'औ', 'अं', 'अः']
    #इन्द्र or सिन्धु
    
    
    diacritics = ['','ा','ि','ी', 'ु', 'ू', 'ृ','ॄ',' ॢ',' ॣ','े', 'ै','ो', 'ौ',' ं',' ः']
   
    #  अंशः -> Anusvara & Visarga aren't working 
    
    #  मातृ not working , error with single char लृ -> Need to fix ru , ruu , lru , lruu
    
    
    consonants = ['क', 'ख', 'ग', 'घ', 'ङ','च', 'छ', 'ज', 'झ', 'ञ','ट', 'ठ', 'ड', 'ढ', 'ण','त', 'थ', 'द', 'ध', 'न','प', 'फ', 'ब', 'भ', 'म','य', 'र', 'ल', 'व','श', 'ष', 'स', 'ह']
    first_vowel = None
    last_vowel = None
    for i in range(len(word)):
        print(word[i])
        # कवि or हरी or मही 
        
        if word[i] in consonants and word[i+1] in consonants: 
          first_vowel = "अ"
        if word[i] in vowels or word[i] in diacritics:
            if not first_vowel:
                first_vowel = word[i]
            last_vowel = word[i]
        else:
          last_vowel = "अ"
    return first_vowel, last_vowel
    
#  Remove  the below lines from the function when it's done
# 
#      

word = "राम"
first_vowel,last_vowel=get_vowels_diacritics(word.ljust(8,' ')) # reducing whitespaces results in string out of bounds error with complex words , ex - रुद्र

#first_vowel,last_vowel in function can be a diacritic as well,so we are assigning them corresponding vowel value in order to get corresponding sandhi
first_vowel,last_vowel=' '+first_vowel,' '+last_vowel
if first_vowel in diacritics:
    first_vowel=vowels[diacritics.index(first_vowel)]
if last_vowel in diacritics:
    last_vowel=vowels[diacritics.index(last_vowel)]
print(first_vowel,last_vowel)
