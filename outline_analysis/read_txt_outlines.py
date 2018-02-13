def txtToDict(txtfile):
    """Read vertices from a text file of (Lon, Lat) coords.

    Input file represents a single polygon with a single line list of comma-separated
    vertices, e.g.: "<lon>, <lat>, <lon>, <lat>, ...".
    """
    with open(txtfile) as f:
        polygon = f.readline()
        if not polygon:
            return None
    vertices = [float(val) for val in polygon.strip().split(",")]
    d = {}
    d["Lon"] = vertices[::2]
    d["Lat"] = vertices[1::2]
    if len(d["Lon"]) != len(d["Lat"]):
        raise RuntimeError("Invalid input.")
    return d
