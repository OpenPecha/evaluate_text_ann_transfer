import difflib

import Levenshtein
from diff_match_patch import diff_match_patch


def transfer_coordinate_google(
    source_text: str, target_text: str, source_coordinate: int
):
    dmp = diff_match_patch()
    diffs = dmp.diff_main(source_text, target_text)

    # Use DiffXIndex to find the equivalent location in the target text
    target_coordinate = dmp.diff_xIndex(diffs, source_coordinate)

    return target_coordinate


def transfer_coordinate_difflib(
    source_text: str, target_text: str, source_coordinate: int
):
    matcher = difflib.SequenceMatcher(None, source_text, target_text)
    blocks = matcher.get_matching_blocks()

    for block in blocks:
        if block.a <= source_coordinate < block.a + block.size:
            return block.b + (source_coordinate - block.a)

    return source_coordinate  # fallback if no match found


def transfer_coordinate_levenshtein(
    source_text: str, target_text: str, source_coordinate: int
):
    editops = Levenshtein.editops(source_text, target_text)
    offset = 0

    for op, src, tgt in editops:
        if src > source_coordinate:
            break
        if op == "insert":
            offset += 1
        elif op == "delete":
            offset -= 1

    return source_coordinate + offset
