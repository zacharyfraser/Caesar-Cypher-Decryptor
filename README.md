# Caesar Cipher Decryptor

A Python-based tool that decrypts text encrypted with a Caesar cipher using statistical letter frequency analysis. This tool automatically analyzes encrypted text, generates frequency distribution plots, and suggests the most likely decryption shifts.

## Features

- **Automatic Decryption**: Analyzes letter frequency to suggest the most likely Caesar cipher shifts
- **Frequency Visualization**: Generates bar plots showing letter frequency distribution
- **Batch Processing**: Process multiple files at once from the Data directory
- **Command Line Support**: Process individual files via command line arguments
- **Top 5 Suggestions**: Provides the top 5 most likely decryption shifts based on English letter frequency

## Installation

1. Clone the repository:
```bash
git clone https://github.com/zacharyfraser/Caesar-Cypher-Decryptor.git
cd Caesar-Cypher-Decryptor
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Process all files in the Data directory

Simply run the script without arguments to process all `.txt` files in the `Data` directory:

```bash
python3 Src/cipher_decrypt.py
```

### Process a specific file

Provide a file path as a command line argument:

```bash
python3 Src/cipher_decrypt.py path/to/your/ciphertext.txt
```

### Example Output

```
Possible Caesar cipher shifts based on letter frequency analysis:
Decrypted text with shift 12:
This is a simple example of a caesar shifted code. You can 
solve it with a simple statistical analysis. The only 
requirement is often you need enough data for the analysis to 
become obvious.

Decrypted text with shift 0:
Ftue ue m euybxq qjmybxq ar m omqemd eturfqp oapq. Kag omz 
eaxhq uf iuft m euybxq efmfuefuomx mzmxkeue. Ftq azxk 
dqcgudqyqzf ue arfqz kag zqqp qzagst pmfm rad ftq mzmxkeue fa 
nqoayq anhuage.
...
```

## Project Structure

```
Caesar-Cypher-Decryptor/
├── Src/
│   └── cipher_decrypt.py    # Main decryption script
├── Data/
│   └── ciphertext.txt       # Sample encrypted text files
├── Output/                  # Generated frequency plots
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## How It Works

The Caesar cipher decryptor uses statistical analysis to crack encrypted text:

1. **Letter Frequency Analysis**: Counts the occurrence of each letter in the ciphertext
2. **Frequency Comparison**: Compares the frequency distribution with known English letter frequencies (E, T, A, O, I, N, S, H, R, D, L...)
3. **Shift Calculation**: Calculates the most likely Caesar cipher shifts based on the assumption that the most frequent letter in the ciphertext corresponds to common English letters
4. **Multiple Suggestions**: Provides the top 5 most likely decryption attempts
5. **Visualization**: Generates bar charts showing letter frequency distribution and saves them to the Output directory

## Requirements

- Python 3.x
- matplotlib

## License

This project is open source and available for educational purposes.
