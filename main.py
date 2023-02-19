import pandas as pd

df_cases_ages = pd.read_csv("COVID19BE_CASES_AGESEX.csv")
df_cases_commune = pd.read_csv("COVID19BE_CASES_MUNI_CUM.csv")
df_hospital = pd.read_csv("COVID19BE_HOSP.csv")
df_death = pd.read_csv("COVID19BE_MORT.csv")
df_tests = pd.read_csv("COVID19BE_tests.csv")

'''NOUS VOULONS ETUDIER LES DONNEES POUR BRUXELLES DONC ON VA FILTRER LES DONNER AFIN D'AVOIR LES DONNEES QUE POUR BRUXELLES '''
#PHASE DE FILTRAGE

# Nombre de tests effectués ainsi que le nombre de tests positifs
df_tests_brussels = df_tests[df_tests["PROVINCE"] == "Brussels"]
print(df_tests_brussels)

#Nombre de morts par age et par sexe
df_death_brussels = df_death[df_death["REGION"] == "Brussels"]
print(df_death_brussels)

#statistique des hopitaux dans bruxelles (in,out,etc)
df_hospital_brussels = df_hospital[df_hospital["REGION"] == "Brussels"]
print(df_hospital_brussels)

# Les cas covid par commune dans la région de bruxelles
df_cases_brussels_commune = df_cases_commune[df_cases_commune["REGION"] == "Brussels"]
print(df_cases_brussels_commune)

#Cas covid par groupe d'ages et sexe à Bruxelles
df_ages_brussels = df_cases_ages[df_cases_ages["REGION"] == "Brussels"]
print(df_ages_brussels)

#au final nous obtenons 5 beaux tableaux

#A PRESENT ON VA SUPPRIMER LES DONNEES MANQUANTES (NaN)

clean_df_ages_brussels = df_ages_brussels.dropna()
clean_df_cases_brussels_commune = df_cases_brussels_commune.dropna()
clean_df_hospital_brussels = df_hospital_brussels.dropna()
clean_df_tests_brussels = df_tests_brussels.dropna()
clean_df_death_brussels = df_death_brussels.dropna()

print(clean_df_death_brussels)
print(clean_df_tests_brussels)
print(clean_df_hospital_brussels)
print(clean_df_cases_brussels_commune)
print(clean_df_ages_brussels)
print("-----------------------------------------------------")
print(df_cases_commune)
print(df_death)
print(df_hospital)
print(df_cases_ages)
print(df_tests)

'''Maintenant que l'on a nettoyé notre jeu de donnée nous pouvons passer à l'analyse'''

#TODO


