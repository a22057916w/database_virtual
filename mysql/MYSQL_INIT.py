import multiprocessing as mp
from sql_lease_TPE import SQL_LEASE_TPE
from sql_lease_NTC import SQL_LEASE_NTC
from sql_lease_IMG import SQL_LEASE_IMG
from sql_lease_score_TPE import SQL_LEASE_SCORE_TPE
from sql_lease_score_NTC import SQL_LEASE_SCORE_NTC
from sql_lease_total_TPE import SQL_LEASE_TOTAL_TPE
from sql_lease_total_NTC import SQL_LEASE_TOTAL_NTC
from sql_sells_TPE import SQL_SELLS_TPE
from sql_sells_NTC import SQL_SELLS_NTC
from sql_sells_IMG import SQL_SELLS_IMG
from sql_sells_score_TPE import SQL_SELLS_SCORE_TPE
from sql_sells_score_NTC import SQL_SELLS_SCORE_NTC
from sql_sells_total_TPE import SQL_SELLS_TOTAL_TPE
from sql_sells_total_NTC import SQL_SELLS_TOTAL_NTC


def MYSQL_INIT():
    func = [SQL_LEASE_TPE, SQL_LEASE_NTC, SQL_LEASE_IMG, SQL_SELLS_TPE, SQL_SELLS_NTC, SQL_SELLS_IMG, SQL_LEASE_TOTAL_TPE, SQL_LEASE_TOTAL_NTC, SQL_SELLS_TOTAL_TPE, SQL_SELLS_TOTAL_NTC, SQL_LEASE_SCORE_TPE, SQL_LEASE_SCORE_NTC, SQL_SELLS_SCORE_TPE, SQL_SELLS_SCORE_NTC]
    index = len(func)
    p = [None] * index
    for i in range(0, index):
        p[i] = mp.Process(target = func[i])
        p[i].start()
    for i in range(0, index):
        p[i].join()
    for i in range(0, index):
        p[i].close()
