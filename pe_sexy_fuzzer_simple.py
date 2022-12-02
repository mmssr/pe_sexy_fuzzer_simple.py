import pefile
import random
import os

# Load the PE file.
pe = pefile.PE("path/to/pe/file.exe")

# Generate a random section name.
def generate_section_name():
  # Generate a random string of 8 characters.
  name = ""
  for i in range(8):
    name += chr(random.randint(32, 126))
  return name

# Fuzz the PE file's section names.
for section in pe.sections:
  # Generate a random section name.
  name = generate_section_name()
  print("Fuzzing section name:", section.Name, "->", name, "\n")

  # Try to save the PE file with the new section name.
  try:
    section.Name = name
    pe.write("path/to/output/file.exe")
  except Exception as e:
    print("Error", e, "\n")

# Try to run the PE file.
filepath = "path/to/output/file.exe"

try:
  os.startfile(filepath)
except Exception as e:
    print("Error:", e, "\n")
