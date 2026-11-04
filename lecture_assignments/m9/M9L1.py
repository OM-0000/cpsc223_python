#! /usr/bin/python3.12
import mylib

def main():
    print("Hello")


print('before call')
mylib.do_something()
print('after call')
if __name__ == "__main__":
    main()