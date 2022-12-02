# pe_sexy_fuzzer_simple.py
python script to fuzz pe section names

This script loads a PE file, generates a random section name, and then attempts to load the PE file with the new section name. If the PE file can be loaded with the new section name, the script will write the modified PE file to disk. If the PE file cannot be loaded with the new section name, an error will be printed.
