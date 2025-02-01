vowels = "aeiouy"

def vowel_counter(word): 
    count = 0
    for char in word.lower():
        if char in vowels:
            count += 1
    return count


def word_counter(line): 
    return len(line.split())

def main():
    total_vowels = 0
    total_words = 0
    counting = False  

    file = open("C:/Users/ziadd/OneDrive/Desktop/338/lab_1_338/lab_data/pg2701.txt", "r", encoding='utf-8')
    lines = file.readlines()

    for line in lines:
        line = line.strip() 

        if "CHAPTER 1. Loomings." in line:
            counting = True  

        if not counting:
            continue

        words = line.split()
        for word in words:
            total_vowels += vowel_counter(word)  
        total_words += word_counter(line)  
        
    average_vowels = total_vowels / total_words if total_words > 0 else 0
    print("The average number of vowels per word is", average_vowels)

    file.close()

if __name__ == '__main__':
    main()