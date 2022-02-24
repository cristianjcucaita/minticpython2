
# Calculo recorrido pistas de F1.

# Descripciones de siglas:
# re: Recorrido en metros
# vm: Velocidad media
# sg: Tiempo en segundos
# rkm: Velocidad Media en metro cuadrado

re, vm, sg = map(float,input().split())
rkm = (re / sg) * 3.6

if re >= 0 and vm >= 0 and sg >= 0:
    if  rkm <= vm:
        rkm = round(rkm,1)
        print(rkm, 'VELOCIDAD NORMAL')
    elif rkm > vm and rkm < ((vm * 20 / 100) + vm):
        rkm = round(rkm,1)
        print(rkm, 'NUEVO RECORD')
    else:
        rkm = round(rkm,1)
        print(rkm, 'ENTREVISTA')
else:
    print('ERROR')