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

In one terminal from where ollama is installed:
run the ollama server

In another terminal from where the project is located to prompt LLMs:
LLM-Code-Security-Analysis$ python LLM-code/Local/codegemma.py 