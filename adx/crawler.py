"""crawler.py defines the ADX crawler and supporting functions.
   The functionality of ADX crawler.
   1. Navigate through the target directory
   2.

"""

from .adx_directory import DataDirectory


class Crawler:
    """ Crawler is designed to traverse all the items including the
        subdirectories in a directory. After the crawling, it returns a list of
        target files and their parser.

        Parameter
        ---------
        dir_name : str
            Directory name
        parsers : list
            A list of `Pareser object` for each item type.
        log_file: str
            The name of log_file

        Return
        ------
        A list of DirProcessors. These processors has the parser information so
        it can be sent to the logging function directly.
        Note
        ----
        Crawler only parses the item types that have the `Parser` object
        provided.
    """
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def walk(self, method='dfs'):
        return getattr(self, method)()

    def dfs(self):
        visited, stack = set(), [self.root_dir]
        result = {}
        while stack:
            cur = stack.pop()
            if cur not in visited:
                visited.add(cur)
                cur_info = DataDirectory(cur)
                result.update({cur: cur_info})
                stack.extend(set(cur_info.next) - visited)
        return result
