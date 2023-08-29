import struct
import random

def opener():
    with open('v8_context_snapshot.bin', 'rb') as f1:
        coded_bin = f1.read()

        random_number = random.randint(490000, 580000)

        while random_number != 0:
            x = 1
            try:
                x = str(random_number) + 'B'
                uncoded_bin1 = struct.unpack(x, coded_bin)
                print(uncoded_bin1)
                break
            except struct.error:
                print(f'Число {random_number} не подошло')
                random_number = random.randint(490000, 580000)
                continue

print(opener())