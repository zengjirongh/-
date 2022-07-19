def search_small_stations(states_needs, stations):
    finall_stations = set()
    while states_needs:
        best_stations = None
        stations_cover = set()
        for station, states_for_station in stations.items():
            covers = states_for_station & states_needs
            if len(covers) > len(stations_cover):
                stations_cover = covers
                best_stations = station

        states_needs -= stations_cover
        finall_stations.add(best_stations)
    return finall_stations


if __name__ == '__main__':
    states_needs = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
    stations = {
        "kone": {"id", "nv", "ut"},
        "ktwo": {"wa", "id", "mt"},
        "kthree": {"or", "nv", "ca"},
        "kfour": {"nv", "ut"},
        "kfive": {"ca", "az"}
    }
    print(search_small_stations(states_needs, stations))
