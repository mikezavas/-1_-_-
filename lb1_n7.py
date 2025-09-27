#7
text = """
    Python is a powerful programming language. 
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""
t = text.strip().lower()
t = t.replace("!", ".")
sentences = [s.strip() for s in t.split(".") if s.strip()]
print("Предложения:", sentences)
first = sentences[0]
words = first.split()
print("Слова первого предложения:", words)
print("Кол-во 'python':", words.count("python"))
print("startswith('python'):", first.startswith("python"))
print("endswith('language'):", first.endswith("language"))
print("Общее кол-во символов:", len(t))
print("Кол-во букв 'a':", t.count("a"))
print("Индекс слова 'data':", t.find("data"))

words_all = t.split()
print("Через '-':", "-".join(words_all))
freq = {}

freq = {}
for w in words_all:
    freq[w] = freq.get(w, 0) + 1
print("Частоты слов:", freq)
import string
def clean_text(txt):
    txt = txt.lower().strip()
    allowed = string.ascii_lowercase + " "
    cleaned = "".join(ch if ch in allowed else " " for ch in txt)
    return " ".join(cleaned.split())

print("Очищенный текст:", clean_text(text))




