"""adx typefilters
"""

import os
class TypeFilterBase(object):
    """TypeFilter class for defining file filters for parsing.

    Attributes
    ----------
    _targets : list
        list of filtered target filenames
    name : str
        filter name

    Methods
    -------
    _run(candFiles) : user-defined method
        Execute logic to filter filenames from `candFiles`.
        Return filtered file list `candFiles` with filtered
        target files removed from the input list.
    __call__(candFiles)
        Execute `self.run()`.
    add_target(target)
        Append new target file to internal list of targets.

    Notes
    -----
    The complexity of a TypeFilter object implementation is left
    completely up to the user. The only requirement that should be
    adhered to is specified in `run()`'s docstring.
    """

    def __init__(self, name, tabletype):
        self.targets = []
        self._name = str(name)
        self._tabletype = str(tabletype)

    def __call__(self, *args, **kwargs):
        """Execute `self._run()` with the provided arguments to filter
        targets according to user-defined logic.
        """
        return self._run(*args, **kwargs)

    @property
    def tabletype(self):
        return self._tabletype

    @property
    def name(self):
        return self._name

    @property
    def targets(self):
        """Internal list of targets."""
        return self._targets

    @targets.setter
    def targets(self, targetList):
        """Set internal target list"""
        self._targets = targetList

    def add_target(self, target):
        """Add new target file to internal targets list
        """
        if target not in self.targets:
            self._targets.append(target)
        else:
            print("Skipping duplicate target: {}".format(target))

    def _run(self, *args, **kwargs):
        """Apply user-defined logic to determine which of the provided
        candidate files should be filtered.

        Returns
        -------
        result : list
            Filtered target list, with filtered targets removed from
            the original list.
        """
        raise NotImplementedError, "user-defined method"


class ExtFilter(TypeFilterBase):
    """extension filter

    Filter targets by file extension

    Parameters
    ----------
    ext : str or list
        file extension to look for when filtering targets.
        `ext` can either be a string containing a file extension or a list of
        strings containing multile file extenstions to be filtered.
    name : str, optional
        name of ExtFilter implementation, defaults to "ExtFilter"
    """

    def __init__(self, ext, name='ExtFilter'):
        super(ExtFilter, self).__init__(name, name)
        if isinstance(ext, str):
            self.ext = list([ext])
        elif isinstance(ext, list):
            self.ext = ext
        elif not isinstance(ext, list):
            raise TypeError("extension must be list or string")

    def _run(self, candTargets):
        """filter candidate target files

        Parameters
        ----------
        candTargets : list
            list of candidate target files to be checked

        Returns
        -------
        (filtered_targets, unfiltered_targets) : tuple
            tuple of lists containing the targets filtered
            and the leftover unfiltered targets.
        """

        cands = []
        for cand in candTargets:
            for e in self.ext:
                if cand.endswith(e):
                    self.add_target(cand)
                    break
            else:
                cands.append(cand)

        result = (self.targets, cands)
        return result
