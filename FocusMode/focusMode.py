blockSites = ["www.linkedin.com", "linkedin.com",
              "www.twitter.com", "twitter.com"]


def blockSite():
    redirect = "127.0.0.1"
    with open("/etc/hosts", "a") as file:
        for i in blockSites:
            file.write(redirect + " " + i + "\n")


def freeSite():
    with open("/etc/hosts", "r") as f:
        lines = f.readlines()
    with open("/etc/hosts", "w") as f:
        for line in lines:
            if all(n not in line.strip("\n") for n in blockSites):
                f.write(line)


if __name__ == "__main__":
    with open("/etc/hosts", "r") as f:
        lines = f.read().splitlines()
    if any(blockSites[0] in line for line in lines):
        freeSite()
    else:
        blockSite()
