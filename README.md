# Tokenizer Visualizer

Tokenizer Visualizer is a Python package that generates HTML to visualize the tokenization of text. It highlights tokens with different colors and customizable styles, making it easier to understand how a text is tokenized.

---

## Project Layout

```terminal
tokenizer-viz/
│
├── tokenizer_viz/
│   ├── __init__.py
│   └── viz—utils.py
│
├── .gitignore
├── README.md
└── setup.py
```

---

## Installation

You can install the tokenizer-visualizer package using pip:

```bash
pip install tokenizer-visualizer
```

---

## Usage

Here's a quick example of how to use the package:

**Usage with a list of strings**

```python
from tokenizer_viz.viz_utils import get_visualization
from IPython.display import HTML

tokens = ['This', ' ', 'is', ' ', 'an', ' ', 'example', ' ', 'sentence']

html = get_visualization(tokens)

# Display the generated HTML
HTML(html)
```

**OUTPUT**

![Tokenizer Visualizer Example #1](https://i.ibb.co/GpsgxTL/Screenshot-2023-04-07-at-3-48-55-PM.png)

**Usage with an encoder and decoder**

```python
from tokenizer_viz.viz_utils import get_visualization
from IPython.display import HTML

ascii_encoder = lambda x: [ord(char) for char in x]
ascii_decoder = lambda x: ''.join([chr(int(char)) for char in x])
corpus = "This is an example sentence"

html = get_visualization(
    tokens=ascii_encoder(corpus),
    decoder=ascii_decoder,
    font_weight='regular',
)

# Display the generated HTML in the notebook (or wherever you're running this)
HTML(html)
```

**OUTPUT**

![Tokenizer Visualizer Example #2](https://i.ibb.co/SKPtXpN/Screenshot-2023-04-07-at-3-44-46-PM.png)

The `get_visualization` function accepts several optional 
parameters to customize the appearance and layout of the tokens:
* **tokens**,
* **decoder** (defualt=`None`),
* **cmap** (defualt=`'Pastel1'`),
* **font_family** (defualt=`'Courier New'`),
* **font_size** (defualt=`'1.1em'`),
* **unk_token** (defualt=`'???'`),
* **font_weight** (defualt=`'bold'`),
* **padding** (defualt=`'2px'`),
* **margin_right** (defualt=`'1px'`),
* **border_radius** (defualt=`'3px'`),
* **display_inline** (defualt=`False`),

Please refer to the function docstrings for a detailed description of each parameter.

---

## License

This project is licensed under the MIT License.
