import os
import json
from bs4 import BeautifulSoup

# Base directory path (adjust this path as necessary)
BASE_DIR = "GCJ/gcj-dataset/codejam"

# Function to clean up $$$ symbols from math expressions
def clean_math_expressions(text):
    return text.replace('$$$', '')

# Function to extract sample input and output from text files based on file name suffix
def extract_sample_input_output(root):
    sample_input = "No sample input found."
    sample_output = "No sample output found."
    
    # Walk through the files in the directory and look for input and output text files
    for file in os.listdir(root):
        if file.endswith('_input.txt'):
            input_file_path = os.path.join(root, file)
            with open(input_file_path, 'r', encoding='utf-8') as input_file:
                sample_input = clean_math_expressions(input_file.read().strip())
        # elif file.endswith('_output.txt'):
        #     output_file_path = os.path.join(root, file)
        #     with open(output_file_path, 'r', encoding='utf-8') as output_file:
        #         sample_output = clean_math_expressions(output_file.read().strip())
    
    return sample_input, sample_output

# Function to extract prompts and answers from HTML files
def extract_prompts_and_answers(base_dir):
    extracted_data = []
    
    # Walk through the directory tree
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            # Look for the problem.html file
            if file == "problem.html":
                html_file_path = os.path.join(root, file)
                print(f"Processing: {html_file_path}")
                
                # Read the HTML content
                with open(html_file_path, "r", encoding="utf-8") as html_file:
                    soup = BeautifulSoup(html_file, "html.parser")

                # Extract the problem name (title of the h1 tag)
                problem_name = soup.find('h1').get_text(strip=True) if soup.find('h1') else "No problem name found."

                # Extract problem statement (located after "Problem")
                problem_statement = ""
                problem_section = soup.find('h3', string="Problem")
                if problem_section:
                    # Loop through <p> tags after the "Problem" section until the next <h3>
                    next_h3 = problem_section.find_next('h3')
                    for p_tag in problem_section.find_all_next('p'):
                        if p_tag == next_h3:
                            break
                        problem_statement += p_tag.get_text(strip=True) + "\n"
                problem_statement = clean_math_expressions(problem_statement)

                # Extract input description (located after "Input")
                input_description = (
                    soup.find('h3', string="Input").find_next('p').get_text(strip=True)
                    if soup.find('h3', string="Input") else "No input description found."
                )
                input_description = clean_math_expressions(input_description)
                
                # Extract output description (located after "Output")
                output_description = (
                    soup.find('h3', string="Output").find_next('p').get_text(strip=True)
                    if soup.find('h3', string="Output") else "No output description found."
                )
                output_description = clean_math_expressions(output_description)

                # Extract sample input and output from corresponding text files
                sample_input, sample_output = extract_sample_input_output(root)

                # Add the extracted data
                extracted_data.append({
                    "problem_name": problem_name,
                    "problem_statement": problem_statement,
                    "input_description": input_description,
                    "output_description": output_description,
                    "sample_input": sample_input,
                    # "sample_output": sample_output,
                    "source": html_file_path  # Store source for reference
                })

    return extracted_data

# Run the extraction
extracted_data = extract_prompts_and_answers(BASE_DIR)

# Save extracted data to a JSON file for easier inspection
output_file = os.path.join("GCJ", "2016-2022_extracted_prompts.json")
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(extracted_data, json_file, indent=4, ensure_ascii=False)

# Print the number of extracted problems
print(f"Extraction complete. {len(extracted_data)} problems extracted. Data saved to {output_file}")