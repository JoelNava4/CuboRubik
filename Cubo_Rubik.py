import pandas as pd
import numpy as np

class RubikCube:
    def __init__(self, nombre_archivo):
        self.cube = pd.read_csv(nombre_archivo)
        self.colors = set()
        self.valid = True
        self.intersections = {
            "Up": {
                0: [(0, "Left"), (2, "Back")],
                1: [(1, "Back")],
                2: [(0, "Back"), (2, "Right")],
                3: [(1, "Left")],
                5: [(1, "Right")],
                6: [(2, "Left"), (0, "Front")],
                7: [(1, "Front")],
                8: [(0, "Right"), (2, "Front")]
            },
            "Front": {
                0: [(6, "Up"), (2, "Left")],  
                1: [(7, "Up")], 
                2: [(8, "Up"), (0, "Right")],
                3: [(5, "Left")],
                5: [(3, "Right")],
                6: [(8, "Left"), (8, "Down")],
                7: [(7, "Down")],
                8: [(6, "Down"), (6, "Right")]
            },
            "Left": {
                0: [(0, "Up"), (2, "Back")],  
                1: [(3, "Up")], 
                2: [(6, "Up"), (0, "Front")],
                3: [(5, "Back")],
                5: [(3, "Front")],
                6: [(8, "Back"), (2, "Down")],
                7: [(5, "Down")],
                8: [(6, "Front"), (8, "Down")]
            },
            "Right": {
                0: [(8, "Up"), (2, "Front")],  
                1: [(5, "Up")], 
                2: [(2, "Up"), (0, "Back")],
                3: [(5, "Front")],
                5: [(3, "Back")],
                6: [(8, "Front"), (6, "Down")],
                7: [(3, "Down")],
                8: [(0, "Down"), (6, "Back")]
            },
            "Down": {
                0: [(6, "Back"), (8, "Right")],  
                1: [(7, "Back")], 
                2: [(8, "Back"), (6, "Left")],
                3: [(7, "Right")],
                5: [(7, "Left")],
                6: [(8, "Front"), (6, "Right")],
                7: [(7, "Front")],
                8: [(6, "Front"), (8, "Left")]
            },
            "Back": {
                0: [(2, "Up"), (2, "Right")],  
                1: [(1, "Up")], 
                2: [(0, "Up"), (0, "Left")],
                3: [(5, "Right")],
                5: [(3, "Left")],
                6: [(8, "Right"), (0, "Down")],
                7: [(1, "Down")],
                8: [(2, "Down"), (6, "Left")]
            }
        }
        self.histori_solution = []
        print(self.cube)
    
    def valid_nine_elements_for_faces(self,transposed_cube):
        for i in range(6):
            if transposed_cube.iloc[i].count() != 9:
                self.valid = False
                print("La cara", self.cube.columns[i], "no tiene 9 elementos.")
                break

    def valid_nine_repeat_color(self,transposed_cube):
        for color in transposed_cube.values.flatten().tolist():
            if transposed_cube.values.flatten().tolist().count(color) != 9:
                self.valid = False
                print("El color :", color, "no cumple con los requisitos para validar el cubo")
                break

    def valid_diferent_color_center_faces(self,transposed_cube):
        for i in range(6):
            color = transposed_cube.iloc[i, 4]
            if color in self.colors:
                self.valid = False
                print("El color del centro de la cara", self.cube.columns[i], "ya ha sido utilizado.")
                break
            else:
                self.colors.add(color)

    def check_intersection_colors(self):
        for face, positions in self.intersections.items():
            for pos, intersections_with in positions.items():
                colors_checked = set()
                colors_checked.add(self.cube[face][pos])
                for intersection in intersections_with:
                    pos_intersection , nombre_face_intersection = intersection
                    color_face = self.cube[nombre_face_intersection][pos_intersection]
                    if color_face in colors_checked:
                        print(f"Error: El color en la posición {pos_intersection} de la cara {nombre_face_intersection} ya ha sido encontrado en una intersección previa.")
                        self.valid = False
                        return
                    colors_checked.add(color_face)

    
    def is_valid(self):
        transposed_cube = self.cube.transpose()    
        self.valid_nine_elements_for_faces(transposed_cube)
        if self.valid:
            self.valid_nine_repeat_color(transposed_cube)
            if self.valid:
                self.valid_diferent_color_center_faces(transposed_cube)
                if self.valid:
                    self.check_intersection_colors()
        return self.valid

    def rotate_clockwise_Up(self):
        rotated_face = self.cube["Up"].values.reshape(3, 3)
        self.cube["Up"] = pd.Series(np.rot90(rotated_face, -1).flatten())
        colors_Left, colors_Right = self.cube.loc[0:2, 'Front'].values.copy(), self.cube.loc[0:2, 'Back'].values.copy()
        colors_Front, colors_Back = self.cube.loc[0:2, 'Right'].values.copy(), self.cube.loc[0:2, 'Left'].values.copy()
        self.cube.loc[0:2, 'Front'],self.cube.loc[0:2, 'Back'] = colors_Front,colors_Back
        self.cube.loc[0:2, 'Right'],self.cube.loc[0:2, 'Left'] = colors_Right,colors_Left
        print(self.cube)

    def rotate_counterclockwise_Up(self):
        rotated_face = self.cube["Up"].values.reshape(3, 3)
        self.cube["Up"] = pd.Series(np.rot90(rotated_face).flatten())
        colors_Left, colors_Right = self.cube.loc[0:2, 'Back'].values.copy(), self.cube.loc[0:2, 'Front'].values.copy()
        colors_Front, colors_Back = self.cube.loc[0:2, 'Left'].values.copy(), self.cube.loc[0:2, 'Right'].values.copy()
        self.cube.loc[0:2, 'Front'],self.cube.loc[0:2, 'Back'] = colors_Front,colors_Back
        self.cube.loc[0:2, 'Right'],self.cube.loc[0:2, 'Left'] = colors_Right,colors_Left
        print(self.cube)

nombre_archivo = "Cubo0.txt"
rubik_cube = RubikCube(nombre_archivo)
print("El cubo es válido:", rubik_cube.is_valid())
rubik_cube.rotate_clockwise_Up()
rubik_cube.rotate_counterclockwise_Up()