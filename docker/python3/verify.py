import warnings
import dateparser
import tldextract
# set warnings to throw an error
warnings.simplefilter("error")
d = dateparser.parse('1 day')
extract = tldextract.TLDExtract(cache_dir=False,suffix_list_urls=None)
t = extract('*test-test.com')
print("all is good managed to parse: {}".format(d))

# cve-2021-3177 See: https://bugs.python.org/issue42938
# verify we are patched
from ctypes import *
print(c_double.from_param(1e300))
print("all is good cve-2021-3177 is patched")

import pydantic
class Sample(pydantic.BaseModel):
    name: str

sample = Sample(name='name')
print('pydantic is installed and running')
