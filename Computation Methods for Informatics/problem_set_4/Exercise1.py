from tqdm import tqdm

def align(seq1, seq2, match = 1, gap_penalty = 1, mismatch_penalty = 1):
    rows = len(seq1) + 1
    cols = len(seq2) + 1
    score_matrix = [[0] * cols for _ in range(rows)]
    traceback_matrix = [[None] * cols for _ in range(rows)]
    max_score = 0
    max_pos = None
    for i in tqdm(range(1, rows)):
        for j in range(1, cols):
            if seq1[i-1] == seq2[j-1]:
                match_score = match
            else:
                match_score = -mismatch_penalty

            diag_score = score_matrix[i-1][j-1] + match_score
            up_score = score_matrix[i-1][j] - gap_penalty
            left_score = score_matrix[i][j-1] - gap_penalty
            score_matrix[i][j] = max(diag_score, up_score, left_score, 0)

            if score_matrix[i][j] == diag_score:
                traceback_matrix[i][j] = "diag"
            elif score_matrix[i][j] == up_score:
                traceback_matrix[i][j] = "up"
            elif score_matrix[i][j] == left_score:
                traceback_matrix[i][j] = "left"
            
            if score_matrix[i][j] > max_score:
                max_score = score_matrix[i][j]
                max_pos = (i,j)

    seq1_aligned = ""
    seq2_aligned = ""
    i, j = max_pos

    while score_matrix[i][j] != 0:
        if traceback_matrix[i][j] == "diag":
            seq1_aligned = seq1[i-1] + seq1_aligned
            seq2_aligned = seq2[j-1] + seq2_aligned
            i -= 1
            j -= 1
        elif traceback_matrix[i][j] == "up":
            seq1_aligned = seq1[i-1] + seq1_aligned
            seq2_aligned = "-" + seq2_aligned
            i -= 1
        elif traceback_matrix[i][j] == "left":
            seq1_aligned = "-" + seq1_aligned
            seq2_aligned = seq2[j-1] + seq2_aligned
            j -= 1

    return seq1_aligned, seq2_aligned, max_score

seq1 = 'tgcatcgagaccctacgtgac'
seq2 = 'actagacctagcatcgac'
seq1_aligned, seq2_aligned, max_score = align(seq1, seq2)
print("Default test taken from example")
print(f"seq1 = {seq1_aligned}")
print(f"seq2 = {seq2_aligned}")
print(f"Score = {max_score}")

seq1_aligned, seq2_aligned, max_score = align(seq1, seq2, gap_penalty = 2)
print("Test with gap penalty = 2 taken from example")
print(f"seq1 = {seq1_aligned}")
print(f"seq2 = {seq2_aligned}")
print(f"Score = {max_score}")

seq1_aligned, seq2_aligned, max_score = align(seq1, seq2, mismatch_penalty = -1)
print("Test with mismatch penalty = -1")
print(f"seq1 = {seq1_aligned}")
print(f"seq2 = {seq2_aligned}")
print(f"Score = {max_score}")

seq1_aligned, seq2_aligned, max_score = align(seq1, seq2, match = 2)
print("Test with match = 2")
print(f"seq1 = {seq1_aligned}")
print(f"seq2 = {seq2_aligned}")
print(f"Score = {max_score}")
