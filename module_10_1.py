import time
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(word_count):
            f.write(f"Какое-то слово № {i + 1}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

if __name__ == "__main__":
    start_time = time.time()
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')
    end_time = time.time()
    print(f"Работа потоков {end_time - start_time}")

    start_time = time.time()
    threads = []
    for i in range(4):
        t = threading.Thread(target=write_words, args=(100, f'example{i + 5}.txt'))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    end_time = time.time()
    print(f"Работа потоков {end_time - start_time}")
