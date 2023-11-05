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
    print(f"{polygon.name}")

polygon_1 = map_widget.set_polygon([(43.7571324, -79.5173560),
                                    (43.7211418, -79.5087729),
                                    (43.7375158,-79.4345272),
                                    (43.7730173, -79.4438827)],
                                   fill_color= 'orange',
                                   
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

polygon_3 = map_widget.set_polygon([(43.6748033, -79.6789024),
                                    (43.6571703, -79.6558997),
                                    (43.6517055 ,-79.6191642),
                                    (43.6628830, -79.5951316),
                                    (43.6718235, -79.5875785),
                                    (43.6844868, -79.5927283),
                                    (43.7055865, -79.6280906),
                                    (43.6944170, -79.6613929)],
                                   fill_color= 'red',
                                   
                                    outline_color="black",
                                    border_width=1,
                                   command = polygon_click,
                                   name = "not safe" )

polygon_4 = map_widget.set_polygon([(43.7850819, -79.3411494),
                                    (43.7766541, -79.3541957),
                                    (43.7664896, -79.3651820),
                                    (43.7526036, -79.3565989),
                                    (43.7454113, -79.3322230),
                                    (43.7555794, -79.3030406),
                                    (43.7734314, -79.2903377),
                                    (43.7858254, -79.3129970)],
                                   fill_color= 'red',
                                   
                                    outline_color="black",
                                    border_width=1,
                                   command = polygon_click,
                                   name = "not safe" )

polygon_5 = map_widget.set_polygon([(43.6402534, -79.5434545),
                                    (43.6347576, -79.5432337),
                                    (43.6285142, -79.5366247),
                                    (43.6322417, -79.5242651),
                                    (43.6408140, -79.5262392),
                                    (43.6434849, -79.5264967)],
                                   fill_color= 'red',
                                   
                                    outline_color="black",
                                    border_width=1,
                                   command = polygon_click,
                                   name = "not safe" )

polygon_6 = map_widget.set_polygon([(43.6474755, -79.3815078),
                                    (43.6457985, -79.3845977),
                                    (43.6418234, -79.3847693),
                                    (43.6407675, -79.3810786),
                                    (43.6413265, -79.3778171),
                                    (43.6462644, -79.3752421)],
                                   fill_color= 'red',
                                   
                                    outline_color="black",
                                    border_width=1,
                                   command = polygon_click,
                                   name = "not safe" )

polygon_7 = map_widget.set_polygon([(43.6546761, -79.3876223),
                                    (43.6511440, -79.3862383),
                                    (43.6524249, -79.3803265),
                                    (43.6559965, -79.3812805)],
                                   fill_color= 'red',
                                   
                                    outline_color="black",
                                    border_width=1,
                                   command = polygon_click,
                                   name = "not safe" )
#####################################################################
######################## ORANGE ZONES ###############################
#####################################################################





root_tk.mainloop()
polygon_1.remove_position(46.3772542, 6.4160156)
polygon_1.add_position(0, 0, index=5)
polygon_1.delete()

# methods
