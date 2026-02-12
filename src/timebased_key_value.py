import time
import bisect
from collections import defaultdict

class TimeBasedKV:
    def __init__(self):
        # Dictionary to store data
        # Key -> Object containing two parallel lists: 'times' and 'values'
        # We use parallel lists to make binary search (bisect) easier on timestamps
        self.store = defaultdict(lambda: {'times': [], 'values': []})

    def set(self, key: str, value: str) -> int:
        """
        Part 1 & 2: Set value.
        Stores the value and returns the generated timestamp (in milliseconds).
        """
        # 1. Generate timestamp (milliseconds)
        timestamp = int(time.time() * 1000)
        
        # 2. Append to history
        # Since time is monotonic, these lists remain sorted automatically.
        self.store[key]['times'].append(timestamp)
        self.store[key]['values'].append(value)
        
        return timestamp

    def get(self, key: str, timestamp: int = None) -> str:
        """
        Part 1, 2 & 3: Get value.
        If timestamp is None, returns latest.
        Otherwise, returns the value at (or just before) the given timestamp.
        """
        if key not in self.store:
            return None
            
        history = self.store[key]
        
        # Part 1: Get latest (no timestamp provided)
        if timestamp is None:
            return history['values'][-1] if history['values'] else None

        # Part 2 & 3: Time-based retrieval
        # We use bisect_right to find the insertion point for the given timestamp.
        # This returns the index where the timestamp *would* go to maintain order.
        # The element immediately to the left (index - 1) is the one we want.
        idx = bisect.bisect_right(history['times'], timestamp)
        
        # Case: Timestamp is older than the very first entry
        if idx == 0:
            return None
            
        # Return the value at the found index
        return history['values'][idx - 1]

# --- Usage Example ---
if __name__ == "__main__":
    kv = TimeBasedKV()

    # 1. Set first value
    t1 = kv.set("foo", "bar")
    print(f"Set 'foo'='bar' at: {t1}")

    time.sleep(1)  # Wait 1 second

    # 2. Set second value
    t2 = kv.set("foo", "bar2")
    print(f"Set 'foo'='bar2' at: {t2}")

    print("\n--- Results ---")
    
    # Part 1: Get latest
    print(f"Latest: {kv.get('foo')}")  # Returns "bar2"

    # Part 2: Get exact timestamp (t1)
    print(f"At t1: {kv.get('foo', t1)}")  # Returns "bar"

    # Part 3: Get fuzzy timestamp (t1 + 500ms)
    # This searches for a time between t1 and t2
    print(f"At t1 + 500ms: {kv.get('foo', t1 + 500)}")  # Returns "bar"
