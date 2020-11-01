import time
from functools import wraps

class time_this:
	"""Декоратор для подсчёта среднего значения времени для выполнения для передаваемой функции, 
	количество повторов передаётся как первый вргумент num_runs, по стандарту он равен 10. 
	Также можно использовать контекстный менеджер, но при этом замеряет время выполнения однократно"""

	def __init__(self, num_runs=10):
	    self.num_runs = num_runs

	def __call__(self, func):
		avg_time = 0
		for _ in range(self.num_runs):
			t0 = time.time()

			# <<полезный>> код
			func()

			t1 = time.time()
			avg_time += (t1 - t0)
		avg_time /= self.num_runs
		print("Выполнение заняло %.5f секунд" % avg_time)

	def __enter__(self):
		self.t0 = time.time()

	def __exit__(self, type, value, traceback):
		self.t1 = time.time()
		print("Выполнение заняло %.5f секунд" % (self.t1 - self.t0))



@time_this(num_runs=10)
def f():
    for j in range(1000000):
        pass


with time_this() as r:
	for j in range(1000000):
		pass