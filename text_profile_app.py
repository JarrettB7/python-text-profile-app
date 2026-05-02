# Name: Jarrett Blevins
# Date: May 1, 2026
# Description: This program demonstrates string methods, text metadata, and uses the Rich library to format output in the terminal.


# Importing external library components from Rich
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# -----------------------------
# About section
# -----------------------------
def show_about():
    # Text explaining what the program does
    about_text = (
        "Text Profile App\n"
        "This program demonstrates:\n"
        "- string methods\n"
        "- text metadata\n"
        "- an About menu\n"
        "- an external library from PyPI"
    )
    #Display the about information inside a styled panel
    console.print(Panel(about_text, title="About", expand=False))

# -----------------------------
# Metadata section
# -----------------------------
# Create a table to display metadata
def show_metadata(original_text, cleaned_text):
    table = Table(title="Text Metadata")
    # Define table columns
    table.add_column("Property")
    table.add_column("Value")

# Add rows with information about the text
    table.add_row("Original Text", original_text)
    table.add_row("Cleaned Text", cleaned_text)
    table.add_row("Character Count", str(len(cleaned_text)))
    table.add_row("Word Count", str(len(cleaned_text.split())))
    table.add_row("Uppercase", cleaned_text.upper())
    table.add_row("Lowercase", cleaned_text.lower())
    table.add_row("Title Case", cleaned_text.title())

    console.print(table)

# -----------------------------
# Main program
# -----------------------------
def main():
    # Display welcome message
    console.print(Panel("Welcome to the Text Profile App", title="Main Menu", expand=False))

  # Get user input
    user_text = input("Enter a short sentence or phrase: ")

    cleaned_text = user_text.strip()
    # Replace lowercase "python" with capitalized "Python"
    replaced_text = cleaned_text.replace("python", "Python")

# Display various string transformations
    console.print("\nUpdated Text Results")
    console.print("Stripped text:", cleaned_text)
    console.print("Uppercase:", cleaned_text.upper())
    console.print("Lowercase:", cleaned_text.lower())
    console.print("Title Case:", cleaned_text.title())
    console.print("Replaced Text:", replaced_text)
    console.print("Centered Text:", cleaned_text.center(40, "-"))

    show_metadata(user_text, cleaned_text)
    show_about()

# Run the program
if __name__ == "__main__":
    main()
