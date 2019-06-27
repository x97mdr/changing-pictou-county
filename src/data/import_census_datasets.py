import pandas as pd

COLUMN_RENAMES = {
    "Age (110)": "Age",
    "Total - Sex": "Total",
    "Age(110)": "Age",
    "Age (122)": "Age",
    "Age (123)": "Age",
    "Age (131)": "Age",
    "Age (in single years) and average age (127)": "Age",
    "  Female": "Female",
    "  Male": "Male",
}


def _get_census_1991_pictou_county():
    path = "https://www12.statcan.gc.ca/English/census91/data/tables/File.cfm?S=0&LANG=E&A=R&PID=71935&GID=3503&D1=0&D2=0&D3=0&D4=0&D5=0&D6=0&OFT=CSV"
    df = pd.read_csv(path, skiprows=2)
    df.drop(columns=[" "], inplace=True)
    df.rename(columns=COLUMN_RENAMES, inplace=True)
    df.drop(df.index[0], inplace=True)
    df = df[~df.Age.str.contains("years")]
    df.drop(df.tail(2).index, inplace=True)
    df.replace(to_replace="Under 1", value=0, inplace=True)
    df["Year"] = 1991
    df.reset_index(inplace=True, drop=True)
    return df


def _get_census_1996_pictou_county():
    path = "https://www12.statcan.gc.ca/English/census96/data/tables/File.cfm?S=0&LANG=E&A=R&PID=1030&GID=199728&D1=0&D2=0&D3=0&D4=0&D5=0&D6=0&OFT=CSV"
    df = pd.read_csv(path, skiprows=2)
    df.drop(columns=[" "], inplace=True)
    df.rename(columns=COLUMN_RENAMES, inplace=True)
    df.drop(df.index[0], inplace=True)
    df = df[~df.Age.str.contains("-")]
    df.drop(df.tail(1).index, inplace=True)
    df["Year"] = 1996
    df.reset_index(inplace=True, drop=True)
    return df


def _get_census_2001_pictou_county():
    path = "https://www12.statcan.gc.ca/English/census01/products/standard/themes/File.cfm?S=0&LANG=E&A=R&PID=55439&GID=426199&D1=0&D2=0&D3=0&D4=0&D5=0&D6=0&OFT=CSV"
    df = pd.read_csv(path, skiprows=2)
    df.drop(columns=[" "], inplace=True)
    df.rename(columns=COLUMN_RENAMES, inplace=True)
    df.drop(df.index[0], inplace=True)
    df = df[~df.Age.str.contains("-")]
    df.drop(df.tail(2).index, inplace=True)
    df["Year"] = 2001
    df.reset_index(inplace=True, drop=True)
    return df


def _get_census_2006_pictou_county():
    path = "https://www12.statcan.gc.ca/census-recensement/2006/dp-pd/tbt/File.cfm?S=0&LANG=E&A=R&PID=88989&GID=771825&D1=0&D2=0&D3=0&D4=0&D5=0&D6=0&OFT=CSV"
    df = pd.read_csv(path, skiprows=2)
    df.drop(columns=[" "], inplace=True)
    df.rename(columns=COLUMN_RENAMES, inplace=True)
    df.drop(df.index[0], inplace=True)
    df = df[~df.Age.str.contains("years")]
    df.drop(df.tail(7).index, inplace=True)
    df["Year"] = 2006
    df.reset_index(inplace=True, drop=True)
    return df


def _get_census_2011_pictou_county():
    path = "https://www12.statcan.gc.ca/census-recensement/2011/dp-pd/tbt-tt/File.cfm?S=0&LANG=E&A=R&PID=102010&GID=906638&D1=0&D2=0&D3=0&D4=0&D5=0&D6=0&OFT=CSV"
    df = pd.read_csv(path, skiprows=2)
    df.drop(columns=[" "], inplace=True)
    df.rename(columns=COLUMN_RENAMES, inplace=True)
    df.drop(df.index[0], inplace=True)
    df = df[~df.Age.str.contains("years")]
    df.drop(df.tail(4).index, inplace=True)
    df["Year"] = 2011
    df.reset_index(inplace=True, drop=True)
    return df


def _get_census_2016_pictou_county():
    path = "https://www12.statcan.gc.ca/census-recensement/2016/dp-pd/dt-td/File.cfm?S=0&LANG=E&A=R&PID=109526&GID=1160159&D1=0&D2=0&D3=0&D4=0&D5=0&D6=0&OFT=CSV"
    df = pd.read_csv(path, skiprows=3)
    df.drop(columns=[" "], inplace=True)
    df.rename(columns=COLUMN_RENAMES, inplace=True)
    df.drop(df.index[0], inplace=True)
    df = df[~df.Age.str.contains("years")]
    df.drop(df.tail(3).index, inplace=True)
    df["Year"] = 2016
    df.reset_index(inplace=True, drop=True)
    return df


def get_census_1991_to_2016_pictou_county():
    df1991 = _get_census_1991_pictou_county()
    df1996 = _get_census_1996_pictou_county()
    df2001 = _get_census_2001_pictou_county()
    df2006 = _get_census_2006_pictou_county()
    df2011 = _get_census_2011_pictou_county()
    df2016 = _get_census_2016_pictou_county()
    df = pd.concat([df1991, df1996, df2001, df2006, df2011, df2016], sort=True)
    return df
