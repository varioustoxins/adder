import sys



def add(*args):
    strings = list(*args)
    numbers = [float(arg) for arg in strings]
    
    return sum(numbers)

def main():
    
    print(add(sys.argv[1:]))    

if __name__ == '__main__':
    main()

