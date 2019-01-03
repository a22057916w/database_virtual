import multiprocessing as mp
import sys
sys.path.append("grading/")
from GRADING_INIT import GRADING_INIT

if __name__ == "__main__":
    func = [GRADING_INIT]
    index = len(func)
    p = [None] * index
    for i in range(0, index):
        p[i] = mp.Process(target = func[i])
        p[i].start()
    for i in range(0, index):
        p[i].join()
    for i in range(0, index):
        p[i].close()
