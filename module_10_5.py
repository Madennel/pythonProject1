from concurrent.futures import ProcessPoolExecutor as Pool
import time

def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        line = f.readline()
        while line:
            all_data.append(line)
            line = f.readline()

filenames = [f'./file {number}.txt' for number in range(1, 5)]

start_time = time.time()
for file in filenames:
    read_info(file)
print(f"{time.time() - start_time} (линейный)")

start_time = time.time()
with Pool() as executor:
    executor.map(read_info, filenames)
print(f"{time.time() - start_time} (многопроцессный)")
