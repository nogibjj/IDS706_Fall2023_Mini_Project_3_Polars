import polars as pl
import matplotlib.pyplot as plt


def data_filter(df):
    return df[df["Sex"] == "M"]


if __name__ == "__main__":
    data = pl.read_csv("./biostats.csv")
    print(data.describe())

    # create data visualization
    weight_col = data["Weight (lbs)"]
    numeric_weight = weight_col.to_numpy()

    plt.hist(numeric_weight, color="blue", alpha=0.7)
    plt.xlabel("Weight (lbs)")
    plt.ylabel("Count")
    plt.title("Histogram of Weight")
    plt.savefig("data_visualization.png")
