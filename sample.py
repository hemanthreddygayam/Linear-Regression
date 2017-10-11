import numpy as np


def sigmoid(x):
    """
    Calculate sigmoid
    """
    return 1 / (1 + np.exp(-x))

def main():
    print sigmoid(0.06)
    print sigmoid(-0.46)
    print sigmoid(-0.00645945)
if __name__ == "__main__":
    main()