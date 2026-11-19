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
    print(sys.argv)

    check_joint(LIMITS, 10, LIMITS[i])
    # for joint in LIMITS:
        # print(f"{joint}: {LIMITS[joint]}")



if __name__ == "__main__":
    main()