import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#this functionn reads the datframe for us
def call_df(df):
    return pd.read_csv(df)
    
# here is the dataframe that we used
df = call_df('vgsales.csv')

def row_col_count(df):
    print('Number of rows for vgsales is', len(df))
    print('Number of columns for vgsales is', len(df.columns))
    
    
def get_row_col_count(df):
    print('Number of rows for vgsales is', len(df))
    print('Number of columns for vgsales is', len(df.columns))

def get_stats():
    num_var = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
    # create stat dictionay and store all the info
    stat = {}
    for i in num_var:
        stat[i] = {}
        stat[i]['avg_sales'] = np.mean(df[i])
        stat[i]['min_sales'] = np.min(df[i])
        stat[i]['max_sales'] = np.max(df[i])
    return stat ## return stat since its a function 

def try_catch(stat):
    try: 
        print('median sale is ', stat['median_sales'])
    except:
        print('median sale is not calculated')

def remane_columns(df):
    rename_list = {'NA_Sales':'north_america_sales',
                'EU_Sales':'europe_sales',
                'JP_Sales':'japan_sales',
                'Other_Sales':'other_countries_sales',
                'Global_Sales':'global_sales'}
    
    df.rename(rename_list, axis='columns', inplace=True)    # Rename some of the columns

    for i in df.columns:         ####  lower case all the column names
        df.rename({i: str.lower(i)}, axis='columns', inplace=True)
    df.columns
    print(df.columns)

def duplicate_check(df):
    
    print('number of obeservations is ', df.count(),' before remove duplication')
    df.drop_duplicates
    print('number of obeservations is ', df.count(),' after remove duplication')

def drop_na(df):    
    df.dropna()   

def missing_value_check(df):
    df.isna().sum()

    df[df['year'].isna()]

    df[df['name'] == 'Triple Play 99']

    df[df['publisher'].isna()].count()
    

def split_join(df):
    print("\nBefore using the split_join function:\n\n",df['name'].head())
    df['name']= df['name'].str.split(' ').str.join('_')
    df.head()
    print ("\nAfter using spli_joinfunction:\n\n",df['name'].head())

#################### SLICING THE DATA ################################
# count the top 5 video games for each publisher 
top_5_publisher = df.groupby('Publisher')[['Name']].nunique().sort_values(by = 'Name', ascending = False).head()

#count the top 20 video games that have the highest global sales.
top_20_global_sales = df[['Name', 'Platform', 'Year','Publisher','Global_Sales']].head(20).sort_values(by = 'Global_Sales', ascending = False)

#Genres distribution
genre = df['Genre'].value_counts().reset_index()

#Top 10 game publishers
top10_publisher = df['Publisher'].value_counts().reset_index().head(10)

def user_interaction_1(choice1):
    if choice1 != 1 and choice1 != 2:
        print(' Wrong choice')
    elif choice1 == 1:
        print('You chose 1 option 1\n', top_5_publisher)
    else:
        print('You chose opttion 2\n', top_20_global_sales)

def user_interaction_2(choice):
    if choice==1:
        print("You chose option 1\n ")
        year = df.groupby('Year')[['Publisher']].count().reset_index()['Year']
        count = df.groupby('Year')[['Publisher']].count().reset_index()['Publisher']
        fig, ax = plt.subplots()
        ax.plot(year, count, linewidth=2.0)
        plt.show()
    elif choice==2:
            print("You chose option 2\n ")
            x = top10_publisher['index']
            y = top10_publisher['Publisher']
            fig = plt.figure(figsize = (10, 5))
            plt.barh(x, y)
            plt.show()
    elif choice==3:
        df_genre = df.groupby('Genre',axis=0).count()

        colors_list = ['gold','yellowgreen','lightcoral', 'lightskyblue', 'green', 'pink','purple','orange','gray','red'
              ,'blue','silver']
        explode_list = [0, 0, 0, 0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0, 0] # ratio for each continent with which to offset each wedge

        df_genre['Name'].plot(kind='pie',
                            figsize=(15,6),
                            autopct='%1.1f%%',
                            startangle = 90,
                            shadow = True,
                            labels=None,
                            pctdistance=1.1, # the ratio between the center of each pie slice and the percentage location
                            colors = colors_list,
                            explode=explode_list) # will explode lowest 6 gernres)                            
        plt.title('Percent Sale for each Genre')
        plt.axis('equal')
        plt.legend(labels=df_genre.index, loc='upper left')
        plt.show()



