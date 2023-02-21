import pandas as pd

#aPPLICATION DU COURS DE STATISTIQUES
#DONNEES QUANTITATIVES DISCRETES

# Code couleur (pour l'ésthétique)
RESET = "\033[0m"  # Réinitialisation de la couleur
NOIR = "\033[30m"  # Texte noir
ROUGE = "\033[31m"  # Texte rouge
VERT = "\033[32m"  # Texte vert
JAUNE = "\033[33m"  # Texte jaune
BLEU = "\033[34m"  # Texte bleu
MAGENTA = "\033[35m"  # Texte magenta
CYAN = "\033[36m"  # Texte cyan
BLANC = "\033[37m"  # Texte blanc



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

#tests pour voir que tout est ok
#print(clean_df_death_brussels)
#print(clean_df_tests_brussels)
#print(clean_df_hospital_brussels)
#print(clean_df_cases_brussels_commune)
#print(clean_df_ages_brussels)
#print("-----------------------------------------------------")
#print(df_cases_commune)
#print(df_death)
#print(df_hospital)
#print(df_cases_ages)
#print(df_tests)

'''Maintenant que l'on a nettoyé notre jeu de donnée nous pouvons passer à l'analyse'''

'''clean_df_death_brussels
clean_df_tests_brussels
clean_df_hospital_brussels
clean_df_cases_brussels_commune
clean_df_ages_brussels'''

#moyennes

mean_death = clean_df_death_brussels["DEATHS"].mean()
mean_all_tests = clean_df_tests_brussels["TESTS_ALL"].mean()
mean_positif_cases = clean_df_tests_brussels["TESTS_ALL_POS"].mean()

mean_new_in_hospital = clean_df_hospital_brussels["NEW_IN"].mean()
mean_new_out_hospital = clean_df_hospital_brussels["NEW_OUT"].mean()
mean_resp = clean_df_hospital_brussels["TOTAL_IN_RESP"].mean()
mean_intensive_care = clean_df_hospital_brussels["TOTAL_IN_ICU"].mean()
mean_ecmo = clean_df_hospital_brussels["TOTAL_IN_ECMO"].mean()
mean_reporting = clean_df_hospital_brussels["NR_REPORTING"].mean()
print(" ")
print(" ")
print("-------------------------------------------------------------")
print("Chiffres COVID à Bruxelles du 15/03/2020 jusqu'au 31/01/2023:")
print("")
print("")


print(CYAN+"VOICI LES MOYENNES: "+RESET)


print("Morts: "+MAGENTA+f"{mean_death}"+RESET)
print("Tests efectués: "+MAGENTA+f"{mean_all_tests}"+RESET)
print("Tests positifs: "+MAGENTA+f"{mean_positif_cases}"+RESET)
print("Personnes entrantes à l'hospital: "+MAGENTA+f"{mean_new_in_hospital}"+RESET)
print("Personne sortantes de l'hopital: "+MAGENTA+f"{mean_new_out_hospital}"+RESET)
print("Personnes sous respirateur: "+MAGENTA+f"{mean_resp}"+RESET)
print("Personne sous oxygénation extracorporel: "+MAGENTA+f"{mean_ecmo}"+RESET)
print("Personnes aux soins intensifs: "+MAGENTA+f"{mean_intensive_care}"+RESET)
print("Nombre de cas rapportés: "+MAGENTA+f"{mean_reporting}"+RESET)
print(" ")
print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------")

print(CYAN+"VOICI LES EFFECTIFS TOTAUX: "+RESET)
sum_death = clean_df_death_brussels["DEATHS"].sum()
sum_all_tests = clean_df_tests_brussels["TESTS_ALL"].sum()
sum_positif_cases = clean_df_tests_brussels["TESTS_ALL_POS"].sum()

sum_new_in_hospital = clean_df_hospital_brussels["NEW_IN"].sum()
sum_new_out_hospital = clean_df_hospital_brussels["NEW_OUT"].sum()
sum_resp = clean_df_hospital_brussels["TOTAL_IN_RESP"].sum()
sum_intensive_care = clean_df_hospital_brussels["TOTAL_IN_ICU"].sum()
sum_ecmo = clean_df_hospital_brussels["TOTAL_IN_ECMO"].sum()
sum_reporting = clean_df_hospital_brussels["NR_REPORTING"].sum()

print("Morts: "+MAGENTA+f"{sum_death}"+RESET)
print("Tests efectués: "+MAGENTA+f"{sum_all_tests}"+RESET)
print("Tests positifs: "+MAGENTA+f"{sum_positif_cases}"+RESET)
print("Personnes entrantes à l'hospital: "+MAGENTA+f"{sum_new_in_hospital}"+RESET)
print("Personne sortantes de l'hopital: "+MAGENTA+f"{sum_new_out_hospital}"+RESET)
print("Personnes sous respirateur: "+MAGENTA+f"{sum_resp}"+RESET)
print("Personne sous oxygénation extracorporel: "+MAGENTA+f"{sum_ecmo}"+RESET)
print("Personnes aux soins intensifs: "+MAGENTA+f"{sum_intensive_care}"+RESET)
print("Nombre de cas rapportés: "+MAGENTA+f"{sum_reporting}"+RESET)
print(" ")
print(" ")


percent_deaths = round(sum_death/sum_positif_cases,3)
print("Pourcentage de morts: "+ROUGE+f"{percent_deaths} %"+RESET)

percent_covid = round(sum_positif_cases/sum_all_tests,3)
print("Pourcentage d'infection: "+ROUGE+f"{percent_covid} %"+RESET)

percent_deaths2 = round(sum_death/sum_all_tests,3)
print(percent_deaths2)
print("-----------------------------------------------------------------")
print(CYAN+"NOMBRE DE CAS PAR COMMUNE: "+RESET)

anderlecht = 48048
Ouderghem = 14606
Berchem_saint_agathe = 10283
Bruxelles = 73848
Etterbeek =  21896
Evere = 17544
Foret = 24866
Ganshoren = 10013
Elsene = 38298
Jette = 21183
Koekelberg =  8510
Molenbeek_Saint_Jean = 39327
Saint_Gilles = 21623
Saint_Josse_Ten_Node = 10474
Schaerbeek = 54820
Uccle = 35348
Watermael_Boitsfort = 10941
Woluwe_Saint_Lambert = 24424
Saint_Peters_Leuw = 17542

total_cases = 503594

print("Anderlecht: "+MAGENTA+f"{anderlecht}"+RESET)
print("Ouderghem: "+MAGENTA+f"{Ouderghem}"+RESET)
print("Berchem-saint-agathe: "+MAGENTA+f"{Berchem_saint_agathe}"+RESET)
print("Bruxelles: "+MAGENTA+f"{Bruxelles}"+RESET)
print("Etterbeek: "+MAGENTA+f"{Etterbeek}"+RESET)
print("Evere: "+MAGENTA+f"{Evere}"+RESET)
print("Foret: "+MAGENTA+f"{Foret}"+RESET)
print("Ganshoren: "+MAGENTA+f"{Ganshoren}"+RESET)
print("Elsene: "+MAGENTA+f"{Elsene}"+RESET)
print("Jette: "+MAGENTA+f"{Jette}"+RESET)
print("Koekelberg: "+MAGENTA+f"{Koekelberg}"+RESET)
print("Molenbeek-saint-jean: "+MAGENTA+f"{Molenbeek_Saint_Jean}"+RESET)
print("Saint-gilles: "+MAGENTA+f"{Saint_Gilles}"+RESET)
print("saint-josse-ten-node: "+MAGENTA+f"{Saint_Josse_Ten_Node}"+RESET)
print("schaerbeek: "+MAGENTA+f"{Schaerbeek}"+RESET)
print("uccle: "+MAGENTA+f"{Uccle}"+RESET)
print("watermael-boitsfort: "+MAGENTA+f"{Watermael_Boitsfort}"+RESET)
print("woluwe-saint-lambert: "+MAGENTA+f"{Woluwe_Saint_Lambert}"+RESET)
print("saint-peters-leuw: "+MAGENTA+f"{Saint_Peters_Leuw}"+RESET)
print(" ")
print(" ")























