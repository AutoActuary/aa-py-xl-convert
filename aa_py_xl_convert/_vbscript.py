from pathlib import Path
from subprocess import run

from locate import this_dir


def convert_to_xlsx_using_vbscript(input_path: Path, output_path: Path) -> None:
    """
    Use a VBS script to convert a file to xlsx format.

    Args:
        input_path: The path to the original Excel file.
        output_path: The path to the converted Excel file.
    """
    output_path = output_path.resolve()
    input_path = input_path.resolve()

    # `subprocess.CREATE_NO_WINDOW` can only be imported on Windows.
    # noinspection PyPep8Naming
    CREATE_NO_WINDOW = 134217728

    run(
        args=[
            "cscript",
            "//nologo",
            str(this_dir().joinpath("save_as_xlsx.vbs")),
            str(input_path),
            str(output_path),
        ],
        check=True,
        creationflags=CREATE_NO_WINDOW,
    )

    # The VBScript does not set an exit code if it fails, so we have to check if the output file exists.
    if not output_path.exists():
        raise RuntimeError(
            f"Failed to convert {input_path} to {output_path}: VBScript produced no output."
        )
