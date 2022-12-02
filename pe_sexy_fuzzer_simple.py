import pefile
import os
import secrets

# Load the PE file.
pe = pefile.PE("file.exe")

# Generate a random section name.
def generate_section_name():
  # Generate a random string of 8 characters.
  name = ""
  name = secrets.token_bytes(8)
  return name

# Fuzz the PE file's section names.
for section in pe.sections:
  # Generate a random section name.
  name = generate_section_name()
  print("Fuzzing section name:", section.Name, "->", name, "\n")

  # Try to save the PE file with the new section name.
  try:
    section.Name = name
    pe.write("file.exe")
  except Exception as e:
    print("Error", e, "\n")

# Define the path to the PE file.
pe.close
filepath = "file.exe"

# Try to run the PE file.
try:
  os.startfile(filepath)
except Exception as e:
  # Output the error to the output file.
    print("Error:", e, "\n")
