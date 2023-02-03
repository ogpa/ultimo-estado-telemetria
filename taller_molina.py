import pandas as pd
from convertir_coordinates import convertir_coordinates
import ast
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
POLY_TALLER_MOLINA = Polygon([(-12.071496, -76.955457), (-12.071008, -76.954843),
                              (-12.070704, -76.953837), (-12.072157, -76.953322), (-12.0726576, -76.954998)])


def taller_molina(main_df):

    main_df["taller_molina"] = main_df.apply(lambda x: POLY_TALLER_MOLINA.contains(
        Point(x["latitud"], x["longitud"])), axis=1)

    return main_df
