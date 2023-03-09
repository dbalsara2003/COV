# from functools import partial
# from shapely.geometry import Polygon
# from shapely.ops import transform
# import pyproj

# coords = [
#             [
#               -123.11549081344143,
#               49.28337374357312
#             ],
#             [
#               -123.11531675519022,
#               49.283248239032844
#             ],
#             [
#               -123.11500415201122,
#               49.28344911102019
#             ],
#             [
#               -123.11517619822942,
#               49.28356751852752
#             ]
#           ]
# polygon = Polygon(coords)

# print(polygon.area)

# proj = partial(pyproj.transform, pyproj.Proj(init='epsg:4326'), 
#                pyproj.Proj(init='epsg:3857'))

# print(transform(proj, polygon).area)





#-------------------------------------------------------------------------------------------------------------#

from functools import partial

import pyproj
from shapely.geometry import Polygon
import shapely.ops as ops

coords = [
            [
              -123.15911769845727,
              49.267915708764605
            ],
            [
              -123.15911081611294,
              49.26812293902756
            ],
            [
              -123.15921913157096,
              49.26812473868367
            ],
            [
              -123.15922574727385,
              49.267917462244725
            ],
            [
              -123.15911769845727,
              49.267915708764605
            ]
          ]
polygon = Polygon(coords)

print(polygon.area)
geom_area = ops.transform(
    partial(
        pyproj.transform,
        pyproj.Proj(init='EPSG:4326'),
        pyproj.Proj(
            proj='aea',
            lat_1=polygon.bounds[1],
            lat_2=polygon.bounds[3])),
    polygon)

#Close to absolute polygon area value is achieved by reducing the area by 0.099%.

print(f"Area of polygon: {geom_area.area/1.00099} square meters")
print(f"Area of polygon: {geom_area.area/1.00099*10.7639104} square feet")