import multiprocessing as mp
import sys
sys.path.append("grading/")
from test import TEST

if __name__ == "__main__":

    p = mp.Process(target = TEST)
    p.start()
    p.join()
    p.close()
