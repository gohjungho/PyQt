import multiprocessing as mp
import time 

def worker():
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)
    time.sleep(5)
    print("SubProcess End")

# 현재 위치의 파일에서만 실행. import로 읽어가지 않음
if __name__ == "__main__": # 문법이므로 이대로 쓸 것!
    # main process 
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)

    #process spawning 
    p = mp.Process(name = "SubProcess", target = worker)
    p.start()

    print("MainProcess End")