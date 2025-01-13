import os
import sys
from art_model import load_image, display_image

# Importing helper functions from scripts folder
from scripts.start_bot import start_bot
from scripts.update_dependencies import update_dependencies
from scripts.clear_cache import clear_cache
from scripts.generate_sample import generate_sample


def main():
    """
    Main entry point for Aerith AI.
    Provides options to start the bot, update dependencies, clear cache, or generate a sample image.
    """
    print(
        """
    Welcome to Aerith AI!
    Please select an option:
    1. Start the bot
    2. Update dependencies
    3. Clear cache
    4. Generate a sample manga PFP
    5. Exit
    """
    )

    while True:
        try:
            choice = int(input("Enter your choice (1-5): ").strip())
            if choice == 1:
                print("Starting the bot...")
                start_bot()
            elif choice == 2:
                print("Updating dependencies...")
                update_dependencies()
            elif choice == 3:
                print("Clearing cache...")
                clear_cache()ff
                print("Generating a sample manga PFP...")
                generate_sample()
            elif choice == 5:
                print("Exiting Aerith AI. See you next time!")
                sys.exit(0)
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
