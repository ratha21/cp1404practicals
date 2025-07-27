from unreliable_car import UnreliableCar

def main():
    """Test UnreliableCar by attempting to drive many times."""
    reliable_car = UnreliableCar("Always Works", 1000, reliability=100)
    unreliable_car = UnreliableCar("Sometimes Works", 1000, reliability=30)

    print("Testing 100% reliable car (should always drive):")
    reliable_successes = 0
    for _ in range(100):
        if reliable_car.drive(1) > 0:
            reliable_successes += 1
    print(f"Successful drives: {reliable_successes}/100")

    print("\nTesting 30% reliable car:")
    unreliable_successes = 0
    for _ in range(100):
        if unreliable_car.drive(1) > 0:
            unreliable_successes += 1
    print(f"Successful drives: {unreliable_successes}/100 (expected ~30)")

    assert reliable_successes == 100, "100% reliable car should always drive"
    assert 15 <= unreliable_successes <= 45, "30% car should succeed roughly 30 times"

if __name__ == "__main__":
    main()
