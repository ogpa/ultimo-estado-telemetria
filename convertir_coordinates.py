import shapely.wkt
import shapely.ops


def convertir_coordinates(coordinates, tipo):
    # print(coordinates)
    tipo_poly = tipo.upper()
    poly_string = str(coordinates)
    poly_string = poly_string[1:]
    poly_string = poly_string[:-1]
    poly_string = poly_string.replace(", -", " -")
    poly_string = poly_string.replace("[", "(")
    poly_string = poly_string.replace("]", ")")
    poly_string = poly_string.replace("((((", "¡¡¡¡")
    poly_string = poly_string.replace("))))", "!!!!")
    poly_string = poly_string.replace("(((", "&&&")
    poly_string = poly_string.replace(")))", "$$$")
    poly_string = poly_string.replace("((", "##")
    poly_string = poly_string.replace("))", "??")
    poly_string = poly_string.replace("(", "")
    poly_string = poly_string.replace(")", "")
    poly_string = poly_string.replace("##", "((")
    poly_string = poly_string.replace("??", "))")
    poly_string = poly_string.replace("&&&", "(((")
    poly_string = poly_string.replace("$$$", ")))")
    poly_string = poly_string.replace("¡¡¡¡", "((((")
    poly_string = poly_string.replace("!!!!", "))))")
    poly_string_completo = tipo_poly + " " + poly_string
    poly = shapely.wkt.loads(poly_string_completo)
    # print(poly)
    return poly
# print(poly_string)

# convertir_coordinates(coordinates)
