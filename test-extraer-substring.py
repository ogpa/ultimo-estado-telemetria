LONGITUD_IDS = 8
str_mongr = '{\"0\":[25657118],\"23151123\":[22511245,22511315,22511352,22511371,22511395,22511549,22512400,22512686,22517564,22518416,22518584,22519288,22528628,22528908,22529061,22529499,22530185,22530462,22533870,22533999,22534544,22534711,22534874,22535021,22537666,22537984,22538007,22538163,22538412,22538534,22538541,22543728,22544657,22544666,22545166,22545392,22545432,22545444,22545550,22545598,22545777,22545869,22546051,22551671,22552581,22552598,22552604,22552609,22552612,22552621,22552627,22553704,22559267,22559403,22559617,22559636,22559741,22559827,22560261,22560690,22560899,22560920,22561222,22561656,22561671,22561680,22561691,22561705,22561715,22566567,22566916,22567272,22567883,22568192,22568228,22568263,22568318,22569022,22569029,22569036,22569042,22569050,22569055,22569060,22569065,22569071,22569078,22569086,22569093,22569097,22569104,22569109,22574357,22574375,22590292,22590471,22590668,22591312,22591910,22592061,22597908,22597970,22598459,22598708,22598714,22613344,22613822,22629202,22629288,22637038,22637054,22637084,22651943,22779722,22786556,22786828,22787000,22787116,22787410,22793225,22802698,22811077,22811089,22811094,22811504,22812553,22818708,22821039,22821235,22821842,22826896,22826925,22827027,22827734,22827762,22828105,22828307,22829196,22829325,22829344,22833035,22833343,22835981,22836008,22840018,22840397,22840717,22851627,22857130,22857846,22858029,22858610,22858782,22874978,22874993,22883957,22892351,22892383,22892444,22892850,22893688,22914063,22914110,22990603,22991857,23032364,23032538,23040851,23133579,23774991,23775008,23775181,23775256,23775383,23775433,23775475,23775522,23775559,23775578,23775599,23775657,23775682,23775701,23775716,23775732,23775761,24353758,25649729,25649772,25649790,25649796,26025413,26026953,26026958,26026968,26026970,26026974,26026978,26026983,26035977,26037572,26037577,26037586,26037594,26037600,26037603,26037608,26037620,26037623,26037627,26037641,26122723,26122766,26122802,26122808,26122892,26122960,26123014,26123183,26123306,26123528,26134421,26134424,26134428,26134461,26135082,26135095,26135106,26135110,26135155,26144747,26144749,26264424,26264426,26264427,26268894,26268908,26268910,26364776,26364792,26364804,26393648],\"25676298\":[22682935,24834421,25087107]}'
lista_ids = []

pos_2_inicio = str_mongr.find("2")
while pos_2_inicio != -1:
    id = str_mongr[pos_2_inicio:pos_2_inicio + LONGITUD_IDS]
    nueva_posicion_inicial = pos_2_inicio + LONGITUD_IDS + 1
    lista_ids.append(id)
    pos_2_inicio = str_mongr.find("2", nueva_posicion_inicial)
print(len(lista_ids))
print(lista_ids)