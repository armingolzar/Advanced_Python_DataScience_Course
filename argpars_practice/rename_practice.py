import argparse
import os

def rename_files(path, prefix, suffix, ext):
    if not os.path.exists(path):
        print(f"Error: The path '{path}' does not exist.")
        return

    files = os.listdir(path)
    count = 0

    for file in files:
        old_path = os.path.join(path, file)

        # Only rename files (not folders)
        if os.path.isfile(old_path):
            name, extension = os.path.splitext(file)

            # Filter by extension if provided
            if ext and extension != ext:
                continue

            new_name = f"{prefix}{name}{suffix}{extension}"
            new_path = os.path.join(path, new_name)

            os.rename(old_path, new_path)
            count += 1
            print(f"Renamed: {file} → {new_name}")

    print(f"✅ Done! Renamed {count} files.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename files in a folder with optional prefix/suffix.")

    parser.add_argument("--path", required=True, help="Path to the folder containing files.")
    parser.add_argument("--prefix", default="", help="Prefix to add to each file name.")
    parser.add_argument("--suffix", default="", help="Suffix to add to each file name.")
    parser.add_argument("--ext", default="", help="Filter files by extension (e.g., .txt).")

    args = parser.parse_args()

    rename_files(args.path, args.prefix, args.suffix, args.ext)