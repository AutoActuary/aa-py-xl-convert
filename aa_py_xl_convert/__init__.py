"""
Convert Excel files from `.xlsb` to `.xlsx`.

This is supposed to be temporary, until we can find a way to read `.xlsb` files directly without Windows or Excel.
"""

from ._context import converted_to_xlsx_if_necessary
