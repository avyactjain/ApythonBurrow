import stdio
import stdarray

def _flow(isOpen, isFull, i, j):
    n = len(isFull)
    if (i < 0) or (i >= n):
        return
    if (j < 0) or (j >= n):
        return
    if not isOpen[i][j]:
        return
    if isFull[i][j]:
        return
    isFull[i][j] = True
    _flow(isOpen, isFull, i+1, j  )  # Down.
    _flow(isOpen, isFull, i  , j+1)  # Right.
    _flow(isOpen, isFull, i  , j-1)  # Left.
    _flow(isOpen, isFull, i-1, j  )  # Up.


def flow(isOpen):
    n = len(isOpen)
    isFull = stdarray.create2D(n, n, False)
    for j in range(n):
        _flow(isOpen, isFull, 0, j)
    return isFull

def percolates(isOpen):
    
    # Compute the full sites of the system.
    isFull = flow(isOpen)
    
    # If any site in the bottom row is full, then the system
    # percolates.
    n = len(isFull)
    for j in range(n):
        if isFull[n-1][j]:
            return True
    return False

def main():
    isOpen = stdarray.readBool2D()
    stdarray.write2D(flow(isOpen))
    stdio.writeln(percolates(isOpen))

    #isOpen = stdarray.readBool2D()
    #stdarray.write2D(flow(isOpen))
    #draw(isOpen, False)
    #stddraw.setPenColor(stddraw.BLUE)
    #draw(flow(isOpen), True)
    #stdio.writeln(percolates(isOpen))
    #stddraw.show()

if __name__ == '__main__':
    main()