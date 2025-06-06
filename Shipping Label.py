
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")

shipping_label("Dr", "Emmanuel", "Okoh", "II",
               street="60 Shore Street,",
               apartment="313,",
               city="Winnipeg,",
               state="Manitoba.",
               postalcode="R3T2C8",
               country="Canada")