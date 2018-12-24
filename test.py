import multiprocessing as mp
import sys
sys.path.append("grading/")
from gtest import GTEST

if __name__ == "__main__":

    p = mp.Process(target = GTEST)
    p.start()
    p.join()
    p.close()
