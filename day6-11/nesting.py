capitals = {
    "France": "paris",
    "Spain" : "Madrid",
    "Germany": "berlin"
}

# nesting

travel_log = {
    "Spain" : ["Madrid","Sevilla","Cadiz"]
}

travel_log["Spain"].append("Valencia")

print(travel_log)