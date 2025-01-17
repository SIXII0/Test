import time

for i in range(101):
    print(f"\r{i:3}%",end=' ')
    time.sleep(0.05)