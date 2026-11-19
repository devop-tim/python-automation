import sys


LIMITS = {
    "J1": (-170, 170),
    "J2": (-120, 120),
    "J3": (-150, 150),
    "J4": (-180, 180),
    "J5": (-120, 120),
    "J6": (-180, 180),
}


def check_joint(name, angle, limits):
    low, high = limits[name]
    return low <= angle <= high


def main():
    args = sys.argv[1:]
    angles = []

    for arg in args:
        angles.append(float(arg))
    print(angles)

    print(check_joint("J1", 10, LIMITS))
    print(check_joint("J6", 200, LIMITS))
    print(check_joint("J2", -120, LIMITS))
    for joint in LIMITS:
        print(f"{joint}: {LIMITS[joint]}")


if __name__ == "__main__":
    main()