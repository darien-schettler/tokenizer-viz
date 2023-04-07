from IPython.display import HTML
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def get_color(value, cmap='Pastel1'):
    """
    Returns an HTML-formatted string representing the background color for a token.

    Args:
        value (int): The index of the token to color.
        cmap (str, optional): The name of the colormap to use. Defaults to 'Pastel1'.

    Returns:
        str: An HTML-formatted string representing the background color.
    """
    colormap = plt.get_cmap(cmap)
    return f"background-color: {mcolors.rgb2hex(colormap(value % cmap.N))};"


def get_visualization(tokens, decoder=None, cmap='Pastel1', font_family='Courier New',
                      font_size='1.1em', unk_token='???', font_weight='bold', padding='2px',
                      margin_right='1px', border_radius='3px', display_inline=False):
    """
    Generates an HTML string to visualize the tokenization of a text.

    Args:
        tokens (list):
            – A list of integer tokens.
        decoder (function, optional):
            – A function that maps an integer to the representative string
            – If this is None, the tokens are assumed to be strings not integers
        cmap (str, optional):
            – The name of the colormap to use. Defaults to 'Pastel1'.
        font_family (str, optional):
            – The font family to use for tokens. Defaults to 'Courier New'.
        font_size (str, optional):
            – The font size to use for tokens. Defaults to '1.1em'.
        unk_token (str, optional):
            – The string to use for unknown tokens. Defaults to '???'
        font_weight (str, optional):
            – The font weight to use for tokens. Defaults to 'bold'.
        padding (str, optional):
            – The padding to use for tokens. Defaults to '2px'.
        margin_right (str, optional):
            – The right margin to use for tokens. Defaults to '5px'.
        border_radius (str, optional):
            – The border radius to use for tokens. Defaults to '3px'.
        display_inline (bool, optional):
            – Whether to display the HTML inline. Defaults to False.

    Returns:
        str: An HTML string representing the tokenized text with styling.
    """
    html = f"<style>span.token {{font-family: {font_family}; font-size: {font_size}; font-weight: {font_weight}; " \
           f"padding: {padding}; margin-right: {margin_right}; border-radius: {border_radius};}}</style>"

    for i, token in enumerate(tokens):
        color = get_color(i, cmap)
        try:
            html += f"<span class='token' style='{color}'>{decoder(token)}</span>"
        except TypeError:
            html += f"<span class='token' style='{color}'>{unk_token}</span>"

    if display_inline:
        HTML(html)

    return html
