# DNA Translation Checker

A web-based application that validates DNA sequence translations by comparing translated amino acid sequences with expected results. This tool uses the standard genetic code to translate DNA codons into amino acids and provides an intuitive web interface for sequence validation.

## Features

- **Web-based Interface**: Clean, modern UI for easy sequence input and validation
- **Real-time Translation**: Instant DNA to amino acid translation using the standard genetic code
- **Visual Feedback**: Clear TRUE/FALSE results with color-coded responses
- **Error Handling**: Comprehensive validation with user-friendly error messages
- **Sequence Cleaning**: Automatically removes whitespace, newlines, and normalizes input
- **Detailed Results**: Shows comparison details and intermediate translation steps

## How It Works

1. Input your original DNA sequence and expected amino acid sequence
2. The application extracts a specific segment from the DNA sequence (positions 20-935)
3. Translates the DNA segment using the standard genetic code codon table
4. Compares the translated sequence with your expected amino acid sequence
5. Returns **TRUE** (in green) if sequences match, **FALSE** (in red) if they don't

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. **Clone or download the project files**:
   ```bash
   git clone <repository-url>
   cd dna-translation-checker
   ```

2. **Install required dependencies**:
   ```bash
   pip install flask flask-cors
   ```

3. **Create the project structure**:
   ```
   dna-translation-checker/
   ├── app.py
   ├── templates/
   │   └── ui.html
   └── README.md
   ```

4. **Place the files**:
   - Copy `app.py` to the root directory
   - Create a `templates` folder and place `ui.html` inside it

## Usage

### Starting the Application

1. **Run the Flask server**:
   ```bash
   python app.py
   ```

2. **Open your web browser** and navigate to:
   ```
   http://localhost:5000
   ```

### Using the Interface

1. **DNA Sequence Input**: Paste your DNA sequence in the first text area
   - Example: `ATGCGATCGATCGATCG...`
   - The application will use positions 20-935 of this sequence

2. **Amino Acid Sequence Input**: Paste your expected amino acid sequence in the second text area
   - Example: `MRFSLKQ...`
   - Use single-letter amino acid codes

3. **Submit**: Click the "Check Translation" button

4. **Results**: 
   - **TRUE** (green): The translated DNA matches your amino acid sequence
   - **FALSE** (red): The sequences don't match
   - Additional details show the actual translation and comparison

## Genetic Code Table

The application uses the standard genetic code for translation:

| Codon | Amino Acid | Codon | Amino Acid | Codon | Amino Acid | Codon | Amino Acid |
|-------|------------|-------|------------|-------|------------|-------|------------|
| ATA,ATC,ATT | I (Ile) | CTA,CTC,CTG,CTT | L (Leu) | GTA,GTC,GTG,GTT | V (Val) | TCA,TCC,TCG,TCT | S (Ser) |
| ATG | M (Met) | CCA,CCC,CCG,CCT | P (Pro) | GCA,GCC,GCG,GCT | A (Ala) | TTC,TTT | F (Phe) |
| ACA,ACC,ACG,ACT | T (Thr) | CAC,CAT | H (His) | GAC,GAT | D (Asp) | TTA,TTG | L (Leu) |
| AAC,AAT | N (Asn) | CAA,CAG | Q (Gln) | GAA,GAG | E (Glu) | TAC,TAT | Y (Tyr) |
| AAA,AAG | K (Lys) | CGA,CGC,CGG,CGT | R (Arg) | GGA,GGC,GGG,GGT | G (Gly) | TAA,TAG,TGA | _ (Stop) |
| AGC,AGT | S (Ser) | | | | | TGC,TGT | C (Cys) |
| AGA,AGG | R (Arg) | | | | | TGG | W (Trp) |

## API Endpoint

The application also provides a REST API endpoint for programmatic access:

### POST /process

**Request Body** (JSON):
```json
{
  "dna_original": "ATGCGATCG...",
  "amino_acid_original": "MRFSL..."
}
```

**Response** (JSON):
```json
{
  "result": true,
  "translated_protein": "MRFSL...",
  "original_protein": "MRFSL...",
  "dna_segment_used": "ATGCGA..."
}
```

## File Structure

```
dna-translation-checker/
├── app.py                 # Flask backend server
├── templates/
│   └── ui.html           # Web interface
└── README.md             # This file
```

## Error Handling

The application handles various error conditions:

- **Empty sequences**: Validates that both DNA and amino acid sequences are provided
- **Invalid DNA sequences**: Checks for valid nucleotide characters and proper length
- **Short sequences**: Ensures DNA sequence is long enough for the required segment
- **Translation errors**: Handles invalid codons or sequences not divisible by 3
- **Network errors**: Provides feedback for connection issues

## Customization

### Changing the DNA Segment

To modify which part of the DNA sequence is translated, edit the `start_pos` and `end_pos` variables in `app.py`:

```python
start_pos = 20    # Change starting position
end_pos = 935     # Change ending position
```

### Modifying the Genetic Code

To use a different genetic code table, update the `table` dictionary in the `translate()` function in `app.py`.

## Troubleshooting

### Common Issues

1. **Port already in use**: If port 5000 is busy, change the port in `app.py`:
   ```python
   app.run(debug=True, port=5001)  # Use a different port
   ```

2. **Module not found**: Ensure Flask is installed:
   ```bash
   pip install flask flask-cors
   ```

3. **Template not found**: Verify the `templates/` directory exists and contains `ui.html`

4. **Empty results**: Check that your DNA sequence is at least 935 characters long

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or contributions, please create an issue in the project repository or contact the development team.