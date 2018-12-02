from cyaron import *

_n = ati([0, 1, 5, 10, 100, 1000, 5000, 10000, 50000, 100000, 100000])

for i in range(1, 11):
    test_data = IO(file_prefix="huffman_", data_id=i, disable_output=True)
    n = _n[i]
    s = String.random(n) if i < 10 else 'a' * n
    test_data.input_writeln(s)
