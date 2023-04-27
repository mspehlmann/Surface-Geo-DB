#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:02:07 2023

@author: michaelspehlmann
"""

import pandas as pd
import re
#%% import takes awhile
hmc_df = pd.read_excel(r"/Volumes/Extreme SSD/geochem db/AGDB_xlsx/BestValue_HMC.xlsx")
rock_df = pd.read_excel(r"/Volumes/Extreme SSD/geochem db/AGDB_xlsx/BestValue_Rock.xlsx")
sed_df = pd.read_excel(r"/Volumes/Extreme SSD/geochem db/AGDB_xlsx/BestValue_Sed.xlsx")
soil_df = pd.read_excel(r"/Volumes/Extreme SSD/geochem db/AGDB_xlsx/BestValue_Soil.xlsx")
#%%% set headers
new_header = hmc_df.iloc[3]
hmc_df = hmc_df.iloc[4:]
hmc_df.columns = new_header
hmc_df["type"] = "hmc"

new_header = rock_df.iloc[3]
rock_df = rock_df.iloc[4:]
rock_df.columns = new_header
rock_df["type"] = "rock"

new_header = sed_df.iloc[3]
sed_df = sed_df.iloc[4:]
sed_df.columns = new_header
sed_df["type"] = "sed"

new_header = soil_df.iloc[3]
soil_df = soil_df.iloc[4:]
soil_df.columns = new_header
soil_df["type"] = "soil"
#%%% create a new field book like table
field_df = hmc_df[["LAB_ID",'FIELD_ID','JOB_ID','SUBMITTER','DATE_SUBMITTED','DATE_COLLECT',
        'LATITUDE','LONGITUDE','LOCATE_DESC','DEPTH','SAMPLE_SOURCE','SAMPLE_COMMENT',
        'MESH_PORE_SIZE', 'type']]
merger = rock_df[["LAB_ID", 'FIELD_ID','JOB_ID','SUBMITTER','DATE_SUBMITTED','DATE_COLLECT',
        'LATITUDE','LONGITUDE','LOCATE_DESC','DEPTH','SAMPLE_SOURCE','SAMPLE_COMMENT',
        'SOURCE_ROCK','type']]
field_df = pd.concat([field_df, merger], axis=0)

merger = sed_df[["LAB_ID",'FIELD_ID','JOB_ID','SUBMITTER','DATE_SUBMITTED','DATE_COLLECT',
        'LATITUDE','LONGITUDE','LOCATE_DESC','DEPTH','SAMPLE_SOURCE','SAMPLE_COMMENT',
        'MESH_PORE_SIZE', "type"]]
field_df = pd.concat([field_df, merger], axis=0)

merger = soil_df[["LAB_ID",'FIELD_ID','JOB_ID','SUBMITTER','DATE_SUBMITTED','DATE_COLLECT',
        'LATITUDE','LONGITUDE','LOCATE_DESC','DEPTH','SAMPLE_SOURCE','SAMPLE_COMMENT',
        'MESH_PORE_SIZE', "type"]]
field_df = pd.concat([field_df, merger], axis=0)
field_df.drop(columns=("DATE_COLLECT"), inplace=True)
#%% This cell is for trying to clean up the mesh pore sizes into ints
def field_mesh_clean(value):
    if value[0] == "+":
        converted = ""
        for character in range(1,len(value)):
            try:
                converted +=  value[character]
            except ValueError:
                break
        return int(converted)
    elif value[0] == "-":
        converted = ""
        for character in range(1, len(value)):
            try:
                converted += value[character]
            except ValueError:
                break
        return int(converted)
    else:
        return None
        
#%% 
litho_string = """^(Li.*(?<!Sum)$|Be.*(?<!Sum)$|Na.*(?<!Sum)$|Mg.*(?<!Sum)$|
    Ca.*(?<!Sum)$|Na.*(?<!Sum)$|K_.*(?<!Sum)$|Rb.*(?<!Sum)$|Sr.*(?<!Sum)$|Cs.*(?<!Sum)$|
    Ba.*(?<!Sum)$|Sc.*(?<!Sum)$|Ti.*(?<!Sum)$|V_.*(?<!Sum)$|Cr.*(?<!Sum)$|Y_.*(?<!Sum)$|
    Zr.*(?<!Sum)$|Nb.*(?<!Sum)$|Lu.*(?<!Sum)$|Hf.*(?<!Sum)$|Ta.*(?<!Sum)$|B_.*(?<!Sum)$|
    O_.*(?<!Sum)$|F_.*(?<!Sum)$|Al.*(?<!Sum)$|Si.*(?<!Sum)$|P_.*(?<!Sum)$|Cl.*(?<!Sum)$|
    Br.*(?<!Sum)$|La.*(?<!Sum)$|Ce.*(?<!Sum)$|Pr.*(?<!Sum)$|Nd.*(?<!Sum)$|Sm.*(?<!Sum)$|
    Eu.*(?<!Sum)$|Gd.*(?<!Sum)$|Tb.*(?<!Sum)$|Dy.*(?<!Sum)$|Ho.*(?<!Sum)$|Er.*(?<!Sum)$|
    Tm.*(?<!Sum)$|Yb.*(?<!Sum)$|Th.*(?<!Sum)$|U_.*(?<!Sum)$|^LAB_ID|^type)"""


calco_string = """^LAB_ID|^S_.*(?<!Sum)$|^Cu.*(?<!Sum)$|^Zn.*(?<!Sum)$|^Ga.*(?<!Sum)$|
    ^Ge.*(?<!Sum)$|^As.*(?<!Sum)$|^Se.*(?<!Sum)$|^Ag.*(?<!Sum)$|^Cd.*(?<!Sum)$|
    ^In.*(?<!Sum)$|^Sn.*(?<!Sum)$|^Sb.*(?<!Sum)$|^Te.*(?<!Sum)$|^Hg.*(?<!Sum)$|
    ^Tl.*(?<!Sum)$|^Pb.*(?<!Sum)$|^Bi.*(?<!Sum)$|^type"""""
    
sidero_string = """^LAB_ID|Mn.*(?<!Sum)$|^Fe.*(?<!Sum)$|^Co.*(?<!Sum)$|^Ni.*(?<!Sum)$|
    ^Mo.*(?<!Sum)$|^Ru.*(?<!Sum)$|^Rh.*(?<!Sum)$|^Pd.*(?<!Sum)$|^W_.*(?<!Sum)$|
    ^Re.*(?<!Sum)$|^Os.*(?<!Sum)$|^Ir.*(?<!Sum)$|^Pt.*(?<!Sum)$|^Au.*(?<!Sum)$|^type"""

lithoR_df = rock_df.filter(regex=litho_string, axis=1)
lithoS_df = sed_df.filter(regex=litho_string, axis=1)
lithoD_df = soil_df.filter(regex=litho_string, axis=1)
lithoH_df = hmc_df.filter(regex=litho_string, axis=1)


litho_df = pd.concat([lithoR_df, lithoS_df, lithoD_df, lithoH_df], ignore_index=True)
litho_df = litho_df[litho_df.columns.drop(list(litho_df.filter(regex='\w+_meq.*')))]
litho_df.rename(columns={"LAB_ID":"lab_id"}, inplace=True)

calcoR_df = rock_df.filter(regex=calco_string, axis=1)
calcoS_df = sed_df.filter(regex=calco_string, axis=1)
calcoD_df = soil_df.filter(regex=calco_string, axis=1)
calcoH_df = hmc_df.filter(regex=calco_string, axis=1)



calco_df = pd.concat([calcoR_df, calcoS_df, calcoD_df, calcoH_df], ignore_index=True)
calco_df = calco_df[calco_df.columns.drop(list(calco_df.filter(regex=("^Ash_.*|Gas_pct.*"))))]
calco_df.rename(columns={"LAB_ID":"lab_id"}, inplace=True)

sideroR_df = rock_df.filter(regex=sidero_string, axis=1)
sideroS_df = sed_df.filter(regex=sidero_string, axis=1)
sideroD_df = soil_df.filter(regex=sidero_string, axis=1)
sideroH_df = hmc_df.filter(regex=sidero_string, axis=1)


sidero_df = pd.concat([sideroR_df, sideroS_df, sideroD_df, sideroH_df], ignore_index=True)
sidero_df.rename(columns={"LAB_ID":"lab_id"}, inplace=True)
#%%clean up dtypes and make the header more sql conventional
field_df.columns = [header.lower() for header in field_df.columns]
litho_df.rename(columns=({"LAB_ID":"lab_id"}), inplace=True)
sidero_df.rename(columns=({"LAB_ID":"lab_id"}), inplace=True)
calco_df.rename(columns=({"LAB_ID":"lab_id"}), inplace=True)

field_df['latitude'] = pd. to_numeric(field_df['latitude'])
field_df['longitude'] = pd.to_numeric(field_df['longtitude'])

def to_floats(chem_table):
    p = re.compile("[A-Za-z0-9]+_ppm$|[A-Za-z0-9]+_pct$")
    arr1 = list(chem_table.columns)
    arr2 = [string for string in arr1 if p.match(string)]
    for element in arr2:
        chem_table[element] = pd.to_numeric(chem_table[element])
    return 

to_floats(sidero_df)
to_floats(calco_df)
to_floats(litho_df)
#%% establish connection to postgres
from sqlalchemy import create_engine

username = input("Enter your username for a postgre database: ")
password = input("Enter your password: ")
ipaddress = input("Enter the ip address to the database or enter localhost for locally hosted database: ")
port = int(input("Enter which port you postgres is using.  Commonly this is 5432: 5432"))
dbname = "Geology"

postgres_str = f'postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'
cnx = create_engine(postgres_str)

#%% a bit slow but damn was that easier than defining cols in sql
#field_df.to_sql("field", con=cnx, index=False)
#sidero_df.to_sql("siderophiles", con=cnx, index=False)
#calco_df.to_sql("chalcophiles", con=cnx, index=False)
#litho_df.to_sql("lithophiles", con=cnx, index=False)




