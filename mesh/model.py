import jpt
from utils import *


class Model(Utils):
    """class working with JPT Model"""
    def __init__(self, model_name):
        """Constructor"""
        Utils.__init__(self)
        self.model_name = model_name
        self.part_cursor = JPT.Exec('FindEntities("{0}", "Part",0)'.format(self.part_name))
        self.part_id = self.get_id_from_cursor(self.part_cursor)
