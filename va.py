import pandas as pd
df = pd.read_csv('calidadvino.csv', sep=';')
df.head()

mediana_alcohol = df.alcohol.median()
for i, alcohol in enumerate(df.alcohol):
    if alcohol >= mediana_alcohol:
        df.loc[i, 'alcohol'] = 'alto'
    else:
        df.loc[i, 'alcohol'] = 'bajo'
df.groupby('alcohol').calidad.mean()

mediana_ph = df.pH.median()
for i, pH in enumerate(df.pH):
    if pH >= mediana_ph:
        df.loc[i, 'pH'] = 'alto'
    else:
        df.loc[i, 'pH'] = 'bajo'
df.groupby('pH').calidad.mean()

mediana_azucar = df.azucar_residual.median()
for i, azucar in enumerate(df.azucar_residual):
    if azucar >= mediana_azucar:
        df.loc[i, 'azucar residual'] = 'alto'
    else:
        df.loc[i, 'azucar residual'] = 'bajo'
df.groupby('azucar residual').calidad.mean()

mediana_acido = df.acido_citrico.median()
for i, acido_citrico in enumerate(df.acido_citrico):
    if acido_citrico >= mediana_acido:
        df.loc[i, 'acido citrico'] = 'alto'
    else:
        df.loc[i, 'acido citrico'] = 'bajo'
df.groupby('acido citrico').calidad.mean()

print(df.groupby('alcohol').calidad.mean())
print(df.groupby('pH').calidad.mean())
print(df.groupby('azucar residual').calidad.mean())
print(df.groupby('acido citrico').calidad.mean())