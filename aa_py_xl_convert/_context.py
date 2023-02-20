import logging
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Generator

from ._vbscript import convert_to_xlsx_using_vbscript

logger = logging.Logger(__name__)


@contextmanager
def converted_to_xlsx_if_necessary(input_path: Path) -> Generator[Path, None, None]:
    """
    Temporarily convert a file to xlsx format if necessary.

    Args:
        input_path: The path to the original file.

    Yields:
        The original path if the file is already in xlsx format, otherwise the path to the converted file.
        The converted file is removed when the context manager exits.
    """
    if input_path.suffix.lower() in [".xlsx", ".xlsm"]:
        yield input_path
    else:
        with TemporaryDirectory() as tmp_dir_str:
            output_path = Path(tmp_dir_str, f"{input_path.stem}.xlsx")
            logger.warning(
                f"Converting file from `{input_path.suffix}` to `.xlsx` format. "
                "For better performance, use only `.xlsx` or `.xlsm` files."
            )
            convert_to_xlsx_using_vbscript(input_path, output_path)
            yield output_path
