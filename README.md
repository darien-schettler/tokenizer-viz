# Tokenizer Viz

Tokenizer Viz is a Python package that generates HTML to visualize the tokenization of text. It highlights tokens with different colors and customizable styles, making it easier to understand how a text is tokenized.

---

<br>

## Project Layout

```terminal
tokenizer-viz/
│
├── tokenizer_viz/
│   ├── __init__.py
│   └── visualization.py
│
├── .gitignore
├── LICENSE
├── README.md
└── setup.py

<br>

## Installation

You can install the **`tokenizer-viz`** package using pip:

```bash
pip install tokenizer-viz
```

<br>

## Usage
Here's a quick example of how to use the package:

Usage with a provided encoder and decoder

```python
from tokenizer_viz import TokenVisualization
from IPython.display import HTML

# Define sample encoder and decoder functions for demonstration purposes
def sample_encoder(text):
    return list(text)

def sample_decoder(token):
    return token

# Initialize the TokenVisualization class with the encoder and decoder functions
token_viz = TokenVisualization(
    encoder=sample_encoder,
    decoder=sample_decoder
)

# Define a sample text to visualize tokenization boundaries
sample_text = "This is a sample text.\nIt has multiple lines."

# Visualize the tokenization boundaries
html = token_viz.visualize(sample_text)
HTML(html)
```

<br>

## EXAMPLE OUTPUT

**TBD EXAMPLE IMAGE**

<br>

## ARGUMENTS

The **`TokenVisualization`** class accepts several optional
parameters to customize the appearance and layout of the tokens:
* **`cmap`** (defualt=**`'Pastel2'`**),
* **`font_family`** (defualt=**`'Courier New'`**),
* **`transparency`** (default=**`0.675`**),
* **`font_size`** (defualt=**`'1.1em'`**),
* **`unk_token`** (defualt=**`'???'`**),
* **`font_weight`** (defualt=**`300`**),
* **`padding`** (defualt=**`'0px'`**),
* **`margin_right`** (defualt=**`'0px'`**),
* **`border_radius`** (defualt=**`'0px'`**),
* **`background_color`** (defualt=**`'#F0F0F0'`**),

Please refer to the class docstrings and method docstrings for a detailed description of each parameter.

## License

This project is licensed under the MIT License.

<br>