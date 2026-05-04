import math 
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(delta_lambda / 2) ** 2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c
def optimize_route(reports, depot):
    """
    reports: list of dicts with 'id', 'latitude', 'longitude'
    depot: dict with 'latitude', 'longitude'
    """

    if not reports:
        return []

    unvisited = reports.copy()
    route = []

    current = depot

    while unvisited:
        nearest = None
        min_distance = float("inf")

        for report in unvisited:
            dist = haversine(
                current["latitude"],
                current["longitude"],
                report["latitude"],
                report["longitude"]
            )

            if dist < min_distance:
                min_distance = dist
                nearest = report

        route.append(nearest)
        unvisited.remove(nearest)
        current = nearest

    return route