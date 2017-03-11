from WOMlenses import *
import os

def create_includes():
    c = ""
    c += '#include "colors.inc"\n\n'
    return c

def create_background():
    c  = ""
    c += "\n\t//\t\tHere goes the background definition\n"
    c += "background {color Silver}\n\n"
    return c


def create_lights():
    c = ""
    c += "\t//\t\tHere go the light definitions\n"
    c += "light_source { <8, 8, 8> color White}\n"
    c += "light_source { <8, 8, -8> color White}\n"

    c   += "light_source { <8, -8, 8> color White}\n"
    c += "light_source { <8, -8, -8> color White}\n\n"

    return c

def create_camera():
    c  = ""
    c += "\t//\t\tHere goes the camera definition\n"
    c += "camera {location <50, 30, 50> look_at <0, 0, 0>}\n"

    return c

def create_axis():
    c  = ""
    c += "\t//\t\tHere go the axis definition\n"
    c += "#declare L_axis = 40;\n"
    c += "#declare r_axis = 0.2 ;\n"

    c += "cylinder { <  0, 0, 0>,\n" +\
                    "\t< L_axis, 0, 0>,\n" +\
                    "\tr_axis\n"\
                    "\topen\n" +\
                    "\ttexture{ pigment {color Red transmit 0.75}}}\n"
    c += "cylinder { <  0, 0, 0>,\n" +\
                    "\t<  0, L_axis, 0>,\n" +\
                    "\tr_axis\n"\
                    "\topen\n" +\
                    "\ttexture{ pigment {color Green transmit 0.75}}}\n"
    c += "cylinder { <  0, 0, 0>,\n" +\
                    "\t<  0, 0, L_axis>,\n" +\
                    "\tr_axis\n"\
                    "\topen\n" +\
                    "\ttexture{ pigment {color Blue transmit 0.75}}}\n\n"
    return c

def create_pov_lens(lens):
    c  = ""
    c += "\t//\t\tHere goes a lens \n"
    curv_lens = lens['lens_charateristics']['Radius of Curvature']
    thickness = lens['lens_charateristics']['Center Thickness']
    diameter = lens['lens_charateristics']['Diameter']
    c += "#declare Curv_lens = " + str(curv_lens) + ";\n"
    c += "#declare Lens_thickness = " + str(thickness) + ";\n"
    c += "#declare Lens_diameter = "+str(diameter)+";\n"
    c += "#declare Left_sphere =\n" + \
         "\tsphere { <0,Curv_lens,0>, \n" + \
                   "\tCurv_lens}\n"
    c += "intersection {\n"+\
                        "\tobject{Left_sphere}\n"  +\
                        "\tobject{Left_sphere\n"   +\
                                "\t\trotate 180*x\n" +\
                                "\t\ttranslate Lens_thickness*y}\n"+\
                        "\tobject{cylinder{<0,0,0>,<0,Lens_thickness,0>,Lens_diameter/2.}}\n"+\
                        "\ttexture {pigment { color LightBlue transmit 0.35}}\n"+\
                    "\t}\n"

    return c
'''----------------------------------------

                Main

---------------------------------------------- '''

c =""
# Include files
c += create_includes()
# Camera
c += create_camera()

# Background
c += create_background()

# Light
c += create_lights()

# Draw the 3d axis
c += create_axis()

                # Objects to draw
# Draw the lens
lens1 = choose_lens('Newport KBX043', 10.)
c += create_pov_lens(lens1)

#Create pov file and write its content
f = open('test.pov','w')
f.write(c)
f.close()

# Execute povray on the pov file
os.system("povray test.pov +W900 +H480")
