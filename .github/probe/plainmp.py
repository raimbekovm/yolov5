import multiprocessing as mp
def f(q): q.put(42)
if __name__ == "__main__":
    q = mp.Queue(); p = mp.Process(target=f, args=(q,)); p.start(); print("plain spawn", q.get(timeout=30)); p.join(); print("exit", p.exitcode)
