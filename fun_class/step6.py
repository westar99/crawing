# -*- coding: utf-8 -*-

import contextlib
import time 

@contextlib.contextmanager
def timer():
    # 시간 측정

    start = time.time()
    yield 
    end = time.time()
    print("(시간측정(Elapsed): {:.2f} 초)".format(end-start))

def main():
    with timer():
        print("얼마나 오래 걸릴까요?")
        time.sleep(1)

if __name__ == "__main__":
    main()