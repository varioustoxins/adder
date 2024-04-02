import sys

def main():
    numbers = [float(arg) for arg in sys.argv[1:]]
    
    print(sum(numbers))    

if __name__ == '__main__':
    main()

