import time

start_time = time.perf_counter()
def tribonacci(num):
    cache = {1: 1, 2: 1, 3: 1}
    def rec_trib(num):
        result = cache.get(num)
        if result is None:
            result = rec_trib(num - 1) + rec_trib(num - 2) + rec_trib(num - 3)
            cache[num] = result

        print(cache)
        return result
    return rec_trib(num)


print(tribonacci(30))


