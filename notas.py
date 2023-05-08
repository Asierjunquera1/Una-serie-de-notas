import pandas as pd

df=pd.DataFrame({"Notas": [3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16] })
print(df)

def media():
    media=df["Notas"].mean()
    print("la media es:", media)
    return media

def mediana():
    mediana=df["Notas"].median()
    print("la mediana es:", mediana)

def moda():
    moda=df["Notas"].mode()
    if len(moda)==1:
        print("la moda es:", moda)
    else:
        print("la moda es:", moda.iloc[0], end=" ")
        for i in range(1, len(moda)):
            print("y", moda.iloc[i])

def desviacion_tipica():
    desviacion_tipica = df["Notas"].std()
    print("La desviación típica es:", desviacion_tipica)

def varianza():
    varianza = df["Notas"].var()
    print("La varianza es:", varianza)

def cuartil1():
    cuartil1 = df["Notas"].quantile(0.25)
    print("El valor del primer cuartil (25%) es: ", cuartil1)

def cuartil2():
    cuartil2 = df["Notas"].quantile(0.5)
    print("El valor del segundo cuartil (50%) es: ", cuartil2)

def cuartil3():
    cuartil3 = df["Notas"].quantile(0.75)
    print("El valor del tercer cuartil (75%) es: ", cuartil3)


def valor_max():
    valor_max = df["Notas"].max()
    print("El valor máximo es: ", valor_max)

def valor_min():
    valor_min = df["Notas"].min()
    print("El valor mínimo es:", valor_min)
