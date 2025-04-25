import pefile

# Replace with the path to your PE binary file
file_path = 'procexp.exe'

try:
    pe = pefile.PE(file_path)

    print("=== DOS Header ===")
    print(pe.DOS_HEADER)

    print("\n=== NT Headers ===")
    print(pe.NT_HEADERS)

    print("\n=== File Header ===")
    print(pe.FILE_HEADER)

    print("\n=== Optional Header ===")
    print(pe.OPTIONAL_HEADER)

    print("\n=== Sections ===")
    for section in pe.sections:
        print(f"{section.Name.decode().rstrip(chr(0))}:")
        print(f"  Virtual Address: {hex(section.VirtualAddress)}")
        print(f"  Virtual Size:    {hex(section.Misc_VirtualSize)}")
        print(f"  Raw Size:        {hex(section.SizeOfRawData)}\n")

except FileNotFoundError:
    print("File not found.")
except pefile.PEFormatError as e:
    print(f"Not a valid PE file: {e}")
