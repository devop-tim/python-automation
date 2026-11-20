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

    for angle,joint in zip(angles,LIMITS):
        if check_joint(joint, angle, LIMITS):
            print(f"{joint}: {angle} OK")
        else:
            print(f"{joint}: {angle} OUT OF RANGE")


if __name__ == "__main__":
    main()