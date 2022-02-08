import os.path


def test_train_data():
    assert os.path.exists("data/models/linear_regression.pkl")
    assert os.path.exists("data/models/randomforest_regression.pkl")
    assert os.path.exists("data/models/tree_regression.pkl")


if __name__ == "__main__":
    test_train_data()
