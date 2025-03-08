name = "mrapy"
version = "0.1.0"

build_command = "python {root}/rezbuild.py {install}"

def commands():
    env.PYTHONPATH.append('{root}/src')
    env.PATH.append('{root}/bin')
