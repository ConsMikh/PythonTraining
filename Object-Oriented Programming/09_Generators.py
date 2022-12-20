# pylint: disable = pointless-string-statement

inname = '''
Jan 26, 2015 11:25:25 DEBUG This is a debugging message. 
Jan 26, 2015 11:25:36 INFO This is an information method. 
Jan 26, 2015 11:25:46 WARNING This is a warning. It could be serious. 
Jan 26, 2015 11:25:52 WARNING Another warning sent. 
Jan 26, 2015 11:25:59 INFO Here's some information.
Jan 26, 2015 11:26:13 DEBUG Debug messages are only useful if you want to figure something out. 
Jan 26, 2015 11:26:32 INFO Information is usually harmless, but helpful. 
Jan 26, 2015 11:26:40 WARNING Warnings should be heeded. 
Jan 26, 2015 11:26:54 WARNING Watch for warnings.
'''
infile = inname.split('\n')
warnings = (l.replace("WARNING", "") for l in infile if 'WARNING' in l)
for l in warnings:
    print(l)

# Consider a truly object-oriented solution of generator, without any shortcuts
# NOT FOR USE

# class WarningFilter:
#     def __init__(self, insequence):
#         self.insequence = insequence
#     def __iter__(self):
#         return self
#     def __next__(self):
#         l = self.insequence.readline()
#         while l and "WARNING" not in l:
#             l = self.insequence.readline()
#         if not l:
#             raise StopIteration
#         return l.replace("\tWARNING", "")

# with open(inname) as infile:
#     with open(outname, "w") as outfile:
#         filter = WarningFilter(infile)
#         for l in filter:
#             outfile.write(l)

# True generator code
'''
When Python sees  yield  in a function, it takes that
function and wraps it up in an object not unlike the one in previous example

Think of the  yield  statement as similar to the  return  statement; it exits the function and returns a
line. Unlike  return , however, when the function is called again (via  next() ), it will start
where it left off—on the line after the  yield  statement—instead of at the beginning of the
function. In this example, there is no line after the  yield  statement, so it jumps to the next
iteration of the  for  loop.
'''
print('*'*20)

def warnings_filter(insequence):
    for l in insequence:
        if "WARNING" in l:
            yield l.replace("WARNING", "")

filter = warnings_filter(infile)
for l in filter:
    print(l)

'''
We want to yield data from another iterable object, possibly a list comprehension or generator
expression we constructed inside the generator, or perhaps some external items that were
passed into the function. 
'''
# def warnings_filter(infilename):
#     with open(infilename) as infile:
#         yield from (
#             l.replace("\tWARNING", "") for l in infile if "WARNING" in l
#         )
