import time

class Timer:
    _start = None
    _end = None

    def start(self):
        self._start = time.time()

    def stop(self):
        self._end = time.time()

    def get_elapsed(self):
        return self._end - self._start
    
    def reset(self):
        self._start = None
        self._end = None

def first_n_generator(n):
    value = 0

    while value < n:
        yield value 
        value += 1

def first_n_creator(n):
    value, numbers = 0, []
    while value < n:
        numbers.append(value)
        value += 1

    return numbers

if __name__ == "__main__":
    timer = Timer()

    timer.start()
    sum(first_n_generator(100000000))
    timer.stop()
    print(f"Generator took: {timer.get_elapsed()} seconds...")
    timer.reset()

    timer.start()
    sum(first_n_creator(100000000))
    timer.stop()
    print(f"List creator took: {timer.get_elapsed()} seconds...")
    