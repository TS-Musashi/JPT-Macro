class Utils:
    """JptUtils class"""
    def __init__(self):
        if self.__class__.__name__ == 'JptUtils':
            raise TypeError('JptUtils is abstract base class')

    @staticmethod
    def find_between(s, first, last):
        """
        Get string between 2 sub strings
        :param s: target string
        :param first: first sub string
        :param last: last sub string
        :return: string in the middle of first and last
        """
        try:
            start = s.index(first) + len(first)
            end = s.index(last, start)
            return s[start:end]
        except ValueError:
            return ""

    def convert_to_cursors(self, cursors):
        """Convert JPT cursors to standard"""
        cursor_list = cursors[1:-1].split(",")
        cursor_list_mod = ["[" + s + "]" for s in cursor_list]
        node_cursors_mod = "[" + ",".join(cursor_list_mod) + "]"
        return node_cursors_mod

    def get_id_from_cursor(self, cursor):
        """"Extract JPT cursor index
        :param cursor: Jupiter cursor, e.g. [5:10]
        :return: id of cursor in integer type
        """
        cursor_id = int(self.__class__.find_between(cursor, ":", "]"))
        return cursor_id

    def get_ids_list_from_cursors(self, cursors):
        """"Extract JPT ids into a list
        :param cursors: list of cursors, e.g. [[5:1], [5:10], [5:12]]
        :return: a tuple of ids
        """
        cursor_list = tuple(cursors.split(","))
        ids_list = []
        for i in range(len(cursor_list)):
            ids_list.append(self.get_id_from_cursor(cursor_list[i]))
        return tuple(ids_list)

    def get_max_id_from_cursors(self, cursors):
        """"Get maximum id from the cursors list
        :param cursors: list of cursors, e.g. [[5:1], [5:10], [5:12]]
        :return: maximum id in the cursors list in integer type
        """
        max_id = max(self.get_ids_list_from_cursors(cursors))
        return max_id

    def get_min_id_from_cursors(self, cursors):
        """"Get minimum id from the cursors list
        :param cursors: list of cursors, e.g. [[5:1], [5:10], [5:12]]
        :return: minimum id in the cursors list in integer type
        """
        min_id = min(self.get_ids_list_from_cursors(cursors))
        return min_id
