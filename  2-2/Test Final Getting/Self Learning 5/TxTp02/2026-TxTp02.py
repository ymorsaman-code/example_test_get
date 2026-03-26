# getting news
path_news = '/Users/mac/Library/Mobile Documents/com~apple~TextEdit/Documents/NEWS.txt'
with open(path_news, "r", encoding = "UTF-8") as f_news :
    news_thai = f_news.read()

#print(news_thai)

#------------------------------------------
# cut word
from pythainlp.tokenize import word_tokenize


cuted_word = word_tokenize(news_thai, engine = "newmm", keep_whitespace=False)
#print(cuted_word)


#------------------------------------------
# clean word
remove = [' ', '\n' , '.', "\u2028", ""]

clean_word  = []

for value in cuted_word:
    if value not in remove:
        clean_word.append(value)
        
#print(clean_word)

#------------------------------------------
# count_word
from collections import Counter

word_count = Counter(clean_word)

#------------------------------------------
# rank max freq
rank_Freq = word_count.most_common()

#------------------------------------------
# show ( word : count ) 
show_w_c = [f" {word} : {count}" for word, count in rank_Freq]
#print(show_w_c)


#------------------------------------------
# ขึ้นบรรทัดใหม่

# \n เพื่อขึ้นบรรทัดใหม่
output_enter = "\n".join(show_w_c)

# print(output_enter)

#------------------------------------------
# save file
path_output = "/Users/mac/Library/Mobile Documents/com~apple~TextEdit/Documents/Count.txt"

with open(path_output, "w", encoding = "UTF-8") as f_save :
    f_save.write(output_enter)

print("save แน่วววว")




