#!/usr/bin/python3

if __name__ == "__main__":
    """Prints all the names defined by the compiled module hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)