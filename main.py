import os 
from Preprocess import *
import sys
    
def main():
    url = sys.argv[1] 
    import_data(url)
    
if __name__ == "__main__":
    main()