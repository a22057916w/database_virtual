import multiprocessing as mp
import sys
sys.path.append("grading/")
from gtest2 import GTEST2

if __name__ == "__main__":

    p = mp.Process(target = GTEST2)
    p.start()
    p.join()
    p.close()
