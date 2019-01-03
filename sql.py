import multiprocessing as mp
import sys
sys.path.append("mysql/")
from sql_lease_score_NTC import SQL_LEASE_SCORE_NTC


if __name__ == "__main__":
    func = [SQL_LEASE_SCORE_NTC]
    index = len(func)
    p = [None] * index
    for i in range(0, index):
        p[i] = mp.Process(target = func[i])
        p[i].start()
    for i in range(0, index):
        p[i].join()
    for i in range(0, index):
        p[i].close()
