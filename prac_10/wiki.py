"""
CP1404/CP5632 Practical - Wikipedia Search
Wikipedia page search program
"""

import wikipedia

def main():
    """Main program: Wikipedia page search"""
    print("Wikipedia Search Program")

    while True:
        page_title = input("\nEnter page title: ").strip()

        # Exit on empty input
        if not page_title:
            print("Thank you.")
            break

        try:
            # Search and display page information
            search_page(page_title)

        except wikipedia.exceptions.DisambiguationError as e:
            handle_disambiguation_error(e)
        except wikipedia.exceptions.PageError:
            print(f"Page id \"{page_title}\" does not match any pages. Try another id!")
        except Exception as e:
            print(f"An error occurred: {e}")


def search_page(page_title):
    """
    Search and display Wikipedia page information
    """
    # Get page content
    page = wikipedia.page(page_title, auto_suggest=True)

    # Display page information
    print(page.title)

    # Get and print summary
    summary = wikipedia.summary(page_title, sentences=3)
    print(summary)

    # Print URL
    print(page.url)


def handle_disambiguation_error(error):
    """
    Handle disambiguation page error
    """
    print("We need a more specific title. Try one of the following, or a new search:")

    disambiguation_options = error.options[:10]
    print(disambiguation_options)


def setup_wikipedia():
    """Configure Wikipedia library settings"""
    # Set to English Wikipedia to match example output
    wikipedia.set_lang("en")

    # Enable rate limiting
    wikipedia.set_rate_limiting(True)


if __name__ == "__main__":
    try:
        setup_wikipedia()
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user")
        print("Thank you.")