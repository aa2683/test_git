#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import h3pandas
import geopandas
import numpy as np
import math




df_data = pd.DataFrame({'lng': [-73.993896, -73.976425, -73.968704, -73.976601, -73.994957, -73.944957, -73.8944957],
                        'lat':[40.700111, 40.739811, 40.754246, 40.751896, 40.745079, 40.775079, 40.805079]})
