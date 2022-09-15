# openscraper/__init__.py

# This file is necessary for Python to recognize the 'openscraper' directory as a package.
# It may be empty or contain initialization code that runs when the package is imported.

# Example: Initializing some configuration or variables when the package is imported.

# Configuration variables
DEFAULT_TIMEOUT = 10  # Default timeout value for network requests in seconds
MAX_CONCURRENT_REQUESTS = 5  # Maximum number of concurrent requests during asynchronous scraping

# Initialization code
print("OpenScraper package is being initialized!")

# You can define functions or perform any other setup tasks here that should run when the package is imported.

# Example function
def welcome_message():
    return "Welcome to OpenScraper! This is your web scraping toolkit."
