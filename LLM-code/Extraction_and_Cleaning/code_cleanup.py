import re
import os
import sys

def clean_gemini_code(input_text):
    """
    Clean up Gemini-generated code by removing escape characters and formatting.
    
    Args:
        input_text (str): The input code string with potential escape characters
    
    Returns:
        str: Cleaned Python code
    """
    # Remove backslash + newline escape sequences
    cleaned_text = input_text.replace('\\n', '\n')
    
    # Remove triple backtick code block markers if present
    cleaned_text = re.sub(r'^```python\n|```$', '', cleaned_text, flags=re.MULTILINE)
    
    # Remove any leading/trailing whitespace
    cleaned_text = cleaned_text.strip()
    
    return cleaned_text

def process_file(input_file, output_file=None):
    """
    Process a file containing Gemini-generated code.
    
    Args:
        input_file (str): Path to the input file
        output_file (str, optional): Path to the output file. 
                                     If None, will use input filename with '_cleaned' appended.
    """
    # Read input file
    with open(input_file, 'r') as f:
        input_text = f.read()
    
    # Clean the code
    cleaned_code = clean_gemini_code(input_text)
    
    # Determine output file path
    if output_file is None:
        base, ext = os.path.splitext(input_file)
        output_file = f"{base}_cleaned{ext}"
    
    # Write cleaned code to output file
    with open(output_file, 'w') as f:
        f.write(cleaned_code)
    
    print(f"Cleaned code written to {output_file}")

def main():
    # Check if file path is provided as an argument
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    process_file(input_file)

if __name__ == "__main__":
    main()