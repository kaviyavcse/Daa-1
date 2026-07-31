class Bin:
    """Class representing a Bin with a fixed capacity."""
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    @property
    def remaining_space(self):
        return self.capacity - sum(self.items)

    def add_item(self, item):
        if self.remaining_space >= item:
            self.items.append(item)
            return True
        return False

    def __repr__(self):
        return f"Bin(Items: {self.items}, Used: {sum(self.items)}/{self.capacity})"


def first_fit(items, capacity):
    """
    Places each item in the FIRST bin that has enough space.
    If no bin can fit the item, opens a new bin.
    """
    bins = []

    for item in items:
        placed = False
        for b in bins:
            if b.remaining_space >= item:
                b.add_item(item)
                placed = True
                break

        if not placed:
            new_bin = Bin(capacity)
            new_bin.add_item(item)
            bins.append(new_bin)

    return bins


def first_fit_decreasing(items, capacity):
    """
    Sorts items in decreasing order, then applies First Fit algorithm.
    """
    sorted_items = sorted(items, reverse=True)
    return first_fit(sorted_items, capacity)


def best_fit_decreasing(items, capacity):
    """
    Sorts items in decreasing order, then places each item in the bin 
    that leaves the MINIMUM remaining space (tightest fit).
    """
    sorted_items = sorted(items, reverse=True)
    bins = []

    for item in sorted_items:
        best_bin = None
        min_space_left = float('inf')

        # Find the bin with the tightest fit that can accommodate the item
        for b in bins:
            space_left = b.remaining_space - item
            if space_left >= 0 and space_left < min_space_left:
                best_bin = b
                min_space_left = space_left

        if best_bin is not None:
            best_bin.add_item(item)
        else:
            new_bin = Bin(capacity)
            new_bin.add_item(item)
            bins.append(new_bin)

    return bins


# --- Demonstration & Testing ---
if __name__ == "__main__":
    # Test Data
    items = [2, 5, 4, 7, 1, 3, 8, 6, 4]
    capacity = 10

    print("=" * 60)
    print(f"Items to pack : {items}")
    print(f"Bin Capacity  : {capacity}")
    print("=" * 60)

    # 1. First Fit
    ff_bins = first_fit(items, capacity)
    print(f"\n--- 1. First Fit (Total Bins: {len(ff_bins)}) ---")
    for i, b in enumerate(ff_bins, 1):
        print(f"  Bin {i}: {b.items} (Sum: {sum(b.items)})")

    # 2. First Fit Decreasing
    ffd_bins = first_fit_decreasing(items, capacity)
    print(f"\n--- 2. First Fit Decreasing (Total Bins: {len(ffd_bins)}) ---")
    for i, b in enumerate(ffd_bins, 1):
        print(f"  Bin {i}: {b.items} (Sum: {sum(b.items)})")

    # 3. Best Fit Decreasing
    bfd_bins = best_fit_decreasing(items, capacity)
    print(f"\n--- 3. Best Fit Decreasing (Total Bins: {len(bfd_bins)}) ---")
    for i, b in enumerate(bfd_bins, 1):
        print(f"  Bin {i}: {b.items} (Sum: {sum(b.items)})")
