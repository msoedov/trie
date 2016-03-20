### Run

The solution works both with python2/python3 and pypy2/pypy3. It runs significantly faster with py3 comparing to py2.

``` shell
python3 main.py fike camp
['fike', 'fake', 'fame', 'came', 'camp']
```
Or build the docker image and run inside of container

```shell
➜  trie git:(master) ✗ docker build -t word-paths .
Sending build context to Docker daemon 6.284 MB
Step 1 : FROM python:3.5
---> e7814e9068f6
Step 2 : COPY . /app
---> Using cache
---> 5f327408fd96
Step 3 : WORKDIR /app
---> Using cache
---> 83e7825c700c
Successfully built 83e7825c700c
➜  trie git:(master) ✗ docker run -it word-paths python3 main.py fike camp -d
Loaded in 0.29026317596435547
Here we go: ['fike', 'fake', 'cake', 'came', 'camp']
['fike', 'fake', 'cake', 'came', 'camp']

```

### Command line options

`-d` is debug cli flag
`-r` rebuild the cache file, this can take 1-2 hours on descent laptop

### Notes
It won't work with `pypy` as is due incompatibility of pickle protocol between `cPython` and `PyPy` so in case you wanna run it with pypy you need to rebuild cached file.

### Author

Alex Myasoedov msoedov@gmail.com
