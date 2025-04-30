digitos = [[" _ ", "| |", "|_|", "   "],
          ["   ", "  |", "  |", "   "],
          [" _ ", " _|", "|_ ", "   "],
          [" _ ", " _|", " _|", "   "],
          ["   ", "|_|", "  |", "   "],
          [" _ ", "|_ ", " _|", "   "],
          [" _ ", "|_ ", "|_|", "   "],
          [" _ ", "  |", "  |", "   "],
          [" _ ", "|_|", "|_|", "   "],
          [" _ ", "|_|", " _|", "   "]]

def convert(input_grid):
    if len(input_grid)%4==0:
        if len(input_grid[0])%3==0:
            dato=""
            for j in range(0,len(input_grid),4):
                for k in range(0,len(input_grid[0]),3):
                    numero_ocr=[]
                    for i in range(4):
                        numero_ocr.append(input_grid[i+j][k:k+3])
                    dato+=identificar(numero_ocr)
            return dato
        raise ValueError("Number of input columns is not a multiple of three")
    raise ValueError("Number of input lines is not a multiple of four")

def identificar(input_grid):
    for grid in digitos:
        if grid == input_grid:
            return str(digitos.index(grid))
    return '?'