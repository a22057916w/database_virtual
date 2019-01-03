import multiprocessing as mp
from sells_score_TPE import SELLS_SCORE_TPE
from sells_score_NTC import SELLS_SCORE_NTC
from lease_score_TPE import LEASE_SCORE_TPE
from lease_score_NTC import LEASE_SCORE_NTC

def GRADING_INIT():
    func = [SELLS_SCORE_TPE, SELLS_SCORE_NTC, LEASE_SCORE_TPE, LEASE_SCORE_NTC]
    index = len(func)
    p = [None] * index
    for i in range(0, index):
        p[i] = mp.Process(target = func[i])
        p[i].start()
    for i in range(0, index):
        p[i].join()
    for i in range(0, index):
        p[i].close()
