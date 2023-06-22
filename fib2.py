import fib.ola as emma
import fib.ola as fib2
emma.fib(200)
print(fib2.fib2(400))



if __name__ == "__main__":
    import sys
    emma.fib(int(sys.argv[3]))