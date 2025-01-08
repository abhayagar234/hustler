# Let's manually verify the letter counts for debugging purposes

############Problem statement 1 ############################


def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()

    # Count occurrences for each letter in "TRUE" and "LOVE"
    true_counts = {char: combined_names.count(char) for char in "true"}
    love_counts = {char: combined_names.count(char) for char in "love"}

    # Sum individual counts
    true_total = sum(true_counts.values())
    love_total = sum(love_counts.values())

    # Combine counts as a 2-digit number
    love_score = int(f"{true_total}{love_total}")
    print(love_score)


# Run debug to inspect individual counts
calculate_love_score("Kanye West", "Kim Kardashian")

############ Problem statement 2 ############################
alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

ecode_decode = input("You want to encode or decode \n").lower()
original_text = input(f"Enter the text you want to {ecode_decode} \n")
shift_number = int(input(f"Enter the number using which you want to shift \n"))


def encrypt(text, shift):
    cipher = ""
    for letter in text:
        shifted_position = alphabet.index(letter) + shift
        shifted_position %= len(alphabet)
        cipher += alphabet[shifted_position]
    print(cipher)


def decrypt(text, shift):
    cipher = ""
    for letter in text:
        shifted_position = alphabet.index(letter) - shift
        shifted_position %= len(alphabet)
        cipher += alphabet[shifted_position]
    print(cipher)


def ceaser(text, shift, ecode_decode):
    cipher = ""
    if ecode_decode == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift
            shifted_position %= len(alphabet)
            cipher += alphabet[shifted_position]
        else:
            cipher += letter
    print(cipher)


ceaser(original_text, shift_number, ecode_decode)


############ Problem statement 3 ############################


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num - 1):  # Check up to the square root of num
        if num % i == 0:
            return False  # Found a divisor, not prime
    return True  # No divisors found, prime


is_prime(75)
is_prime(17)
