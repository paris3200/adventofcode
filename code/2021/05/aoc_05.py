def create_line(start, stop):
    """
    Creates all points on a line given the starting and stopping coordinates.

    Args:
        start (list): Starting point [x, y] of line.
        stop (list): Stopping point [x, y] of line.

    Returns:
        list: All points on line including the start and stop.
    """
    line = []
    # Horizontal Lines
    if start[0] == stop[0]:
        delta = stop[1] - start[1]
        for y in range(start[1], delta + 1):
            line.append([start[0], y])
        line.append(stop)

    # Vertical Lines
    elif start[1] == stop[1]:
        for y in range(stop[0], start[0]):
            line.append([y, start[1]])
        line.append(start)
        line.reverse()
    return line


def get_list_limits(coordinates):
    """
    Determines the x,y coordinates of the lower right corner of a grid
    that will contain all points in the coordinates list.

    Args:
        coordinates (list): List of coordinates [x,y]

    Returns:
        list: Lower right coordinate [x, y] of grid that can contain all points.
    """
    x = 0
    y = 0
    for point in coordinates:
        if point[0] > x:
            x = point[0]
        if point[1] > y:
            y = point[1]

    return [x, y]


def create_grid(end_point):
    """
    Creates a grid starting at [0,0] and going to the endpoint.

    Args:
        end_point (list): Coordinate of lower right point in the grid.

    Returns:
        list: Grid with `.` at each point on the grid.
    """
    grid = []
    for x in range(0, end_point[1] + 1):
        row = []
        for x in range(0, end_point[1] + 1):
            row.append(".")
        grid.append(row)
    return grid
