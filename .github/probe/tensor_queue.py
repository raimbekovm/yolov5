import sys, torch, torch.multiprocessing as mp
def f(q, kind):
    try:
        q.put(torch.zeros(3) if kind == "tensor" else 7)
    except BaseException as e:
        print("child exc", type(e).__name__, e, file=sys.stderr, flush=True); raise
if __name__ == "__main__":
    kind = sys.argv[1]
    print("strategy", mp.get_sharing_strategy())
    q = mp.Queue(); p = mp.Process(target=f, args=(q, kind)); p.start()
    try: print(kind, "->", q.get(timeout=20))
    except Exception as e: print(kind, "get failed", type(e).__name__)
    p.join(10); print("child exitcode", p.exitcode)
