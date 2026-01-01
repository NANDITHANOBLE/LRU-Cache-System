from lru_cache import LRUCache
import time

def test_basic_put_get():
    print("TEST 1: Basic PUT & GET")
    cache = LRUCache(2)

    cache.put(1, "A")
    cache.put(2, "B")

    assert cache.get(1) == "A"
    assert cache.get(2) == "B"
    print("✔ Passed\n")


def test_lru_eviction():
    print("TEST 2: LRU Eviction")
    cache = LRUCache(2)

    cache.put(1, "A")
    cache.put(2, "B")
    cache.get(1)          # Make key 1 MRU
    cache.put(3, "C")     # Evicts key 2

    assert cache.get(2) == -1
    assert cache.get(1) == "A"
    assert cache.get(3) == "C"
    print("✔ Passed\n")


def test_update_existing_key():
    print("TEST 3: Update Existing Key")
    cache = LRUCache(2)

    cache.put(1, "A")
    cache.put(1, "Updated")

    assert cache.get(1) == "Updated"
    print("✔ Passed\n")


def test_delete_key():
    print("TEST 4: Delete Key")
    cache = LRUCache(2)

    cache.put(1, "A")
    cache.delete(1)

    assert cache.get(1) == -1
    print("✔ Passed\n")


def test_cache_clear():
    print("TEST 5: Clear Cache")
    cache = LRUCache(2)

    cache.put(1, "A")
    cache.put(2, "B")
    cache.clear()

    assert cache.get(1) == -1
    assert cache.get(2) == -1
    print("✔ Passed\n")


def test_resize_cache():
    print("TEST 6: Resize Cache")
    cache = LRUCache(3)

    cache.put(1, "A")
    cache.put(2, "B")
    cache.put(3, "C")

    cache.resize(2)   # Should remove LRU (key 1)

    assert cache.get(1) == -1
    assert cache.get(2) == "B"
    assert cache.get(3) == "C"
    print("✔ Passed\n")


def test_cache_stats():
    print("TEST 7: Cache Hit/Miss Stats")
    cache = LRUCache(2)

    cache.put(1, "A")
    cache.get(1)      # hit
    cache.get(2)      # miss

    stats = cache.stats()
    assert stats["hits"] == 1
    assert stats["misses"] == 1
    print("✔ Passed\n")


def test_ttl_expiry():
    print("TEST 8: TTL Expiry")
    cache = LRUCache(2)

    cache.put(1, "A", ttl=2)
    time.sleep(3)

    assert cache.get(1) == -1
    print("✔ Passed\n")


# ----------------- RUN ALL TESTS -----------------

if __name__ == "__main__":
    test_basic_put_get()
    test_lru_eviction()
    test_update_existing_key()
    test_delete_key()
    test_cache_clear()
    test_resize_cache()
    test_cache_stats()
    test_ttl_expiry()

    print("🎉 ALL TESTS PASSED SUCCESSFULLY 🎉")
