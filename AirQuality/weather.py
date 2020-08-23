import tkinter as tk
from requests import get
from json import loads

# Getting all data from API


def get_data(city_var='piastow'):
    global status
    global city_name
    global category
    global time
    global total_rows
    # Here insert your own token, created on: https://aqicn.org/data-platform/token/#/
    token = 'here goes your token'
    # requests.get()
    api_request = get(
        'https://api.waqi.info/feed/'
        + city_var
        + f'/?token={token}')
    # Loading JSON jason.loads
    api = loads(api_request.content)

# Variables for api
    status = api['data']['aqi']
    city_name = api['data']['city']['name']
    category = api['data']["iaqi"]
    time = api['data']['time']['s']

    total_rows = len(category.keys())


def quality_colors(value):
    if value <= 50:
        return ('Good', '#009966')
    elif value <= 100:
        return ('Moderate', '#ffde33')
    elif value <= 150:
        return ('Unhealthy for sensitive groups', '#ff9933')
    elif value <= 200:
        return ('Unhealthy', '#cc0033')
    elif value <= 300:
        return ('Very unhealthy', '#660099')
    elif value > 300:
        return ('Hazardous', '#7e0023')
    else:
        return ('WRONG DATA', 'black')


def print_lables():
    global all_lbl
    global title_lbl
    global time_lbl
    global city_menu
    global refresh_btn
    global city_var
    # Title label
    title_lbl = tk.Label(root, text=f'{city_name.split()[1]} air quality: {status}',
                         font=('Helvetica', 20), background=quality_colors(status)[1])
    title_lbl.grid(row=0, column=0)
    # Time mesurment parameters
    time_lbl = tk.Label(root, text=f'Time messurement: {time}')
    time_lbl.grid(row=1, column=0)
    # Parameters labels
    lbl_text = [f"{name}: {category[value]['v']}" for name,
                value in zip(category_name, category_value) if value in category]
    all_lbl = [tk.Label(root, text=element, font=(font, font_size),
                        background=quality_colors(float(element.split()[1]))[1])
               for element in lbl_text]

    # Setting color of labels Wind, Pressure, Temp. on grey
    for lbl in all_lbl[-4:]:
        if lbl.cget('text').split()[0] in ['Temp.:', 'Pressure:', 'Humidity:', 'Wind:']:
            lbl.config(background='grey')

    # Putting labels in the window
    for row in range(2, total_rows+1):
        all_lbl[row-2].grid(row=row, column=0, sticky=tk.EW)

    # Refresh Button
    refresh_btn = tk.Button(text='Refresh', font=(font, font_size), command=refresh)
    refresh_btn.grid(row=total_rows+2, column=0, sticky=tk.EW)

    # OptionMenu
    city_menu = tk.OptionMenu(root, city_var, *cities.keys())
    city_menu.grid(row=total_rows+3, column=0, sticky=tk.EW)


def refresh():
    title_lbl.destroy()
    time_lbl.destroy()
    city_menu.destroy()
    refresh_btn.destroy()
    for label in all_lbl:
        label.destroy()
    get_data(cities[city_var.get()])
    print_lables()


# Program body
root = tk.Tk()
root.title('Weather quality')
get_data()
# App parameters
font = 'Helvetica'
font_size = 15
category_name = ['PM2.5', 'PM10', 'O3', 'NO2', 'SO2',
                 'CO', 'Temp.', 'Pressure', 'Humidity', 'Wind']
category_value = ['pm25', 'pm10', 'o3', 'no2', 'so2', 'co', 't', 'p', 'h', 'w']
cities = {
    'Piastów': '@8280',
    'Warszawa Marszałkowska': '@3391',
    'Warszawa Targówek': '@3392',
    'Warszawa': 'warszawa'
}
city_var = tk.StringVar()
city_var.set('Piastów')
print_lables()

tk.mainloop()
