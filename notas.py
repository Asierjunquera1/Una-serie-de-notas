import pandas as pd

df=pd.DataFrame({"Notas": [3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16] })
print(df)

def media():
    media=df["Notas"].mean()
    print("la media es:", media)

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

media()
mediana()
moda()
