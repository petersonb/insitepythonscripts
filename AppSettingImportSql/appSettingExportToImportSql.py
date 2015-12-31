import csv

## Create App Settings if do not exist
##
##sql_line = """
##IF EXISTS (SELECT Id FROM ApplicationSetting WHERE Name='{0}')
##  UPDATE ApplicationSetting
##      SET Value='{1}', Description='{2}'
##  WHERE Name='{0}'
##ELSE
##  INSERT INTO ApplicationSetting (Name, Value, Description)
##  VALUES ('{0}','{1}','{2}')
##"""

## Do not create app settings
## Do not update description
sql_appsetting = """
IF EXISTS (SELECT Id FROM ApplicationSetting WHERE Name='{0}')
  UPDATE ApplicationSetting
      SET Value='{1}'
  WHERE Name='{0}'
"""

## WebSiteConfigurationId 0,NameUseMiniCart 1,ParentWebSiteName 2,Value 3,Description 4
sql_websitesetting = """
IF EXISTS (SELECT Id FROM WebSiteConfiguration WHERE Name='{0}')
  UPDATE WebSiteConfiguration
      SET Value='{1}'
  WHERE Name='{0}'
"""

outfile = open("import.sql",'w')
with open("applicationsettings.csv") as appcsvfile:
    infileReader = csv.reader(appcsvfile, delimiter=',', quotechar='"')
    for row in infileReader:
        out_sql = sql_appsetting.format(row[1],row[2],row[3])
        print(out_sql)
        outfile.write(out_sql)

with open("websitesettings.csv") as webcsvfile:
    infileReader = csv.reader(webcsvfile, delimiter=',', quotechar='"')
    for row in infileReader:
        out_sql = sql_websitesetting.format(row[1],row[3],row[4])
        print(out_sql)
        outfile.write(out_sql)
    
outfile.close()
appcsvfile.close()
webcsvfile.close()
