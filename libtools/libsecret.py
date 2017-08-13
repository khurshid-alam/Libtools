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

#gi libraries import
# reference: https://people.gnome.org/~stefw/libsecret-docs/py-examples.html
import gi
try:
    gi.require_version('Secret', '1')
except Exception as e:
    print(e)
    exit(-1)
    
from gi.repository import Secret


class Libsecret(object):
    def __init__(self):
        self._collection = Secret.COLLECTION_DEFAULT
        self._xdg_chema = 'org.freedesktop.Secret.Generic'
        self._flags = Secret.SchemaFlags.NONE
        
        
    def _make_schema(self, **kwargs):
        if kwargs:
            schema_args = {}
            for k,v in kwargs.items():
                if isinstance(k, str):
                    schema_args[k] = Secret.SchemaAttributeType.STRING
                elif  isinstance(k, str):
                    schema_args[k] = Secret.SchemaAttributeType.INTEGER
                elif  isinstance(k, bool):
                    schema_args[k] = Secret.SchemaAttributeType.BOOLEAN
                else:
                    print ("Error: Only string,integer and boolean values are allowed")
                    return None        
            ex_schema = Secret.Schema.new("org.freedesktop.Secret.Generic",
                                                Secret.SchemaFlags.NONE, 
                                                schema_args)
            return ex_schema
            
        else:
            return None
            
            
    def _store_secret(self, ex_schema, 
                        kwargs,
                        label,
                        password):
        
        Secret.password_store_sync(ex_schema, 
                                    kwargs, 
                                    self._collection,
                                    label, password, None)
                                    
                                    
    def _get_secret(self, ex_schema, kwargs):
        password = Secret.password_lookup_sync(ex_schema, kwargs, None)
        return password
        
        
    def _remove_secret(self, ex_schema, kwargs):
        result = Secret.password_clear_sync(ex_schema, kwargs, None)
        return result
        
        
        
        
        
        
        
        
        
        
        
            
                     
