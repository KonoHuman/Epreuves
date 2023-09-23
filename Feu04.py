import sys

# Fonction pour afficher la grille du Sudoku
def print_sudoku(grid):
    for row in grid:
        print("".join(map(str, row)))

# Fonction pour vérifier si une valeur peut être placée dans une cellule
def is_safe(grid, row, col, num):
    # Vérifier la ligne
    if num in grid[row]:
        return False

    # Vérifier la colonne
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Vérifier le carré 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True

# Fonction récursive pour résoudre le Sudoku
def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == '.':
                for num in map(str, range(1, 10)):
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = '.'  # Annuler la tentative si elle ne mène pas à une solution
                return False  # Aucune valeur possible n'a fonctionné ici
    return True  # La grille est complète

if __name__ == "__main__":
    # Vérifier les arguments de ligne de commande
    if len(sys.argv) != 2:
        print("Usage: python sudoku_solver.py input_file.txt")
        sys.exit(1)

    input_file = sys.argv[1]

    # Lire la grille Sudoku depuis le fichier d'entrée
    try:
        with open(s.txt, "r") as file:
            sudoku_grid = [list(line.strip()) for line in file]
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

    # Assurez-vous que la grille a la bonne taille
    if len(sudoku_grid) != 9 or any(len(row) != 9 for row in sudoku_grid):
        print("Error: Invalid Sudoku grid.")
        sys.exit(1)

    # Résoudre le Sudoku
    if solve_sudoku(sudoku_grid):
        print_sudoku(sudoku_grid)
    else:
        print("No solution found.")
