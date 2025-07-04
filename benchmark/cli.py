if __name__ == "__main__":
    email = input("Enter email to check: ")
    from benchmark.compare import compare_lookup

    print(compare_lookup(email))
