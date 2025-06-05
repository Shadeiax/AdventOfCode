def count_xmas_patterns(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])
    xmas_count = 0  # Initialisiere den Zähler

    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == 'A':
                tl_coord = (r - 1, c - 1)  # Top-Left
                tr_coord = (r - 1, c + 1)  # Top-Right
                bl_coord = (r + 1, c - 1)  # Bottom-Left
                br_coord = (r + 1, c + 1)  # Bottom-Right
                neighbor_coords = [tl_coord, tr_coord, bl_coord, br_coord]

                all_neighbors_in_bounds = True
                for nr, nc in neighbor_coords:
                    if not (0 <= nr < num_rows and 0 <= nc < num_cols):
                        all_neighbors_in_bounds = False
                        break

                if not all_neighbors_in_bounds:
                    continue

                tl_char = grid[tl_coord[0]][tl_coord[1]]
                tr_char = grid[tr_coord[0]][tr_coord[1]]
                bl_char = grid[bl_coord[0]][bl_coord[1]]
                br_char = grid[br_coord[0]][br_coord[1]]

                diag1_is_valid_ms = (tl_char == 'M' and br_char == 'S') or (tl_char == 'S' and br_char == 'M')
                diag2_is_valid_ms = (tr_char == 'M' and bl_char == 'S') or (tr_char == 'S' and bl_char == 'M')

                if diag1_is_valid_ms and diag2_is_valid_ms:
                    xmas_count += 1
    return xmas_count


array = []
with open("boss.txt", "r") as file:
    for n, line in enumerate(file.readlines()):
        line = [x for x in line.strip()]
        array.append(line)
print(count_xmas_patterns(array))
