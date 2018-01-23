import jpt
from utils import *


class Part(Utils):
    """class working with JPT Part"""
    def __init__(self, part_name):
        """Constructor"""
        Utils.__init__(self)
        self.part_name = part_name
        self.part_cursor = JPT.Exec('FindEntities("{0}", "Part",0)'.format(self.part_name))
        self.part_id = self.get_id_from_cursor(self.part_cursor)

    def get_part_id(self):
        """Return part id in integer type"""
        return self.part_id

    def get_max_node_id(self):
        """Get the maximum node id in the part in integer type"""
        node_cursors = JPT.Exec('AssociatedPick({0}, "Node", "UNKNOWN")'.format(self.part_cursor))
        node_cursors_mod = self.convert_to_cursors(node_cursors)
        max_node_id = self.get_max_id_from_cursors(node_cursors_mod)
        return max_node_id

    def get_min_node_id(self):
        """Get the minimum node id in the part in integer type"""
        node_cursors = JPT.Exec('AssociatedPick({0}, "Node", "UNKNOWN")'.format(self.part_cursor))
        node_cursors_mod = self.convert_to_cursors(node_cursors)
        min_node_id = self.get_min_id_from_cursors(node_cursors_mod)
        return min_node_id

    #Bug
    def surface_mesh(self):
        """"Surface mesh current part"""
        JPT.Exec('SurfaceMeshing2D({0}, {5, 10, 1, 1, 0.7853981634, 0.001, 1.25, 0.1, 0.1, 0.7, 0.5, 1, 3, 0, 0, 0, 0.524, 0, 0, 0, 0, 0, 0, 0, 0, 10000000, 0, 0}, 1, 0, 4, 1, 0, 65280)'.format(self.part_cursor))
        return 1

    def solid_mesh(self):
        return 1

    def remove_solid_mesh(self):
        return 1
