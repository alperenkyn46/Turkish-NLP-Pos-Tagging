import os
def load_conllu(filePath):
    word_data = {}
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split("\t")
                if len(parts) == 10:  # sütun sayısı
                    word = parts[1].lower()
                    upos = parts[3]
                    morph = parts[5]  #
                    word_data[word] = (upos, morph)
        return word_data
    except FileNotFoundError:
        print(f"HATA: {filePath} dosyası bulunamadı!")
        return {}
filePath = "tr_boun-ud-test.conllu"
word_data = load_conllu(filePath) #kelimeler

sentence = input("Türkçe bir cümle yazın: ")
words = sentence.split()

print("\nKelime Türü ve Morfolojik Analiz:")
for word in words:
    word_lower = word.lower()
    if word_lower in word_data:
        upos, morph = word_data[word_lower]
        print(f"Kelime: {word}")
        print(f"  - Kelime Türü (UPOS): {upos}")
    else:
        print(f"Kelime: {word} (Bilinmiyor)")
    print()
