import re
import datetime
import os
import sys


WORD_PAT = re.compile(r"[^\S]?([^\s\n]+)")
LINE_PAT = re.compile(r"[^\\\n]?\n")
FUNCTION_PAT = re.compile(r"\n?def\s+?([\d\w_]+?)\s*?\(.*?\)\s*?:", re.DOTALL)
LAMBDA_PAT = re.compile(r"lambda.+?:.+?\n?", re.DOTALL)
CLASS_PAT = re.compile(r"\n?[\t ]*?class\s+([\d\w_]+?)(?:\([\s,\w\d_]\))*\s*?:", re.DOTALL)

IMPORT_PAT1 = re.compile(r"\n\s*import\s+([^\n]+)")
IMPORT_PAT2 = re.compile(r"\n\s*from (.+?)\s+import\s+([^\n]+)", re.DOTALL)

VARIABLE_PAT1 = re.compile(r"\n\s*([\w\d_]+?)\s*=.+?\n?", re.DOTALL)
VARIABLE_PAT2 = re.compile(r"\n\s*((?:[\w\d_]+?\s*,\s*[\w\d_]+?)+?)\s*=.+?\n?", re.DOTALL)

ALL_MODULES = ['__future__', '__main__', '_thread', 'abc', 'aifc', 'argparse', 'array', 'ast', 'asynchat', 'asyncio', 'asyncore', 'atexit', 'audioop', 'base64', 'bdb', 'binascii', 'binhex', 'bisect', 'builtins', 'bz2', 'calendar', 'cgi', 'cgitb', 'chunk', 'cmath', 'cmd', 'code', 'codecs', 'codeop', 'collections', 'colorsys', 'compileall', 'configparser', 'contextlib', 'contextvars', 'copy', 'copyreg', 'cProfile', 'csv', 'ctypes', 'dataclasses', 'datetime', 'dbm', 'decimal', 'difflib', 'dis', 'distutils', 'doctest', 'email', 'ensurepip', 'enum', 'errno', 'faulthandler', 'filecmp', 'fileinput', 'fnmatch', 'formatter', 'fractions', 'ftplib', 'functools', 'gc', 'getopt', 'getpass', 'gettext', 'glob', 'graphlib', 'gzip', 'hashlib', 'heapq', 'hmac', 'html', 'http', 'imaplib', 'imghdr', 'imp', 'importlib', 'inspect', 'io', 'ipaddress', 'itertools', 'json', 'keyword', 'lib2to3', 'linecache', 'locale', 'logging', 'lzma', 'mailbox', 'mailcap', 'marshal', 'math', 'mimetypes', 'mmap', 'modulefinder', 'multiprocessing', 'netrc', 'nntplib', 'numbers', 'operator', 'optparse', 'os', 'parser', 'pathlib', 'pdb', 'pickle', 'pickletools', 'pkgutil', 'platform', 'plistlib', 'poplib', 'pprint', 'profile', 'pstats', 'py_compile', 'pyclbr', 'pydoc', 'queue', 'quopri', 'random', 're', 'reprlib', 'rlcompleter', 'runpy', 'sched', 'secrets', 'select', 'selectors', 'shelve', 'shlex', 'shutil', 'signal', 'site', 'smtpd', 'smtplib', 'sndhdr', 'socket', 'socketserver', 'sqlite3', 'ssl', 'stat', 'statistics', 'string', 'stringprep', 'struct', 'subprocess', 'sunau', 'symbol', 'symtable', 'sys', 'sysconfig', 'tabnanny', 'tarfile', 'telnetlib', 'tempfile', 'test', 'textwrap', 'threading', 'time', 'timeit', 'tkinter', 'token', 'tokenize', 'trace', 'traceback', 'tracemalloc', 'turtle', 'turtledemo', 'types', 'typing', 'unicodedata', 'unittest', 'urllib', 'uu', 'uuid', 'venv', 'warnings', 'wave', 'weakref', 'webbrowser', 'wsgiref', 'xdrlib', 'xml', 'zipapp', 'zipfile', 'zipimport', 'zlib', 'zoneinfo']

def traverse_dir(path: str, depth=-1):
    prev_wd = os.getcwd()
    try:
        os.chdir(path)
        items = os.listdir()
    except:
        items = []
    
    for f in items:
        if os.path.isfile(f):
            yield os.path.abspath(f)
        elif depth < 0 or depth != 0:
            yield from traverse_dir(f, depth - 1)
    os.chdir(prev_wd)

def analyze_file(filepath):
    with open(filepath) as f:
        text = f.read()
    n_chars = len(text)
    words = WORD_PAT.findall(text)
    n_words = len(words)
    lines = LINE_PAT.findall(text)
    n_lines = len(lines) + 1
    text = "\n" + text + "\n"
    
    variables = VARIABLE_PAT1.findall(text)
    multi_vars = VARIABLE_PAT2.findall(text)
    for gp in multi_vars:
        vars = list(map(str.strip, gp.split(",")))
        variables.extend(vars)
    variables = set(variables)
    n_variables = len(variables)
    
    functions = FUNCTION_PAT.findall(text)
    n_functions = len(functions)
    
    classes = CLASS_PAT.findall(text)
    n_classes = len(classes)

    to_consider = []
    modules = []
    for module in IMPORT_PAT1.findall(text):
        items = list(map(str.strip, module.split(",")))
        for item in items:
            if "." in item:
                parts = list(map(str.strip, module.split(".")))
                if parts[0] in modules:
                    continue
                to_consider.append(parts)
            elif item not in modules and item in ALL_MODULES:
                modules.append(item)
    for item in to_consider:
        if item[0] in modules or item[0] not in ALL_MODULES:
            continue
        modules.append(".".join(item))
    for from_, item in IMPORT_PAT2.findall(text):
        items = list(map(str.strip, item.split(",")))
        if "." in from_:
            parts = list(map(str.strip, from_.split(".")))
            from_ = parts[0]
            for i in range(len(items)):
                items[i] = ".".join(parts[1:]) + "." + items[i]
        if from_ in modules or from_ not in ALL_MODULES:
            continue
        else:
            for item_ in items:
                modules.append(from_ + "." + item_)

    return (n_chars, n_words, n_lines, n_variables, n_functions, n_classes, sorted(modules))

project = "".join(sys.argv[1:])
if not project:
    project = input("Enter path of project (folder or file): ").strip()
if not os.path.exists(project):
    print("No such file or directory")
    sys.exit()
if os.path.isfile(project):
    stat = analyze_file(project)
    print("\nProject :", os.path.basename(project))
    print("Last Modified On: " + datetime.datetime.fromtimestamp(os.stat(project).st_mtime).strftime("%A, %d %B %Y, %I:%M %p"))
    print("Contains:")
    print("\t", stat[0], " Characters.", sep='')
    print("\t", stat[1], " Words.", sep='')
    print("\t", stat[2], " Lines.", sep='')
    print("\tVariables of ", stat[3], " different names.", sep='')
    print("\t", stat[4], " user defined Functions (including methods and lambda functions).", sep='')
    print("\t", stat[5], " user defined Classes.", sep='')
    print("\tUsed Modules (from Standard Library):", ", ".join(stat[6]))
    sys.exit()

stat_strs = []
modules = []
totals = [0, 0, 0, 0, 0, 0]
last_modified = 0
for file in traverse_dir(project):
    if not file.endswith(".py") and not file.endswith(".pyw"):
        continue
    stat = analyze_file(file)
    file_stat = os.stat(file)
    last_modified = max(file_stat.st_mtime, last_modified)
    stat_str = f"File Name: {os.path.basename(file)}.\nLast Modified On: {datetime.datetime.fromtimestamp(file_stat.st_mtime).strftime('%A, %d %B %Y, %I:%M %p')}\nContains:\n"
    stat_str += f"\t{stat[0]} Characters.\n"
    stat_str += f"\t{stat[1]} Words.\n"
    stat_str += f"\t{stat[2]} Lines.\n"
    stat_str += f"\tVariables of {stat[3]} different names.\n"
    stat_str += f"\t{stat[4]} user defined Functions (including methods and lambda functions).\n"
    stat_str += f"\t{stat[5]} user defined Classes."
    stat_strs.append(stat_str)
    for i in range(len(stat) - 1):
        totals[i] += stat[i]
    modules.extend(stat[6])

modules = list(set(modules))
for module in modules.copy():
    if "." in module:
        parts = module.split(".")
        for i in range(len(parts)):
            if ".".join(parts[:i + 1]) in modules:
                modules.remove(module)
                break
modules.sort()

print("\nProject:", os.path.basename(project))
print("Last Modified On: " + datetime.datetime.fromtimestamp(last_modified).strftime("%A, %d %B %Y, %I:%M %p"))
print("Contains:")
print("\t", totals[0], " Characters.", sep='')
print("\t", totals[1], " Words.", sep='')
print("\t", totals[2], " Lines.", sep='')
print("\tVariables of ", totals[3], " different names.", sep='')
print("\t", totals[4], " user defined Functions (including methods and lambda functions).", sep='')
print("\t", totals[5], " user defined Classes.", sep='')
print("\tUsed Modules (from Standard Library):", ", ".join(modules))
print("\n\nIndividual File stats:\n", "\n\n".join(stat_strs), sep='')
