import multiprocessing

def collatz_check(start, end, result_queue):
    for n in range(start, end):
        current = n
        while current != 1:
            if current % 2 == 0:
                current //= 2
            else:
                current = 3 * current + 1
        result_queue.put(n)

def worker(task_queue, result_queue):
    while not task_queue.empty():
        try:
            start, end = task_queue.get_nowait()
            collatz_check(start, end, result_queue)
        except:
            break

def main():
    start = 1
    end = 1000000000
    process_count = multiprocessing.cpu_count()
    chunk_size = 1000000


    task_queue = multiprocessing.Queue()
    result_queue = multiprocessing.Queue()


    for i in range(start, end, chunk_size):
        task_queue.put((i, min(i + chunk_size, end)))


    processes = []
    for _ in range(process_count):
        p = multiprocessing.Process(target=worker, args=(task_queue, result_queue))
        processes.append(p)
        p.start()


    for p in processes:
        p.join()

    print("Collatz conjecture from 1 to", end)

#Option 2
# def collatz(n):
#     seq = [n]
#     while n != 1:
#         if n % 2 == 0:
#             n = n // 2
#         else:
#             n = 3 * n + 1
#         seq.append(n)
#     return seq
#
# def test_collatz_conjecture(start, end):
#     for i in range(start, end + 1):
#         seq = collatz(i)
#         print(f'The collatz sequence of {i} is {seq}')
#
# def main():
#     try:
#         number = int(input("Enter a positive integer: "))
#         if number <= 0:
#             print("Please enter a positive integer.")
#             return
#         seq= collatz(number)
#         print("Collatz sequence:", seq)
#     except ValueError:
#         print("Invalid input. Please enter a valid integer.")
if __name__ == "__main__":
    main()

