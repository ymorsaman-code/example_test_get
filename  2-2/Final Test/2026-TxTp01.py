# get file text 

path_songTH = r"C:\Users\admin\OneDrive - Silpakorn University\DS_learning\songTH.txt"

with open(path_songTH, "r", encoding = "UTF-8") as f :
    songTH = f.read()

#print(songTH)

#-----------------------------------------------
# cut word
from pythainlp.tokenize import word_tokenize

cuted_word = word_tokenize(songTH, engine="newmm")
#print(cuted_word)

#-----------------------------------------------
# thai to english
from pythainlp.transliterate import romanize


songEN = [ romanize(word_cut, engine="royin") for word_cut in cuted_word]
print(songEN)

#
