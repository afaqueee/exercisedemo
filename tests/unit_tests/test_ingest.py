import sys
import pandas as pd
from src.package.score import score_values

sys.path.append("...")


def test_null():
    df1 = pd.read_csv("data/train/train.csv")
    assert df1.isna().sum().sum() == 0

    df2 = pd.read_csv("data/test/test.csv")
    assert df2.isna().sum().sum() == 0


def test_one_hot_encode():
    df1 = pd.read_csv("data/train/train.csv")
    assert df1["ocean_proximity_INLAND"].isin([0, 1]).all()
    assert df1["ocean_proximity_ISLAND"].isin([0, 1]).all()
    assert df1["ocean_proximity_NEAR BAY"].isin([0, 1]).all()
    assert df1["ocean_proximity_NEAR OCEAN"].isin([0, 1]).all()

    df2 = pd.read_csv("data/test/test.csv")
    assert df2["ocean_proximity_INLAND"].isin([0, 1]).all()
    assert df2["ocean_proximity_ISLAND"].isin([0, 1]).all()
    assert df2["ocean_proximity_NEAR BAY"].isin([0, 1]).all()
    assert df2["ocean_proximity_NEAR OCEAN"].isin([0, 1]).all()


def test_score():
    result = score_values()
    assert result[0] == 4477408708.672473  # Linear Regression MSE
    assert result[1] == 66913.44191320958  # Linear Regression RSME
    assert result[2] == 49234.73616908966  # Linear Regression MAE
    assert result[3] == 4953618206.538033  # Decision Tree MSE
    assert result[4] == 70381.94517444109  # Decision Tree RSME
    assert result[5] == 45366.59132751938  # Decision Tree MAE
    assert result[6] == 2287726760.037806  # Random Forest MSE
    assert result[7] == 47830.186702936946  # Random Forest RSME
    assert result[8] == 32046.821842700258  # Random Forest MAE


def test_column_check():
    df1 = pd.read_csv("data/train/train.csv")
    df2 = pd.read_csv("data/test/test.csv")

    a = df1.shape[1]
    b = df2.shape[1]

    assert a == b
