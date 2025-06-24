from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def translate(seq):
    table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
    }

    protein = ""
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            if codon in table:
                protein += table[codon]
            else:
                # Handle invalid codons
                return None
    else:
        return None

    return protein


def clean_sequence(seq):
    """Clean sequence by removing newlines and carriage returns"""
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    seq = seq.replace(" ", "")  # Also remove spaces
    return seq.upper()


@app.route('/')
def index():
    return render_template('ui.html')


@app.route('/process', methods=['POST'])
def process_sequences():
    try:
        data = request.json

        # Get the three sequences from the request
        dna_original = clean_sequence(data.get('dna_original', ''))
        amino_acid_original = clean_sequence(data.get('amino_acid_original', ''))

        # Validate inputs
        if not dna_original or not amino_acid_original:
            return jsonify({'error': 'Please provide both DNA and amino acid sequences'}), 400

        # Extract the relevant portion of DNA (positions 20 to 935 as in original code)
        # Adjust indices to be within bounds
        start_pos = min(20, len(dna_original))
        end_pos = min(935, len(dna_original))

        if start_pos >= len(dna_original):
            return jsonify({'error': 'DNA sequence too short'}), 400

        dna_segment = dna_original[start_pos:end_pos]

        # Translate the DNA segment
        translated_protein = translate(dna_segment)

        if translated_protein is None:
            return jsonify({'error': 'Invalid DNA sequence or length not divisible by 3'}), 400

        # Compare with the provided amino acid sequence
        result = translated_protein == amino_acid_original

        return jsonify({
            'result': result,
            'translated_protein': translated_protein,
            'original_protein': amino_acid_original,
            'dna_segment_used': dna_segment
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)