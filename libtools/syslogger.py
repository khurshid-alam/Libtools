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
import logging
import logging.handlers
#from friends.utils.logging import initialize


class logstderr:
    def write(self, data):
        Log.error('%s' % data)


def _get_logger():
    Log = logging.getLogger(__name__)
    Log.setLevel(logging.DEBUG)

    handler = logging.handlers.SysLogHandler(address = '/dev/log')

    formatter = logging.Formatter('%(filename)-5s[%(process)d] %(levelname)-10s %(message)s')
    handler.setFormatter(formatter)

    Log.addHandler(handler)

    #syslog.openlog('test[%u]' % os.getpid())

    return Log




