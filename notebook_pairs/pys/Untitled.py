# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
from random_choice.records import ProbabilityRecord
from collections import Counter

# %%
sample = [ProbabilityRecord(-1, 0.33), ProbabilityRecord(0, 0.33), ProbabilityRecord(1, 0.33)]

# %%
c = Counter((s.data for s in sample))

# %%
c.update((s.data for s in sample))

# %%
c

# %%
3*0.33 - 1 

# %%
from itertools import cycle
from random import choices

# %%
c = cycle(choices([r.data for r in sample], weights=[r.probability for r in sample], k=10))

# %%
next(c)

# %%
