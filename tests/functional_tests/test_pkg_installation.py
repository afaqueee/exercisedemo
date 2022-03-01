def test_pkg_install():

    try:
        import housing_package
    except ImportError as e:
        print(e)


if __name__ == "__main__":
    test_pkg_install()
