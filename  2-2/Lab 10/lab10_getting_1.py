import requests
from bs4 import BeautifulSoup
from collections import Counter
from pythainlp import word_tokenize

url = "https://www.sc.su.ac.th"

res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

text = soup.get_text()
print(text)

#------------------------------------------------
with open("result.txt", "w", encoding="utf-8") as f:
    f.write(text)

#------------------------------------------------
# Process: Tokenize and Count
words = word_tokenize(text, engine='newmm', keep_whitespace=False)
cleaned_words = [w for w in words if w.strip()]
word_counts = Counter(cleaned_words)

print("-" * 20)
print("Top 20 Frequent Words:")
for word, count in word_counts.most_common(20):
    print(f"{word}: {count}")