from typing import Dict


def read_fasta(filepath: str) -> Dict[str, str]:
    """
    Read a FASTA file and return its contents as a dictionary.

    Parameters
    ----------
    filepath : str
        Path to the FASTA file.

    Returns
    -------
    Dict[str, str]
        Dictionary mapping sequence headers to sequences.

    Notes
    -----
    - Assumes standard FASTA format
    - Lines starting with '>' are headers
    - Sequence lines may span multiple lines
    """
    sequences: Dict[str, str] = {}

    current_header: str | None = None
    current_sequence_parts: list[str] = []

    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                if current_header is not None:
                    sequences[current_header] = "".join(current_sequence_parts)

                current_header = line[1:]
                current_sequence_parts = []
            else:
                current_sequence_parts.append(line)

        if current_header is not None:
            sequences[current_header] = "".join(current_sequence_parts)

    return sequences

