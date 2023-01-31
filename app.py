import pandas as pd
import final as ft
import matplotlib.pyplot as plt

if __name__=="__main__":
################# CONTRIBUTION ###########################
#### Hussein Mawaw: Data Cleaning, data insights, graph generation, debugging
#### Madison Dotson: Data Cleaning, data insights, graph generation, ppt
#### Paola Dumbi: Data Cleaning, function generation, data insights, graph generation debugging
################# QUESTION 1    ##########################
    
    df = ft.call_df('vgsales.csv')

################## QUESTION 2   #############################
## COUNT ROWS AND COLUMNS
    ft.get_row_col_count(df)

###SHOW STATS
    max_jp_sales = ft.get_stats()["JP_Sales"]["max_sales"]
    print("\nMax sales in Japan:", max_jp_sales,'\n')

################## QUESTION 3   #############################

    print('\n\n___________Let us walk you through our data cleaning process with the following functions:_____________\n\n')
    
    print("\nRenaming our columns:\n",ft.remane_columns(df),"\n")
    print("\nRemoving duplicates:\n",ft.duplicate_check(df),"\n")
    print("\nDropping null values:\n",ft.drop_na(df),"\n")
    print("\nChecking missing values:\n",ft.missing_value_check(df),"\n\n")

################## QUESTION 4   #############################
###TRY AND CATCH
    ft.try_catch(max_jp_sales)

###SPLIT JOIN
    print("\nUsing the split_join funciton to modify the column Name:",ft.split_join(df),"\n")

###WHILE LOOP     
    print('\n')
    print('__________ HELLO, WELCOME TO OUR VIDEO GAME DB !! __________ \n')
    print('What would you want to know today? \n ')  

#Prompt the user to select the outcome that he wants to see 
    choice1 = int(input('Please make a choice. 1 = top 5 video publisher and 2 = top 20 global sales\n\n')) 
    while (choice1==1) or (choice1==2):
        ft.user_interaction_1(choice1)  
        break 
    else:
        if input("Wrong Choice. Do you want to try again? (y/n): ") == "y":
            choice1 = int(input("\nPlease make a choice. 1 = top 5 video publisher and 2 = top 20 global sales\n\n"))
            ft.user_interaction_1(choice1)   
        else: 
            print("you chose NO")
            quit()  
        
# Prompt the user to select the outcome that he wants to see
    choice = int(input("\n\n__________What do you want to see next?__________\n\n Enter the number of the desired option:\n\n1.The dominant genre\t2.The top 10 game publisher\t3.Percent Sale for each Genre"))

    while (choice==1) or (choice==2) or (choice==3):
        ft.user_interaction_2(choice) 
        quit()     
    else:
        if input("Wrong Choice. Do you want to try again? (y/n): ") == "y":
            choice = int(input("\n\n__________What do you want to see next?__________\n Enter the number of the desired option:\n1.The dominant genre\t2.The top 10 game publisher\t3.Percent Sale for each Genre"))
            ft.user_interaction_2(choice)   
            quit()  
        else: 
            print("you chose NO")
            quit()  


