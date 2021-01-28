#!/usr/bin/env python
from correctionlib.schemav2 import CorrectionSet
import jsonschema
import gzip
import json
import time

tic = time.time()
with gzip.open("data/examples.json.gz") as fin:
    y = CorrectionSet.parse_raw(fin.read())
toc = time.time()
print(f"Reading using pydantic model: {toc-tic:.3}s")

tic = time.time()
with open("data/schemav2.json") as sfin:
    schema = json.load(sfin)
    with gzip.open("data/examples.json.gz") as fin:
        data = json.load(fin)
        jsonschema.validate(data, schema)
toc = time.time()
print(f"Reading using jsonschema (py2-compatible): {toc-tic:.3}s")
