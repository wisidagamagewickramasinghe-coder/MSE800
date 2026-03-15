# Temperature conversion program with input validation
# Autohor : Wisidagamage
# Date : 2025-12-04

class TemperatureConverter:
    def __init__(self):
        self.user_input = ""
        self.prefix = ""
        self.value = 0.0

    def get_input(self):
        """Get user input and validate it."""
        self.user_input = input("Enter the temperature (e.g., F51 or C11): ").strip()

    def validate(self):
        """Validate input format."""
        # Basic length check
        if len(self.user_input) < 2:
            return False
        # split prefix and numeric part
        self.prefix = self.user_input[0]      
        number_part = self.user_input[1:]      

        # Try converting numeric part
        try:
            self.value = float(number_part)
        except ValueError:
            return False

        # Prefix check
        if self.prefix not in ('F', 'C'):
            return False

        return True

    def convert(self):
        """Perform temperature conversion."""
        if self.prefix == 'F':
            celsius = (self.value - 32) * 5 / 9
            return f"{self.user_input} degrees Fahrenheit is converted to {celsius:.2f} degrees Celsius"

        elif self.prefix == 'C':
            fahrenheit = (self.value * 9 / 5) + 32
            return f"{self.user_input} degrees Celsius is converted to {fahrenheit:.2f} degrees Fahrenheit"

    def run(self):
        """Main logic for running the converter with validation."""
        self.get_input()

        if not self.validate():
            print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix.")
        else:
            print(self.convert())


# Main execution
if __name__ == "__main__":
    converter = TemperatureConverter()
    converter.run()