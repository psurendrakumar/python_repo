keys = ['surendra','naveen','rajesh']
values = ['java','python','css']
data = dict(zip(keys,values))
print(data)

data['mounika'] = 'js'
print(data)

del data['rajesh']
print(data)


prog = {
    'js'     : 'atom',
    'cs'     : 'vs',
    'python' : ['pycharm','anaconda'], #using list as a value in the dictionaries
    'java'   : {'jse' : 'netbeans','jee' : 'eclipse' } #using dictionary as a value in the dictionaries
}
print(prog)
print(prog['js'])
print(prog['python'])
print(prog['python'][1])
print(prog['java'])
print(prog['java']['jee'])