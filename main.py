# coding: utf-8
from solids import *
from draw import *

def main_q1():

    cube = Parallelepiped()
    cube.create_parallelepiped(origin_point =(-0.75,-0.75,0),edge = 1.5)
    plot_solids([(cube,"red")])

    parallelepiped = Parallelepiped()
    parallelepiped.create_parallelepiped(origin_point =(0,0,0), x=1.5, y=5, z=2.5)
    plot_solids([(parallelepiped,"blue")])
  
    pyramid = Pyramid()
    pyramid.create_pyramid(origin_point = (-1,-1,0), edge = 2, z = 3)
    pyramid.solid_rotation(45,pivot_point = (0,0,0))
    plot_solids([(pyramid,"black")])
  
    pyramid_trunk = Pyramid_trunk()
    pyramid_trunk.create_pyramid_trunk(lower_edge = 3, upper_edge = 1.3, z = 2.5)
    plot_solids([(pyramid_trunk,"brown")])
    
    
def main_q2():
    
    solids_list = []
    
    cube = Parallelepiped()
    cube.create_parallelepiped(origin_point =(0.5,0,0),edge = 1.5)
    solids_list.append((cube,"red"))

    parallelepiped = Parallelepiped()
    parallelepiped.create_parallelepiped(origin_point =(-2,0,0), x=1.5, y=5, z=2.5)
    solids_list.append((parallelepiped,"blue"))
  
    pyramid = Pyramid()
    pyramid.create_pyramid(origin_point = (2.5,0,0), edge = 2, z = 3)
    solids_list.append((pyramid,"black"))
  
    pyramid_trunk = Pyramid_trunk()
    pyramid_trunk.create_pyramid_trunk(origin_point = (-5.5,0,0),lower_edge = 3, upper_edge = 1.3, z = 2.5)
    solids_list.append((pyramid_trunk,"green"))
    
    plot_solids(solids_list,view = "3d")
    
def main_q3():
    
    cube = Parallelepiped()
    cube.create_parallelepiped(origin_point =(0.5,0,0),edge = 1.5)

    parallelepiped = Parallelepiped()
    parallelepiped.create_parallelepiped(origin_point =(-2,0,0), x=1.5, y=5, z=2.5)
      
    pyramid = Pyramid()
    pyramid.create_pyramid(origin_point = (2.5,0,0), edge = 2, z = 3)
    
    pyramid_trunk = Pyramid_trunk()
    pyramid_trunk.create_pyramid_trunk(origin_point = (-5.5,0,0),lower_edge = 3, upper_edge = 1.3, z = 2.5)

    '''A aaprtir daqui e necessario revisar oq ta acontecendo'''
    eye_coordinates = (-6, -6, 6)
    VV_mid_point = Solid.solid_vision_volume([cube, pyramid,parallelepiped,pyramid_trunk])

    camera_axis = create_camera_axis(VV_mid_point, eye_coordinates)

    cube.vertices = np.matmul(camera_axis, cube.vertices.T).T
    pyramid.vertices = np.matmul(camera_axis, pyramid.vertices.T).T
    parallelepiped.vertices = np.matmul(camera_axis, parallelepiped.vertices.T).T
    pyramid_trunk.vertices = np.matmul(camera_axis, pyramid_trunk.vertices.T).T
    
    
    solids_list = []
    solids_list.append((cube,"red"))
    solids_list.append((parallelepiped,"blue"))
    solids_list.append((pyramid,"black"))
    solids_list.append((pyramid_trunk,"green"))
    
    for solid,color in solids_list:
        solid.update_solid_features()
    
    plot_solids(solids_list, eye = (eye_coordinates,camera_axis))

if __name__ == "__main__":
    #main_q1()
    #main_q2()
    main_q3()
