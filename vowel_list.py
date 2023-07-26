import sys

words = ['abstemious', 'luxury', 'onomotopiea', 'existence', 'death', 'Islam', 'president']

def vowel(words):
    vowels = 'aeiou'
    for word in words:
        v_ct = 0
        v_li = []
        for w in range(len(word)):
            if word[w].lower() in vowels:
                v_ct += 1
                v_li.append(word[w])
        print(f"There are {v_ct} vowels in {word}.")
        print(f"{word} = {list(set(v_li))}")

def main():
    return vowel(words)

if __name__ == "__main__":
    main()