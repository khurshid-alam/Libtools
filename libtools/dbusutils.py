# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
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

import dbus
import subprocess

def _search_bus_name(SERVICE_NAME_FILTER, activate=False):

    interface = None
    obj = None
    sbus = dbus.SessionBus()

    try:
        #check for running pidgin (code from note.py)
        proxy_obj = sbus.get_object('org.freedesktop.DBus', '/org/freedesktop/DBus')
        dbus_iface = dbus.Interface(proxy_obj, 'org.freedesktop.DBus')
        bus_names = dbus_iface.ListActivatableNames()
        eds_cal = list(filter(lambda x:SERVICE_NAME_FILTER in x, bus_names))
        if eds_cal:
            EDS_FACTORY_BUS = eds_cal[0]
    except dbus.exceptions.DBusException as err:
        pretty.print_debug(err)
    return EDS_FACTORY_BUS


def _create_dbus_connection(SERVICE_NAME, OBJECT_NAME, IFACE_NAME, activate=False):
    ''' Create dbus connection to Gnote
    @activate: true=starts Gnote if not running
    '''
    interface = None
    obj = None
    sbus = dbus.SessionBus()

    try:
        proxy_obj = sbus.get_object('org.freedesktop.DBus', '/org/freedesktop/DBus')
        dbus_iface = dbus.Interface(proxy_obj, 'org.freedesktop.DBus')
        cmd = 'qdbus {}'.format(SERVICE_NAME)
        while OBJECT_NAME not in ((subprocess.check_output(cmd, shell=True)).decode("utf-8")).split("\n"):
            pass
        if activate or dbus_iface.NameHasOwner(SERVICE_NAME):
            obj = sbus.get_object(SERVICE_NAME, OBJECT_NAME)
        if obj:
            interface = dbus.Interface(obj, IFACE_NAME)
    except dbus.exceptions.DBusException as err:
        print(__name__, err)
    return interface
