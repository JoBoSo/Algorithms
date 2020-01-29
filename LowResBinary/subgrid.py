from grids import *

## subgrid(grid, row_first, row_last, col_first, col_last) produces a grid
##     consisting of the entries in grid grid in rows row_first through row_last
##     and col_first through col_last, inclusive
## subgrid: Grid int int int int -> Grid
## Requires: 0 <= row_first <= row_last <= grid.rows
##           0 <= col_first <= col_last <= grid.cols
def subgrid(grid, row_first, row_last, col_first, col_last):
    number_rows = row_last - row_first + 1
    number_cols = col_last - col_first + 1
    result = Grid(number_rows, number_cols)
    for row in range(number_rows):
        for col in range(number_cols):
            result.enter(row, col, \
                         grid.access(row_first + row, col_first + col))
    return result

## subgrid_alt(grid, row_first, row_last, col_first, col_last) produces a grid
##     consisting of the entries in grid grid in rows row_first through row_last
##     and col_first through col_last, inclusive
# subgrid_alt: Grid int int int int -> Grid
## Requires: 0 <= row_first <= row_last <= grid.rows
##           0 <= col_first <= col_last <= grid.cols
def subgrid_alt(grid, row_first, row_last, col_first, col_last):
    number_rows = row_last - row_first + 1
    number_cols = col_last - col_first + 1
    result = Grid(number_rows, number_cols)
    row = 0
    while row < number_rows:
        col = 0
        while col < number_cols:
            result.enter(row, col, \
                         grid.access(row_first + row, col_first + col))
            col = col + 1
        row = row + 1
    return result
