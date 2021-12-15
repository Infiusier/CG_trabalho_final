# coding: utf-8
from solids import *
from draw import *

def matrix_multiplication(vertices_matrix, rt_matrix):
    vertices_matrix = np.hstack((vertices_matrix, np.ones((len(vertices_matrix), 1))))
    vertices_matrix = np.matmul(vertices_matrix, rt_matrix)
    vertices_matrix = np.delete(vertices_matrix, 3, axis=1)
    return vertices_matrix

def main_q1():

    draw = Draw()

    cube = Parallelepiped()
    cube.create_parallelepiped(origin_point =(-0.75,-0.75,0),edge = 1.5)
    draw.draw_solids([(cube,"red")])

    parallelepiped = Parallelepiped()
    parallelepiped.create_parallelepiped(origin_point =(0,0,0), x=1.5, y=5, z=2.5)
    draw.draw_solids([(parallelepiped,"blue")])
  
    pyramid = Pyramid()
    pyramid.create_pyramid(origin_point = (-1,-1,0), edge = 2, z = 3)
    pyramid.solid_rotation(45,pivot_point = (0,0,0))
    draw.draw_solids([(pyramid,"black")])
  
    pyramid_trunk = Pyramid_trunk()
    pyramid_trunk.create_pyramid_trunk(lower_edge = 3, upper_edge = 1.3, z = 2.5)
    draw.draw_solids([(pyramid_trunk,"brown")])
    
    
def main_q2():
    
    draw = Draw()
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
    
    draw.draw_solids(solids_list,view = "3d")
    
def main_q3():
    
    draw = Draw()
    
    cube = Parallelepiped()
    cube.create_parallelepiped(origin_point =(0.5,0,0),edge = 1.5)

    parallelepiped = Parallelepiped()
    parallelepiped.create_parallelepiped(origin_point =(-2,0,0), x=1.5, y=5, z=2.5)
      
    pyramid = Pyramid()
    pyramid.create_pyramid(origin_point = (2.5,0,0), edge = 2, z = 3)
    
    pyramid_trunk = Pyramid_trunk()
    pyramid_trunk.create_pyramid_trunk(origin_point = (-5.5,0,0),lower_edge = 3, upper_edge = 1.3, z = 2.5)

    eye_coordinates = (-6, -6, 6)
    VV_mid_point = Solid.solid_vision_volume([cube, pyramid,parallelepiped,pyramid_trunk])

    camera_axis = draw.create_camera_axis(VV_mid_point, eye_coordinates)
    inverse_camera_axis = np.linalg.inv(camera_axis)
    
    rt_matrix = np.array([[camera_axis[0][0],camera_axis[0][1],camera_axis[0][2],(-eye_coordinates[0] * camera_axis[0][0]) + (-eye_coordinates[1] * camera_axis[0][1]) + (-eye_coordinates[2] * camera_axis[0][2])],
                          [camera_axis[1][0],camera_axis[1][1],camera_axis[1][2],(-eye_coordinates[0] * camera_axis[1][0]) + (-eye_coordinates[1] * camera_axis[1][1]) + (-eye_coordinates[2] * camera_axis[1][2])],
                          [camera_axis[2][0],camera_axis[2][1],camera_axis[2][2],(-eye_coordinates[0] * camera_axis[2][0]) + (-eye_coordinates[1] * camera_axis[2][1]) + (-eye_coordinates[2] * camera_axis[2][2])],
                          [0,0,0,1]])
    
    
    cube.vertices = matrix_multiplication(cube.vertices,rt_matrix)
    pyramid.vertices = matrix_multiplication(pyramid.vertices,rt_matrix)
    parallelepiped.vertices = matrix_multiplication(parallelepiped.vertices,rt_matrix)
    pyramid_trunk.vertices = matrix_multiplication(pyramid_trunk.vertices,rt_matrix)
    
    solids_list = []
    solids_list.append((cube,"red"))
    solids_list.append((parallelepiped,"blue"))
    solids_list.append((pyramid,"black"))
    solids_list.append((pyramid_trunk,"green"))
    
    for solid,color in solids_list:
        solid.update_solid_features()
    
    draw.draw_solids(solids_list, eye = (eye_coordinates,inverse_camera_axis))
    
def main_q4():
    
    draw = Draw()
    
    cube = Parallelepiped()
    cube.create_parallelepiped(origin_point =(0.5,0,0),edge = 1.5)

    parallelepiped = Parallelepiped()
    parallelepiped.create_parallelepiped(origin_point =(-2,0,0), x=1.5, y=5, z=2.5)
      
    pyramid = Pyramid()
    pyramid.create_pyramid(origin_point = (2.5,0,0), edge = 2, z = 3)
    
    pyramid_trunk = Pyramid_trunk()
    pyramid_trunk.create_pyramid_trunk(origin_point = (-5.5,0,0),lower_edge = 3, upper_edge = 1.3, z = 2.5)

    eye_coordinates = (-6, -6, 6)
    VV_mid_point = Solid.solid_vision_volume([cube, pyramid,parallelepiped,pyramid_trunk])

    camera_axis = draw.create_camera_axis(VV_mid_point, eye_coordinates)
    
    rt_matrix = np.array([[camera_axis[0][0],camera_axis[0][1],camera_axis[0][2],(-eye_coordinates[0] * camera_axis[0][0]) + (-eye_coordinates[1] * camera_axis[0][1]) + (-eye_coordinates[2] * camera_axis[0][2])],
                          [camera_axis[1][0],camera_axis[1][1],camera_axis[1][2],(-eye_coordinates[0] * camera_axis[1][0]) + (-eye_coordinates[1] * camera_axis[1][1]) + (-eye_coordinates[2] * camera_axis[1][2])],
                          [camera_axis[2][0],camera_axis[2][1],camera_axis[2][2],(-eye_coordinates[0] * camera_axis[2][0]) + (-eye_coordinates[1] * camera_axis[2][1]) + (-eye_coordinates[2] * camera_axis[2][2])],
                          [0,0,0,1]])
    
    
    cube.vertices = matrix_multiplication(cube.vertices,rt_matrix)
    pyramid.vertices = matrix_multiplication(pyramid.vertices,rt_matrix)
    parallelepiped.vertices = matrix_multiplication(parallelepiped.vertices,rt_matrix)
    pyramid_trunk.vertices = matrix_multiplication(pyramid_trunk.vertices,rt_matrix)
    
    projection_2d = [[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 0]]
    
    cube.vertices = np.dot(cube.vertices,projection_2d)
    pyramid.vertices = np.dot(pyramid.vertices,projection_2d)
    parallelepiped.vertices = np.dot(parallelepiped.vertices,projection_2d)
    pyramid_trunk.vertices = np.dot(pyramid_trunk.vertices,projection_2d)
    
    solids_list = []
    solids_list.append((cube,"red"))
    solids_list.append((parallelepiped,"blue"))
    solids_list.append((pyramid,"black"))
    solids_list.append((pyramid_trunk,"green"))
    
    for solid,color in solids_list:
        solid.update_solid_features()
    
    draw.draw_solids(solids_list, eye = (eye_coordinates,camera_axis),view = "2d")

if __name__ == "__main__":
    main_q1()
    main_q2()
    main_q3()
    main_q4()
