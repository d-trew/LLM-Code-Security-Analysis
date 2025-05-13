# LLM Code Generation Benchmarking

A project to evaluate different LLMs' capabilities in generating Python code solutions for programming competition problems.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Ollama](https://img.shields.io/badge/Ollama-%23000000.svg?style=for-the-badge&logo=ollama&logoColor=white)

## 📌 Overview

This project:
1. Takes programming competition problems (from Google Code Jam)
2. Generates Python solutions using various LLMs via Ollama
3. Validates and analyzes the quality of generated code
4. Produces comparative reports on model performance

To run Ollama:
In one terminal from where ollama is installed:
run the ollama server

In another terminal from where the project is located to prompt LLMs:
LLM-Code-Security-Analysis$ python LLM-code/Local/codegemma.py 


Then run the python file that prompts one of the LLMs downloaded by Ollama

The results are stored in LLM_Response/

The results can be extracted using LLM-code\Extraction_and_Cleaning\code_extraction_from_json.py

Bandit reports can be generated with LLM-code\bandit\generate_bandit_reports.py and CodeQL reports were generated with a databasequery

the reports can then be analysed with LLM-code\bandit\analyse_bandit_reports.py and LLM-code\codeql\analyse_codeql_reports.py
