
#Libraries for plotting and data processing:
import pandas as pd


#prompts user to enter name of input file
file = input("Enter file name: ")

#prompts user to enter name of star type
star = input("Enter the name of the star type: ")

#Open the CSV file and store in pop and prompts user to enter name of input file
name = pd.read_csv(file)

#Group the data by largest star type and radius.
large = name.groupby(['Star type'])

#Group the data by smallest star type and radius.
small = name.groupby(['Star type'])

#Print the radii of the largest star for the given star type.
print("The radius of the largest" , star , "is" , large['Radius(R/Ro)'].max())

#Print the radii of the smallest star for the given star type.
print("The radius of the smallest" , star , "is" , small['Radius(R/Ro)'].min())
