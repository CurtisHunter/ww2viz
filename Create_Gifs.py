import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D
import s3fs
import os



# Loading data from AWS S3

AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_DEFAULT_REGION = os.environ["AWS_DEFAULT_REGION"]
bucket_name = os.environ["bucket_name"]
url = os.environ["url"]

s3 = s3fs.S3FileSystem(anon=False, key=AWS_ACCESS_KEY_ID, secret=AWS_SECRET_ACCESS_KEY)

with s3.open(f"{bucket_name}/operations.csv", "rb") as f:
    oper = pd.read_csv(f)

with s3.open(f"{bucket_name}/events.csv", "rb") as f:
    even = pd.read_csv(f)


#even = pd.read_csv("data/events.csv")
#oper = pd.read_csv("data/operations.csv")


# Converting str dates to datetime

oper['Mission Date'] = pd.to_datetime(oper['Mission Date']).dt.to_period('M').dt.to_timestamp()
even['Date'] = even['Date'].str.split(' - ').str[0]  # handling when there is a range of dates
even['Date'] = pd.to_datetime(even['Date']).dt.to_period('M').dt.to_timestamp()

# Drop unused features
drop_list = ['Mission ID', 'Unit ID', 'Target ID', 'Altitude (Hundreds of Feet)', 'Airborne Aircraft',
             'Attacking Aircraft', 'Bombing Aircraft', 'Aircraft Returned',
             'Aircraft Failed', 'Aircraft Damaged', 'Aircraft Lost',
             'High Explosives', 'High Explosives Type', 'Mission Type',
             'High Explosives Weight (Pounds)', 'High Explosives Weight (Tons)',
             'Incendiary Devices', 'Incendiary Devices Type',
             'Incendiary Devices Weight (Pounds)',
             'Incendiary Devices Weight (Tons)', 'Fragmentation Devices',
             'Fragmentation Devices Type', 'Fragmentation Devices Weight (Pounds)',
             'Fragmentation Devices Weight (Tons)', 'Total Weight (Pounds)',
             'Total Weight (Tons)', 'Time Over Target', 'Bomb Damage Assessment', 'Source ID']
oper.drop(drop_list, axis=1, inplace=True)

# Drop incorrect latitude and longitude values
oper = oper[(oper.iloc[:, 8] != 4248) & (oper.iloc[:, 9] != 1355)]

# Set color based on country
oper['color'] = "yellow"
oper.loc[oper.Country == "USA", 'color'] = "red"
oper.loc[oper.Country == "GREAT BRITAIN", 'color'] = "blue"


# Set the overall map bounds

lllat = -60  # lower-left corner latitude
urlat = 70   # upper-right corner latitude
lllon = -16  # lower-left corner longitude
urlon = 180  # upper-right corner longitude
textoffset = 3
dotsize = 4.5
textsep = 6

plotmain = False # Choose to plot/animate the main plot on the home page
if plotmain:
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111)
    m = Basemap(projection='cyl', llcrnrlat=lllat, urcrnrlat=urlat,
                llcrnrlon=lllon, urcrnrlon=urlon, ax=ax)
    m.drawcoastlines()
    m.drawcountries()


def update_plot(frame): # Generic function to plot each frame of the animation
    ax.clear()
    m = Basemap(projection='cyl', llcrnrlat=lllat, urcrnrlat=urlat,
                llcrnrlon=lllon, urcrnrlon=urlon, ax=ax)
    m.drawcoastlines()
    m.drawcountries() # Map setup

    filtered_events = even[even['Date'] == frame] # Getting just the specific date
    filtered_data = oper[oper['Mission Date'] == frame]

    lat = filtered_data['Target Latitude'].values
    lon = filtered_data['Target Longitude'].values
    colors = filtered_data['color'].values

    for lt, ln, col in zip(lat, lon, colors): # Plotting each point individually (as they have different colours, so can't do them all together)
        x, y = m(ln, lt)
        m.plot(x, y, 'o', markersize=dotsize, color=col)


    for i, event in enumerate(filtered_events['Event']): # Plotting event text
        ax.text(lllon + 2, lllat + i * textsep + textoffset, event, fontsize=12, ha='left', color='red', backgroundcolor='white')

    framedate = pd.to_datetime(frame)

    ax.set_title(f'Date: {framedate.month_name()} {framedate.year}') # Setting title

    # Legend
    red_dot = Line2D([0], [0], marker='o', color='w', label='USA', markerfacecolor='red', markersize=10)
    blue_dot = Line2D([0], [0], marker='o', color='w', label='Great Britain', markerfacecolor='blue', markersize=10)
    yellow_dot = Line2D([0], [0], marker='o', color='w', label='Other Allied Forces', markerfacecolor='yellow', markersize=10)
    ax.legend(handles=[red_dot, blue_dot, yellow_dot], loc='lower right')


# Create animation
#ani = FuncAnimation(fig, update_plot, frames=sorted(oper['Mission Date'].unique()), repeat=True, interval = 400)

# Save the animation to a GIF
#ani.save(filename="mainviz.gif", writer="pillow")

#plt.show()



# --------- EUROPE --------------------------------------------


# Creating these large code segments with replicated code because FuncAnimation doesn't allow arguments in the update_plot funtion, so using global variables instead


# Map Bounds
lllat = -1  # lower-left corner latitude
urlat = 67.5   # upper-right corner latitude
lllon = -16 # lower-left corner longitude
urlon = 52  # upper-right corner longitude
textoffset = 2
textsep = 3.5
dotsize = 3.5

plotEurope = True

if plotEurope:
    # Set up the figure, axis, and map projection
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111)
    m = Basemap(projection='cyl', llcrnrlat=lllat, urcrnrlat=urlat,
                llcrnrlon=lllon, urcrnrlon=urlon, ax=ax)
    m.drawcoastlines()
    m.drawcountries()
    # plt.show # (uncomment this if you want to see just the map)

    # Create animation
    #ani = FuncAnimation(fig, update_plot, frames=sorted(oper['Mission Date'].unique()), repeat=True, interval = 400)

    #ani.save(filename="Europeviz.gif", writer="pillow")

    # Display the animation
    # plt.show()



# --------- Asia --------------------------------------------



# Map bounds
lllat = -60  # lower-left corner latitude
urlat = 70   # upper-right corner latitude
lllon = 60  # lower-left corner longitude
urlon = 180  # upper-right corner longitude
textoffset = 3
dotsize = 4.5
textsep = 6


plotAsia = True

if plotAsia:
    # Set up the figure, axis, and map projection
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111)
    m = Basemap(projection='cyl', llcrnrlat=lllat, urcrnrlat=urlat,
                llcrnrlon=lllon, urcrnrlon=urlon, ax=ax)
    m.drawcoastlines()
    m.drawcountries()

    #plt.show() # (uncomment this if you want to see just the map)


    # Create animation
    ani = FuncAnimation(fig, update_plot, frames=sorted(oper['Mission Date'].unique()), repeat=True, interval = 400)

    ani.save(filename="Asiaviz.gif", writer="pillow")

    # Display the animation
    #plt.show()

