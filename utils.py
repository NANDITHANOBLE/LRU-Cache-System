import json
import time
from node import Node

CACHE_FILE = "cache_data.json"


def save_cache(cache_obj):
    """
    Save cache data to JSON file
    """
    data = []

    current = cache_obj.head.next
    while current != cache_obj.tail:
        data.append({
            "key": current.key,
            "value": current.value,
            "ttl": current.ttl,
            "timestamp": current.timestamp
        })
        current = current.next

    payload = {
        "capacity": cache_obj.capacity,
        "cache": data,
        "hits": cache_obj.hits,
        "misses": cache_obj.misses
    }

    with open(CACHE_FILE, "w") as f:
        json.dump(payload, f, indent=4)

    print("Cache saved to file.")


def load_cache(cache_obj):
    """
    Load cache data from JSON file
    """
    try:
        with open(CACHE_FILE, "r") as f:
            payload = json.load(f)

        cache_obj.capacity = payload["capacity"]
        cache_obj.hits = payload.get("hits", 0)
        cache_obj.misses = payload.get("misses", 0)

        # Clear existing cache
        cache_obj.clear()

        for item in payload["cache"]:
            node = Node(item["key"], item["value"], item["ttl"])
            node.timestamp = item["timestamp"]

            cache_obj.cache[node.key] = node
            cache_obj._add_front(node)

        print("Cache loaded from file.")

    except FileNotFoundError:
        print("No saved cache found.")
