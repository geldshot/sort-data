from decorators.sortoutput import sortOutput
import random

def main():
    data = generate_data(100)
    print(data)

@sortOutput
def generate_data(num): 
    arr = [random.randint(0,100) for x in range(num)]
    return arr


if __name__ == '__main__':
    main()