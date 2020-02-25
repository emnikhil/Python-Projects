# Runs code on GPU
os.environ["THEANO_FLAGS"] = "device=cuda, assert_no_cpu_op=True"