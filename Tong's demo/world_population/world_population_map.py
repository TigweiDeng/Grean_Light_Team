import json

import pygal.style

import pygal

from pygal.maps.world import COUNTRIES


#通过国家名获取国家代码的函数
def get_country_code(country_name1):
    for code1, name in COUNTRIES.items():
        if name == country_name1:
            return code1
    return None


# 读取文件
filename = 'population_json.json'
with open(filename) as f:
    pop_data = json.load(f)


# 提取国家人口信息
cc_population = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2016':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_population[code] = population


# 根据人口数量分三组
cc_pops1, cc_pops2, cc_pops3 = {}, {}, {}
for cc, pop in cc_population.items():
    if pop < 10000000:
        cc_pops1[cc] = pop
    elif pop < 1000000000:
        cc_pops2[cc] = pop
    else:
        cc_pops3[cc] = pop


# 制作地图
wm = pygal.maps.world.World()
wm.title = 'World Population in 2016, by Country'
wm.add('0-10m', cc_pops1)
wm.add('10m-1bn', cc_pops2)
wm.add('>1bn', cc_pops3)
wm_style = pygal.style.RotateStyle('#3399AA', base_style=pygal.style.LightColorizedStyle)

wm.render_to_file('world_population.svg')
