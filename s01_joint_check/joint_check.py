import sys


LIMITS = {
    "J1": (-170, 170),
    "J2": (-120, 120),
    "J3": (-150, 150),
    "J4": (-180, 180),
    "J5": (-120, 120),
    "J6": (-180, 180),
}


def main():
    print(sys.argv)
    for joint in LIMITS:
        print(f"{joint}: {LIMITS[joint]}")


if __name__ == "__main__":
    main()