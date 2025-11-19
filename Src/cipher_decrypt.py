"""
cipher_decrypt.py

Decrypts text encrypted with a Caesar cipher by analyzing letter frequency.
Generates frequency plots and suggests possible shifts for decryption.
Input can be provided via command line or by processing all .txt files in the 'Data' directory.
Outputs frequency plots to the 'Output' directory.
"""

import matplotlib.pyplot as plt
import sys
import os

"""Generate letter frequency plot by counting occurrences of each letter in the text."""
def plot_letter_frequency(text, filename="ciphertext"):
    # Initialize frequency dictionary
    frequency_dict = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
    # Count letter frequencies
    for char in text.upper():
        if char in frequency_dict:
            frequency_dict[char] += 1
    # Prepare data for plotting
    letters = list(frequency_dict.keys())
    frequencies = list(frequency_dict.values())

    output_path = 'Output'
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Plotting
    plt.bar(letters, frequencies)
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title(f'Letter Frequency: {filename}')
    # Save plot to Output directory
    plt.savefig(os.path.join(output_path, f'{filename}_frequency_plot.png')) 
    plt.close() # Important: Close the figure to free up memory and resources

    return frequency_dict

"""Suggest possible Caesar cipher shifts based on letter frequency analysis."""
def suggest_caesar_shifts(frequency_dict):
    # English letter frequency order
    english_freq_order = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
    # Sort letters by frequency in descending order
    sorted_letters = sorted(frequency_dict, key=frequency_dict.get, reverse=True)
    
    suggestions = []
    for i in range(5):  # Suggest top 5 possible shifts
        most_frequent_letter = sorted_letters[i]
        assumed_shift = (ord(most_frequent_letter) - ord(english_freq_order[0])) % 26
        suggestions.append((most_frequent_letter, assumed_shift))
    
    return suggestions

"""Decrypt text using a given Caesar cipher shift."""
def decrypt_caesar_cipher(text, shift):
    decrypted_text = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

if __name__ == "__main__":
    # Check for file input from command line
    if(len(sys.argv) > 1):
        filepath = sys.argv[1]
        if os.path.isfile(filepath):
            with open(filepath, 'r') as file:
                content = file.read()
            frequency_distribution = plot_letter_frequency(content, os.path.basename(filepath))
            suggestions = suggest_caesar_shifts(frequency_distribution)
            print("Possible Caesar cipher shifts based on letter frequency analysis:")
            for letter, shift in suggestions:
                decrypted_text = decrypt_caesar_cipher(content, shift)
                print(f"Decrypted text with shift {shift}:\n{decrypted_text}\n")
        else:
            print(f"File {filepath} does not exist.")
    # If no file provided, process all .txt files in 'Data' directory
    else:
        data_dir = 'Data'
        for filename in os.listdir(data_dir):
            if filename.endswith('.txt'):
                with open(os.path.join(data_dir, filename), 'r') as file:
                    content = file.read()
                frequency_distribution = plot_letter_frequency(content, filename)
                suggestions = suggest_caesar_shifts(frequency_distribution)
                print("Possible Caesar cipher shifts based on letter frequency analysis:")
                for letter, shift in suggestions:
                    decrypted_text = decrypt_caesar_cipher(content, shift)
                    print(f"Decrypted text with shift {shift}:\n{decrypted_text}\n")