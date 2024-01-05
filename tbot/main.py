import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    python_version = sys.version.split()[0]

    if sys.version_info < (3, 9):
        print("Sherlock requires Python 3.6+\nYou are using Python %s, which is not supported by Sherlock" % (
            python_version))
        sys.exit(1)

    import jarvis
    jarvis.main()
