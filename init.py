import multiprocessing as mp
import sys
sys.path.append("sells/")
sys.path.append("lease/")
sys.path.append("mysql/")
from SELLS_INIT import SELLS_INIT
from LEASE_INIT import LEASE_INIT
from MYSQL_INIT import MYSQL_INIT

if __name__ == "__main__":
    # 爬資料
    ps = mp.Process(target = SELLS_INIT)
    pl = mp.Process(target = LEASE_INIT)
    ps.start()
    pl.start()
    ps.join()
    pl.join()
    ps.close()
    pl.close()
    # 載完資料後上傳MYSQL
    psql = mp.Process(target = MYSQL_INIT)
    psql.start()
    psql.join()
    psql.close()
