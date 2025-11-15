def peel():
    return "Here's a delicious banana!"


def dip_in_chocolate():
    return "Here's a delicious banana, dipped in chocolate!"


def sell():
    return "There's always money in the banana stand."

#this runs only when this module is run directly, not when imported
if __name__ == "__main__":
    print(sell())
