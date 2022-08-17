from shortcuts import dictOverviewSheet


def sheet():
    print("--------------Shortcut Sheet--------------\n")
    for key, value in dictOverviewSheet.items():
        print(key + ": " + value + "\n")
    print("------------------------------------------")


if __name__ == "__main__":
    sheet()
