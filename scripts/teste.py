import random

async def _carrega_dados():
    vinculos_temp = []
    data_DU = await supabase.from_('vw_dispositivos_usuarios2').select()
    vinculos_temp.extend(data_DU)
    for i in vinculos_temp:
        list_vinculos.append(DispUser.from_map(i))
        dev_loc.append({
            'cor': Colors.primaries[(len(list_vinculos) - 1) % len(Colors.primaries)],
            'tag': list_vinculos[-1].tag,
            'destino': Area.get_nome_by_id(list_vinculos[-1].area),
            'h': _height_destination(list_vinculos[-1].area),
            'w': _width_destination(list_vinculos[-1].area),
        })
    # print(dev_loc)

def _gerar_coordenada(min_, max_):
    return min_ + random.random() * (max_ - min_)

def _width_destination(destino):
    is_mobile = (_image_size.height < 400)
    fator = _image_size.width * (0.93 if is_mobile else 0.94)
    if destino == 1:  # RECEPÇÃO
        min_ = fator * 0.59
        max_ = fator
    elif destino == 2:  # PEDIATRIA
        min_ = fator * 0.35
        max_ = fator * 0.55
    elif destino in [3, 4, 5, 6]:  # QUARTO 1, 2, 3, 4
        min_ = fator * 0.02
        max_ = fator * 0.21
    elif destino == 7:  # SALA DE RAIO-X
        min_ = fator * 0.35
        max_ = fator * 0.63
    elif destino == 8:  # ORTOPEDIA
        min_ = fator * 0.76
        max_ = fator
    elif destino == 14:  # CORREDOR
        min_ = fator * 0.25
        max_ = fator * 0.73
    elif destino == 15:  # BANHEIROS
        min_ = fator * 0.76
        max_ = fator
    else:
        min_ = fator * 0.25
        max_ = fator * 0.73
    return _gerar_coordenada(min_, max_)

def _height_destination(destino):
    is_mobile = (_image_size.height < 400)
    add = 55.0 if is_mobile else 70.0
    fator = _image_size.height * (1.07 if is_mobile else 1.01)
    if destino == 1:  # RECEPÇÃO
        min_ = fator * 0.65
        max_ = fator
    elif destino == 2:  # PEDIATRIA
        min_ = fator * 0.75
        max_ = fator
    elif destino == 3:  # QUARTO 1
        min_ = fator - (fator - add)
        max_ = fator * 0.3
    elif destino == 4:  # QUARTO 2
        min_ = fator * 0.4 if is_mobile else fator * 0.35
        max_ = fator * 0.53
    elif destino == 5:  # QUARTO 3
        min_ = fator * 0.62 if is_mobile else fator * 0.58
        max_ = fator * 0.77
    elif destino == 6:  # QUARTO 4
        min_ = fator * 0.83
        max_ = fator
    elif destino == 7:  # SALA DE RAIO-X
        min_ = fator * 0.4 if is_mobile else fator * 0.35
        max_ = fator * 0.56
    elif destino == 8:  # ORTOPEDIA
        min_ = fator - (fator - add)
        max_ = fator * 0.36
    elif destino == 14:  # CORREDOR
        min_ = fator - (fator - add)
        max_ = fator * 0.31
    elif destino == 15:  # BANHEIROS
        min_ = fator * 0.43
        max_ =fator * 0.56
    else:
        min_ = fator - (fator - add)
        max_ = fator * 0.31
    return _gerar_coordenada(min_, max_)