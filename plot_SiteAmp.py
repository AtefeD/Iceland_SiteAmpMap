# -*- coding: utf-8 -*-
"""
Plot the geology-based seismic siter amplification classes for Iceland
Hard Rock (HR), Rock (R), Lava Rock (L), and Sedimentary Soil (S). 

Reference: A. Darzi, B. Halldorsson, F. Cotton, and S. Rahpeyma (2024),
 “Nationwide frequency-dependent seismic site amplification models for Iceland”, Soil Dynamics and Earthquake Engineering, 183, 108798. https://doi.org/10.1016/j.soildyn.2024.108798 

Atefe Darzi, PhD, Atefe@hi.is 
 
"""

import matplotlib.pyplot as plt
import numpy as np
import rasterio
from rasterio.enums import Resampling
from matplotlib.colors import ListedColormap, BoundaryNorm


 
tif="GeoSiteAmp_class.tif"


with rasterio.open(tif) as src:
    
    print("coor system:", src.crs)
    print("nodata value:", src.nodata)
    print("dtype:", src.dtypes[0])
    print("bounds:", src.bounds)
    print("shape:", src.height, src.width)
    
    # downsampling
    max_dim=2000
    scale=max(src.width//max_dim, src.height//max_dim, 1)
    out_h=src.height//scale
    out_w=src.width//scale
    a=src.read(1,out_shape=(out_h,out_w),resampling=Resampling.nearest)
print("nodata from metadata:", src.nodata)
print("number of nodata pixels:", np.ma.count_masked(a))
print("valid min/max:", a.min(), a.max())
a=np.ma.masked_equal(a,0)
a=np.ma.masked_equal(a,-9999)
cmap=ListedColormap(["darkgreen","dodgerblue","purple","gray"])
norm=BoundaryNorm([1,2,3,4,5],cmap.N)
plt.figure(figsize=(8,7), dpi=100)
plt.imshow(a,cmap=cmap,norm=norm,interpolation="nearest")
plt.title(f"GeoSiteAmp classes, downsampled x{scale}")
plt.show()
