import matplotlib.pyplot as plt


def plot_spread(spread, zscore=None):
    """
    Plot spread and optional z-score.
    """
    fig, ax = plt.subplots(2 if zscore is not None else 1, 1, figsize=(10, 6))

    if zscore is None:
        ax.plot(spread)
        ax.set_title("Spread")
    else:
        ax[0].plot(spread)
        ax[0].set_title("Spread")

        ax[1].plot(zscore)
        ax[1].axhline(0)
        ax[1].axhline(2, linestyle="--")
        ax[1].axhline(-2, linestyle="--")
        ax[1].set_title("Z-Score")

    plt.tight_layout()
    plt.show()
