import time
import datetime
import threading

def background(func):
  """
  """
  def wrapper(*args, **kwargs):
    thread = threading.Thread(target=func, args=args, kwargs=kwargs)
    #thread.daemon = True # if True backgound function/process stops with foreground execution, else keeps on running until manually stopped or function completes its code
    thread.start()
  return wrapper

@background
def function_to_run_in_background(*args, **kwargs):
  # do some stuff like below
  while True:
    # this is infinite loop, finite loops are advised 
    print(datetime.datetime.now().__str__() + f' : {self.__name__} running in background')
    time.sleep(1)

if __name__ == "__main__":
  function_to_run_in_background()
  for i in range(10):
    print(datetime.datetime.now().__str__() + f' : {self.__name__} running in foreground')
