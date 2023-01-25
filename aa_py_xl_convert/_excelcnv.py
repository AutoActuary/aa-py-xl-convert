import os
from itertools import chain
from pathlib import Path
from subprocess import run


def convert_to_xlsx_using_excelcnv(input_path: Path, output_path: Path) -> None:
    """
    Use `excelcnv.exe` to convert a file to xlsx format.

    See Also:
        https://www.hexacorn.com/blog/2021/05/23/excellent-conversions-and-downloads/

    Args:
        input_path: The path to the original Excel file.
        output_path: The path to the converted Excel file.
    """
    output_path = output_path.resolve()
    input_path = input_path.resolve()

    run(
        args=[
            str(find_excelcnv()),
            "-oice",
            str(input_path),
            str(output_path),
        ],
        check=True,
    )

    # `excelcnv.exe` does not set an exit code if it fails, so we have to check if the output file exists.
    if not output_path.exists():
        raise RuntimeError(
            f"Failed to convert {input_path} to {output_path}: `excelcnv.exe` produced no output."
        )


def find_excelcnv() -> Path:
    """
    Try to find `excelcnv.exe`.
    """
    try:
        return next(
            chain(
                Path(os.environ["PROGRAMFILES"]).glob(
                    "Microsoft Office/root/Office*/excelcnv.exe"
                ),
                Path(os.environ["PROGRAMFILES(X86)"]).glob(
                    "Microsoft Office/root/Office*/excelcnv.exe"
                ),
            )
        )
    except StopIteration as e:
        raise RuntimeError("Could not find `excelcnv.exe`") from e
