# Auto-Concordance 🔍📚🔗

**Discover the hidden connections within texts.**

Automatically generate a concordance for a set of books. Uses text embeddings to find relationships between texts.

## Features
1. Text embedding analysis: The project utilizes text embeddings to analyze and find relationships between texts.
2. Automatic concordance generation: The software automatically generates a concordance for a set of books or texts.
3. Relationship identification: The project identifies and highlights hidden connections within texts.
4. Efficient processing: The software is designed to process large volumes of text efficiently.
5. User-friendly interface: The project provides a user-friendly interface for easy interaction and navigation.
6. Customization options: The software allows users to customize the concordance generation process according to their specific requirements.

## Getting started
```bash
pip install auto-concordance
```
Here is an example usage of the Auto-Concordance project:

```python
from auto_concordance.concordance import generate_concordance

# Define a list of books or texts
texts = [
    "The quick brown fox jumps over the lazy dog.",
    "A quick brown dog jumps over a lazy fox.",
    "The lazy dog is brown and the fox is quick.",
]

# Generate a concordance for the texts
concordance = generate_concordance(texts)

# Print the concordance
for word, occurrences in concordance.items():
    print(f"{word}: {occurrences}")
```

This example demonstrates how to use the `generate_concordance` function from the `auto_concordance.concordance` module to generate a concordance for a set of books or texts. The function takes a list of texts as input and returns a dictionary where the keys are words and the values are the number of occurrences of each word in the texts. The example then prints the concordance, displaying each word and its occurrences.
## Project Structure
- `auto_concordance/`: This directory contains the main code files for the Auto-Concordance project.
- `auto_concordance/__init__.py`: This file is used to initialize the `auto_concordance` package.
- `auto_concordance/concordance.py`: This file contains the code for generating a concordance for a set of books or texts.
- `auto_concordance/embeddings.py`: This file contains the code for analyzing and finding relationships between texts using text embeddings.
- `auto_concordance/utils.py`: This file contains utility functions used in the Auto-Concordance project.
- `tests/`: This directory contains the test files for the Auto-Concordance project.
- `tests/test_concordance.py`: This file contains the tests for the concordance generation functionality.
- `tests/test_embeddings.py`: This file contains the tests for the text embedding analysis functionality.
- `docs/`: This directory contains the documentation files for the Auto-Concordance project.
- `docs/index.md`: This file contains the main documentation for the project.
- `README.md`: This file contains the README documentation for the Auto-Concordance project.
- `LICENSE`: This file contains the license information for the project.
- `setup.py`: This file contains the setup configuration for the Auto-Concordance project.
- `requirements.txt`: This file contains the required dependencies for the project.

## Changelog

## Development
 
 - Install pyenv
 - Git clone the project
 - Run `make init` to create the environment and install the dependencies
 - You can now run:
   - `make help` to see the available commands
   - `make test` to run the tests
   - `make lint` to run the linter
   - `make autoformat` to format the code
   - `make type-check` to run the type checker