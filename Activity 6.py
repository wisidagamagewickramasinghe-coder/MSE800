

class FileReader:
    def __init__(self, filename):
        self.demo_file = filename
        self.content = ""

    def read_file(self):
      
        try:
            with open(self.demo_file, 'r', encoding='utf-8') as file:
                self.content = file.read()
            print("File read successfully.\n")
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
    def display_content(self):
        #Prints the content of the file.
        if self.content:
    
            print(self.content)
        else:
            print("No content loaded. Please read the file first.")

    def count_asterisks(self):
        #Counts and prints number of '*' characters
        if self.content:
            count = self.content.count('*')
            print(f"\nNumber of '*' characters found: {count}")
        else:
            print("No content loaded. Please read the file first.")



if __name__ == "__main__":
    filename = input("enter the file name:")
    file_reader = FileReader(filename)

    file_reader.read_file()
    file_reader.display_content()
    file_reader.count_asterisks()
   