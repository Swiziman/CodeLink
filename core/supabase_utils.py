import random
from supabase import create_client, Client
from django.conf import settings

supabase_url = settings.SUPABASE_URL
supabase_key = settings.SUPABASE_KEY
supabase: Client = create_client(supabase_url, supabase_key)

image_size = {'width': 400, 'height': 400}  # Exemplo de tamanho de imagem
list_vinculos = []
dev_loc = []

class DispUser:
    def __init__(self, tag, area):
        self.tag = tag
        self.area = area

    @classmethod
    def from_map(cls, map_data):
        return cls(map_data['tag'], map_data['area'])

class Area:
    @staticmethod
    def get_nome_by_id(area_id):
        # Implementar a lógica para obter o nome da área pelo ID
        pass

def _gerar_coordenada(min, max):
    return min + random.random() * (max + 1 - min)

def _width_destination(destino):
    is_mobile = (image_size['height'] < 400)
    fator = image_size['width'] * (0.93 if is_mobile else 0.94)
    if destino == 1:  # RECEPÇÃO
        min = fator * 0.59
        max = fator
    elif destino == 2:  # PEDIATRIA
        min = fator * 0.35
        max = fator * 0.55
    elif destino in [3, 4, 5, 6]:  # QUARTOS
        min = fator * 0.02
        max = fator * 0.21
    elif destino == 7:  # SALA DE RAIO-X
        min = fator * 0.35
        max = fator * 0.63
    elif destino == 8:  # ORTOPEDIA
        min = fator * 0.76
        max = fator
    elif destino in [14, 15]:  # CORREDOR, BANHEIROS
        min = fator * 0.25
        max = fator * 0.73
    else:  # Default case
        min = fator * 0.25
        max = fator * 0.73
    return _gerar_coordenada(min, max)

def _height_destination(destino):
    is_mobile = (image_size['height'] < 400)
    add = 55.0 if is_mobile else 70.0
    fator = image_size['height'] * (1.07 if is_mobile else 1.01)
    if destino == 1:  # RECEPÇÃO
        min = fator * 0.65
        max = fator
    elif destino == 2:  # PEDIATRIA
        min = fator * 0.75
        max = fator
    elif destino == 3:  # QUARTO 1
        min = fator - (fator - add)
        max = fator * 0.3
    elif destino == 4:  # QUARTO 2
        min = fator * 0.35 if not is_mobile else fator * 0.4
        max = fator * 0.53
    elif destino == 5:  # QUARTO 3
        min = fator * 0.58 if not is_mobile else fator * 0.62
        max = fator * 0.77
    elif destino == 6:  # QUARTO 4
        min = fator * 0.83
        max = fator
    elif destino == 7:  # SALA DE RAIO-X
        min = fator * 0.35 if not is_mobile else fator * 0.4
        max = fator * 0.56
    elif destino == 8:  # ORTOPEDIA
        min = fator - (fator - add)
        max = fator * 0.36
    elif destino == 14:  # CORREDOR
        min = fator - (fator - add)
        max = fator * 0.31
    elif destino == 15:  # BANHEIROS
        min = fator * 0.43
        max = fator * 0.56
    else:  # Default case
        min = fator - (fator - add)
        max = fator * 0.31
    return _gerar_coordenada(min, max)

def _carrega_dados():
    vinculos_temp = []
    data_du = supabase.table('vw_dispositivos_usuarios2').select('*').execute()
    vinculos_temp.extend(data_du.data)
    for i in vinculos_temp:
        list_vinculos.append(DispUser.from_map(i))
        dev_loc.append({
            'cor': f"Color-{(len(list_vinculos) - 1) % 12}",  # Simulação de cor
            'tag': list_vinculos[-1].tag,
            'destino': Area.get_nome_by_id(list_vinculos[-1].area),
            'h': _height_destination(list_vinculos[-1].area),
            'w': _width_destination(list_vinculos[-1].area),
        })

class DispUser:
    def __init__(self, tag, area):
        self.tag = tag
        self.area = area

    @classmethod
    def from_map(cls, map_data):
        tag = map_data.get('tag')
        area = map_data.get('area')
        if tag is not None and area is not None:
            return cls(tag, area)
        else:
            return None

    # Outros métodos e definições de classe aqui...

    # core/supabase_utils.py

async def _carrega_dados():
    listVinculos = []
    devLoc = []

    dataDU = await supabase.from_('vw_dispositivos_usuarios2').select('*').execute()
    if dataDU.error:
        print(dataDU.error)
        return

    vinculosTemp = dataDU['data']

    for i in vinculosTemp:
        disp_user = DispUser.from_map(i)
        if disp_user:
            listVinculos.append(disp_user)
            devLoc.append({
                'cor': Colors.primaries[(len(listVinculos) - 1) % len(Colors.primaries)],
                'tag': disp_user.tag,
                'destino': Area.get_nome_by_id(disp_user.area),
                'h': _height_destination(disp_user.area),
                'w': _width_destination(disp_user.area),
            })
        else:
            print("Erro ao processar dados do usuário do dispositivo:", i)

    # Restante do seu código aqui
