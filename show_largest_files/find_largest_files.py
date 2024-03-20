import os
import heapq

def find_largest_files(directory, count):
    file_sizes = []

    # Traverse the directory and collect file sizes
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            file_sizes.append((os.path.getsize(filepath), filepath))

    # Get the N largest files using heapq.nlargest
    largest_files = heapq.nlargest(count, file_sizes)

    # Display the results
    print(f"\nTop {count} largest files:")
    for size, filepath in largest_files:
        print(f"{filepath} - {size / (1024 * 1024):.2f} MB")

if __name__ == "__main__":
    # Get user input for directory and count
    directory = input("Enter the directory to search: ")
    count = int(input("Enter the number of largest files to display: "))

    # Call the function
    find_largest_files(directory, count)
