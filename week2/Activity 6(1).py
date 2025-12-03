


class FileProcessor:
    """
    A class responsible for reading a file, printing its content,
    counting '*' characters, and showing an End of File message.
    """

    def __init__(self, file_path: str):
        """
        Constructor: stores the path of the file to be processed
        and initializes the star counter.

        :param file_path: Path to the file that should be read
        """
        self.file_path = file_path
        self.star_count = 0

    def process_file(self) -> None:
        """
        High-level method that:
        - opens the file
        - prints each line
        - counts '*' characters
        - prints the End of File message and summary
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                for line in file:
                    # Print the current line exactly as it is
                    print(line, end="")

                    # Count '*' characters in this line
                    self._count_stars(line)

            # After finishing reading, show EOF message and star summary
            self._print_end_of_file_message()
            self._print_star_summary()

        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' was not found.")
        except OSError as e:
            print(f"An error occurred while reading the file: {e}")

    def _count_stars(self, text: str) -> None:
        """
        Counts how many '*' characters are in the given text
        and adds them to the total star_count.

        :param text: A line of text from the file
        """
        self.star_count += text.count("*")

    def _print_end_of_file_message(self) -> None:
        """Prints the End of File notification."""
        print("\n--- End of File ---")

    def _print_star_summary(self) -> None:
        """Prints the total number of '*' characters found in the file."""
        print(f"Total '*' characters found: {self.star_count}")


def main() -> None:
    """
    Entry point of the program:
    - Asks the user for a file name
    - Creates a FileProcessor object
    - Calls process_file() to perform all tasks
    """
    file_name = input("Enter the file name to read: ").strip()
    processor = FileProcessor(file_name)
    processor.process_file()


if __name__ == "__main__":
    main()
