from threading import Thread


def counter_even():
  for i in range(0, 10, 2):
    print(i)


def counter_odd():
  for i in range(1, 10, 2):
    print(i)


thread1 = Thread(target=counter_odd)
thread2 = Thread(target=counter_even)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
