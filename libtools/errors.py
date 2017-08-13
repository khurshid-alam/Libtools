# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------

"""Internal Friends exceptions."""


__all__ = [
    'AuthorizationError',
    'FriendsError',
    'UnsupportedProtocolError',
    ]


try:
    from contextlib import ignored
except ImportError:
    from contextlib import contextmanager

    # This is a fun toy from Python 3.4, but I want it NOW!!
    @contextmanager
    def ignored(*exceptions):
        """Context manager to ignore specifed exceptions.

             with ignored(OSError):
                 os.remove(somefile)

        Thanks to Raymond Hettinger for this.
        """
        try:
            yield
        except exceptions:
            pass

