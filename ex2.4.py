import timeit

vowels = "aeiouy"

def vowel_counter(word): 
    count = 0
    for char in word.lower():
        if char in vowels:
            count += 1
    return count

def word_counter(line): 
    return len(line.split())

def compute_average_vowels(lines):
    total_vowels = 0
    total_words = 0
    counting = False  

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
    return average_vowels

def main():
    # Read the file once (not timed)
    file_path = "C:/Users/ziadd/OneDrive/Desktop/338/lab_1_338/lab_data/pg2701.txt"
    with open(file_path, "r", encoding='utf-8') as file:
        lines = file.readlines()

    # Define the code to be timed
    def timed_code():
        compute_average_vowels(lines)

    # Use timeit to time the function
    repetitions = 100
    total_time = timeit.timeit(timed_code, number=repetitions)
    average_time = total_time / repetitions

    print(f"The average computation time over {repetitions} runs is {average_time:.6f} seconds.")

if __name__ == '__main__':
    main()
