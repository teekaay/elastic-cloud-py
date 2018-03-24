"""
This module contains various methods and classes related to the
Elastic Cloud Enterprise (on-premise) variant which may or may 
not be present in the SaaS variant.
"""

ROOT_USER = 'root'
READONLY_USER = 'readonly'

class Authorization(object):
    @staticmethod
    def readonly_user():
        """
        Returns the predefined readonly user name.
        """
        return READONLY_USER

    @staticmethod
    def root_user():
        """
        Returns the predefined admin/root user name.
        """
        return ROOT_USER