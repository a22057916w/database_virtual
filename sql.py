import multiprocessing as mp
import sys
sys.path.append("mysql/")
from sql_lease_TPE import SQL_LEASE_TPE
from sql_lease_NTC import SQL_LEASE_NTC
from sql_sells_TPE import SQL_SELLS_TPE
from sql_sells_NTC import SQL_SELLS_NTC

if __name__ == "__main__":
    func = [SQL_LEASE_TPE, SQL_LEASE_NTC, SQL_SELLS_TPE, SQL_SELLS_NTC]
    p = [None] * 4
    for i in range(0, 4):
        p[i] = mp.Process(target = func[i])
        p[i].start()
    for i in range(0, 4):
        p[i].join()
    for i in range(0, 4):
        p[i].close()
