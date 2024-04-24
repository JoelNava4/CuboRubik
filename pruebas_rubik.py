import pandas as pd

# Crear el DataFrame dado
data = {'Up': ['Y']*9,
        'Front': ['W']*9,
        'Left': ['O']*9,
        'Right': ['G']*9,
        'Down': ['B']*9,
        'Back': ['R']*9}
df = pd.DataFrame(data)

# Intercambiar los valores según las instrucciones dadas
colors_Left, colors_Right = df.loc[0:2, 'Front'].values.copy(), df.loc[0:2, 'Back'].values.copy()
colors_Front, colors_Back = df.loc[0:2, 'Right'].values.copy(), df.loc[0:2, 'Left'].values.copy()
df.loc[0:2, 'Front'],df.loc[0:2, 'Back'] = colors_Front,colors_Back
df.loc[0:2, 'Right'],df.loc[0:2, 'Left'] = colors_Right,colors_Left

print("DataFrame modificado:")
print(df)