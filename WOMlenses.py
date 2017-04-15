
def choose_lens(lens_choice, distance):
    if lens_choice=='Newport KBX043':
        lens_characteristics\
             ={'Lens Shape': 'Bi-Convex',\
               'length unit': 'mm',\
               'Diameter': 25.4,\
               'Lens Material': 'N-BK7',\
               'Antireflection Coating': "Uncoated",\
               'Effective Focal Length': 19.0,\
               'Surface Quality': "40-20 scratch-dig",\
               'Surface Accuracy Irregularity': "lambda/4",\
               'Surface Accuracy, Power': '1.5 lambda',\
               'Surface Flatness': 'lambda/4',\
               'Focal Length, Back': 13.28,\
               'F/#': 0.7,\
               'Centration': '<=3 arc min',\
               'Principle Plane 2': -5.71,\
               'Principle Plane 1': 5.71,
               'Radius of Curvature': 16.687,
               'Chamfers': '0-0.8 mm face width',
               'Chamfers Angle/Tolerance': '45deg +-15deg, typical',
               'Diameter Tolerance': '+0/-0.1 mm',
               'Focal Length Tolerance': '+-1 %',
               'Center Thickness': 14.725,
               'Center Thickness Tolerance': '+-0.1 mm',
               'Edge Thickness': 3.0,
               'Clear Aperture': '>=central 90% of diameter'}
        lens = { 'lens_charateristics':lens_characteristics,\
                 'position':distance}
        return lens
    return 'None'

def lens_info(lens):
    print ("\t\tLens information")
    print ("\nLens Characteristics")
    for key in lens['lens_charateristics'].keys():
        print (key,":",lens['lens_charateristics'][key])
    print ( "\nLens Position" )
    print ( lens["position"]  )

    return
