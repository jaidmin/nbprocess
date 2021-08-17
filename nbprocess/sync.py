# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_sync.ipynb.

# %% auto 0
__all__ = ['nb2dict', 'write_nb', 'absolute_import', 'update_lib']

# %% ../nbs/03_sync.ipynb 4
from .read import *
from .maker import *
from .export import *

from .imports import *
from fastcore.script import *

import ast,tempfile,json

# %% ../nbs/03_sync.ipynb 5
def nb2dict(d, k=None):
    "Convert parsed notebook to `dict`"
    if k=='source': return d.splitlines(keepends=True)
    if isinstance(d, (L,list)): return list(L(d).map(nb2dict))
    if not isinstance(d, dict): return d
    return dict(**{k:nb2dict(v,k) for k,v in d.items() if k[-1] != '_'})

# %% ../nbs/03_sync.ipynb 8
def write_nb(nb, path):
    "Write `nb` to `path`"
    nb = nb2dict(nb)
    with io.open(path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(nb, sort_keys=True, indent=1, ensure_ascii=False))
        f.write("\n")

# %% ../nbs/03_sync.ipynb 11
def absolute_import(name, fname, level):
    "Unwarps a relative import in `name` according to `fname`"
    if not level: return name
    mods = fname.split(os.path.sep)
    if not name: return '.'.join(mods)
    return '.'.join(mods[:len(mods)-level+1]) + f".{name}"

# %% ../nbs/03_sync.ipynb 13
_re_import = re.compile("from\s+\S+\s+import\s+\S")
_re_export = re.compile("\s*#\s*exporti?(\s+\S+)?\s*$")

# %% ../nbs/03_sync.ipynb 15
def _to_absolute(code, lib_name):
    if not _re_import.search(code): return code
    res = update_import(code, ast.parse(code).body, lib_name, absolute_import)
    return ''.join(res) if res else code

def _update_lib(nbname, nb_locs, lib_name=None):
    if lib_name is None: lib_name = get_config().lib_name
    nb = read_nb(nbname)

    for name,idx,code in nb_locs:
        assert name==nbname
        cell = nb.cells[int(idx)-1]
        lines = cell.source.splitlines(True)
        source = lines[0] if lines and _re_export.match(lines[0]) else ''
        cell.source = source + _to_absolute(code, lib_name)
    write_nb(nb, nbname)

def _get_call(s):
    top,*rest = s.splitlines()
    return *top.split(),'\n'.join(rest)

# %% ../nbs/03_sync.ipynb 16
@call_parse
def update_lib(fname:str): # A python file name to convert
    "Propagates any change in the modules matching `fname` to the notebooks that created them"
    if os.environ.get('IN_TEST',0): return
    code_cells = Path(fname).read_text().split("\n# %% ")[1:]
    locs = L(_get_call(s) for s in code_cells if not s.startswith('auto '))
    for nbname,nb_locs in groupby(locs, 0).items(): _update_lib(nbname, nb_locs)
