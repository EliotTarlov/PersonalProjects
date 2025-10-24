import slangpy as spy
import pathlib
import numpy as np
device = spy.create_device(include_paths=[\
    pathlib.Path(__file__).parent.absolute(),\
])
module = spy.Module.load_from_file(device,"example.slang")

a = np.random.rand(1*10**6).astype(np.float32)
b = np.random.rand(1*10**6).astype(np.float32)
result = module.add(a, b, _result='numpy')
print(result[:100])
