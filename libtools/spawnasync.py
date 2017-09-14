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


import gi
gi.require_version('GLib', '2.0')
from gi.repository import GLib
from libtools import pretty

class SpawnError (Exception):
    "Error starting application"

def spawn_async(argv, in_dir="."):
    """
    Silently spawn @argv in the background

    Returns False on failure
    """
    try:
        return spawn_async_raise(argv, in_dir)
    except SpawnError as exc:
        pretty.print_debug(__name__, "spawn_async", argv, exc)
        return False

def spawn_async_raise(argv, workdir="."):
    """
    A version of spawn_async that raises on error.

    raises SpawnError
    """
    # FIXME: How to support locale strings?
    argv
    #argv = _argv_to_locale(argv)
    pretty.print_debug(__name__, "spawn_async", argv, workdir)
    try:
        return GLib.spawn_async (argv, working_directory=workdir,
                flags=GLib.SPAWN_SEARCH_PATH)
    except GLib.GError as exc:
        raise SpawnError(exc.message)
