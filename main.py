from lru_cache import LRUCache

cache = LRUCache(int(input("Enter Cache Capacity: ")))

while True:
    print("\n1.Put  2.Get  3.Delete  4.Display")
    print("5.Stats  6.Clear  7.Resize  8.Exit")

    ch = input("Choice: ")

    if ch == '1':
        k = input("Key: ")
        v = input("Value: ")
        ttl = input("TTL (seconds / blank): ")
        ttl = int(ttl) if ttl else None
        cache.put(k, v, ttl)

    elif ch == '2':
        k = input("Key: ")
        print("Value:", cache.get(k))

    elif ch == '3':
        print("Deleted" if cache.delete(input("Key: ")) else "Not Found")

    elif ch == '4':
        cache.display()

    elif ch == '5':
        print(cache.stats())

    elif ch == '6':
        cache.clear()
        print("Cache Cleared")

    elif ch == '7':
        cache.resize(int(input("New Capacity: ")))

    elif ch == '8':
        break
