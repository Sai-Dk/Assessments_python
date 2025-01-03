import pandas as pd
import io

# Read the existing SKU sheet
sku_df = pd.read_excel('SKU.xlsx', sheet_name='SKU')

# Read the ITEM data from a text file
item_data = """
Name,Null?,Type
DMDUNIT,NOT NULL,VARCHAR2(50 CHAR)
DMDGROUP,NOT NULL,VARCHAR2(50 CHAR)
LOC,NOT NULL,VARCHAR2(50 CHAR)
HISTSTART,NOT NULL,DATE
EFF,NOT NULL,DATE
DISC,NOT NULL,DATE
FCSTHOR,NOT NULL,NUMBER
DMDCAL,NOT NULL,VARCHAR2(50 CHAR)
DMDPOSTDATE,NOT NULL,DATE
MODELDATE,NOT NULL,DATE
STATMSE,NOT NULL,FLOAT(126)
MAXHIST,NOT NULL,NUMBER
TOTFCSTLOCK,NOT NULL,NUMBER
LOCKDUR,NOT NULL,NUMBER
REFITDATE,NOT NULL,DATE
MASK,NOT NULL,VARCHAR2(18 CHAR)
MAPUSED,NOT NULL,VARCHAR2(50 CHAR)
NETFCSTMSE,NOT NULL,FLOAT(126)
NETFCSTMSESMCONST,NOT NULL,FLOAT(126)
NETFCSTERROR,NOT NULL,FLOAT(126)
NEGFCSTSW,NOT NULL,NUMBER
MODEL,NOT NULL,VARCHAR2(18 CHAR)
PUBLISHDATE,NOT NULL,DATE
NUMYEARS,NOT NULL,NUMBER
SEASONERRORLAG,NOT NULL,NUMBER
SEOUTLIEROPT,NOT NULL,NUMBER(38)
SEOUTLIERFACTOR,NOT NULL,FLOAT(126)
PICKBESTSW,NOT NULL,NUMBER(38)
PICKBESTDATE,NOT NULL,DATE
SYMMETRICMAPE,NOT NULL,FLOAT(126)
RUNCALCMODELSW,NOT NULL,NUMBER(38)
STATICCFDESCR,NOT NULL,VARCHAR2(50 CHAR)
STATICCFVALUE,NOT NULL,FLOAT(126)
COPYFROMDMDUNIT,NOT NULL,VARCHAR2(50 CHAR)
COPYFROMDMDGROUP,NOT NULL,VARCHAR2(50 CHAR)
COPYFROMLOC,NOT NULL,VARCHAR2(50 CHAR)
COPYFROMMODEL,NOT NULL,VARCHAR2(18 CHAR)
COPYDATE,NOT NULL,DATE
NEWDFUSW,NOT NULL,NUMBER(1)
MSEHISTDUR,NOT NULL,NUMBER(38)
OUTLIEROPT,NOT NULL,NUMBER(38)
STOREFITTEDHISTOPT,NOT NULL,NUMBER(38)
OBSOLETEFLAG,NOT NULL,NUMBER
DCRANK,NOT NULL,NUMBER
NPIINDDATE,NOT NULL,DATE
NPIMEANSMOOTH,NOT NULL,FLOAT(126)
NPITRENDSMOOTH,NOT NULL,FLOAT(126)
NPISCALINGFACTOR,NOT NULL,FLOAT(126)
NPISW,NOT NULL,NUMBER(1)
NPIFROMDMDPOSTDATE,NOT NULL,DATE
ADJDMDPOSTDATE,NOT NULL,DATE
NPIFROMMSE,NOT NULL,FLOAT(126)
HWMODELSW,NOT NULL,NUMBER(1)
INITE3ERROR,NOT NULL,FLOAT(126)
E3ERROR,NOT NULL,FLOAT(126)
SEASONPROFILE,NOT NULL,VARCHAR2(50 CHAR)
INCLUDE_IN_SLCCURVE,NOT NULL,NUMBER(38)
INITE3ERRORDATE,,DATE
E3ERRORDATE,,DATE
DFUATTRIBGROUP,NOT NULL,VARCHAR2(50 CHAR)
PEERPROFILE,NOT NULL,VARCHAR2(50 CHAR)
EXTREMEFCSTFACTOR,,NUMBER
TIMEALLOCPROFILENAME,NOT NULL,VARCHAR2(50 CHAR)
TIMEALLOCSW,NOT NULL,NUMBER
NPILAUNCHDATE,NOT NULL,DATE
U_DFU_LEVEL,NOT NULL,VARCHAR2(20 CHAR)
U_FCST_DISC_DATE,NOT NULL,DATE

"""

# Create a DataFrame for the ITEM data
item_df = pd.read_csv(io.StringIO(item_data), delimiter=',')

# Update the Excel file with the ITEM data
with pd.ExcelWriter('SKU.xlsx', engine='openpyxl', mode='a') as writer:
    item_df.to_excel(writer, sheet_name='8', index=False)

print("Excel file updated successfully last sheet")