import multiprocessing as mp
from sql_lease_TPE import SQL_LEASE_TPE
from sql_lease_NTC import SQL_LEASE_NTC
from sql_lease_IMG import SQL_LEASE_IMG
from sql_sells_TPE import SQL_SELLS_TPE
from sql_sells_NTC import SQL_SELLS_NTC
from sql_sells_IMG import SQL_SELLS_IMG

def MYSQL_INIT():
    func = [SQL_LEASE_TPE, SQL_LEASE_NTC, SQL_LEASE_IMG, SQL_SELLS_TPE, SQL_SELLS_NTC, SQL_SELLS_IMG]
    p = [None] * 6
    for i in range(0, 6):
        p[i] = mp.Process(target = func[i])
        p[i].start()
    for i in range(0, 6):
        p[i].join()
    for i in range(0, 6):
        p[i].close()
