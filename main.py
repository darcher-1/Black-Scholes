import os 
from Preprocess import *
import sys
from compute_black_scholes import *
    
def main():
    url = sys.argv[1] 
    print(url)
    import_data(url)
    
if __name__ == "__main__":
    main()