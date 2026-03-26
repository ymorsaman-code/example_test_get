# get file text 

path_songTH = "/Users/mac/Downloads/songTH.txt"

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


songEN = [ romanize(word_cut, engine = "royin") for word_cut in cuted_word]
print(songEN)

#-----------------------------------------------
# list to long string
long_sting = " ".join(songEN)
print(long_sting)

#-----------------------------------------------
# save file
path_output = "/Users/mac/Downloads/songEN.txt"

with open(path_output, "w", encoding = "UTF-8") as f_save :
            f_save.write(long_sting)

print("save file : songEN finish")
