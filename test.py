#from PIL import Image, ImageTk
import tkinter
#import os
from tkintermapview import TkinterMapView

#create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{1000}x{700}")
root_tk.title("Aryan and Simon's Map")
root_tk.iconbitmap('c:/Users/ghosh/OneDrive/Documents/newhacks/rocket.ico')

#create map widget
map_widget = TkinterMapView(root_tk, width=1000, height=700, corner_radius=0)
#map_widget.set_address("45 Belgate Pl, Toronto, ON, Canada")
map_widget.set_position(43.6551250, -79.3870156) #Toronto
map_widget.set_zoom(10)
map_widget.pack(fill="both", expand=True)



def polygon_click(polygon):
    print(f"polygon clicked - text: {polygon.name}")

polygon_1 = map_widget.set_polygon([(43.7571324, -79.5173560),
                                    (43.7211418, -79.5087729),
                                    (43.7375158,-79.4345272),
                                    (43.7730173, -79.4438827)],
                                   fill_color= 'red',
                                   
                                    outline_color="black",
                                    border_width=1,
                                   command = polygon_click,
                                   name = "not safe" )

polygon_2 = map_widget.set_polygon([(43.6280781, -79.4047402),
                                    (43.6342284, -79.3952129),
                                    (43.6445396, -79.3600783),
                                    (43.6614311, -79.3152320),
                                    (43.6505018, -79.3099963),
                                    (43.6173091, -79.3178928),
                                    (43.6105978, -79.3446719),
                                    (43.6103492, -79.3920505)],
                                   fill_color= 'red',
                                   
                                    outline_color="black",
                                    border_width=1,
                                   command = polygon_click,
                                   name = "not safe" )





root_tk.mainloop()
polygon_1.remove_position(46.3772542, 6.4160156)
polygon_1.add_position(0, 0, index=5)
polygon_1.delete()

# methods
