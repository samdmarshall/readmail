# Copyright (c) 2016, Samantha Marshall (http://pewpewthespells.com)
# All rights reserved.
#
# https://github.com/samdmarshall/readmail
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation and/or
# other materials provided with the distribution.
#
# 3. Neither the name of Samantha Marshall nor the names of its contributors may
# be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import configparser
from .helpers.Logger   import Logger

class MailboxConfiguration(object):
    def __init__(self, startup_path):
        self.__configuration_dir = os.path.expanduser(startup_path)

    def load_mailbox_config(self) -> bool:
        configuration_file_path = os.path.join(self.__configuration_dir, 'init')
        valid = os.path.exists(configuration_file_path)
        if valid is True:
            self.__mailbox_config = configparser.ConfigParser()
            self.__mailbox_config.read(configuration_file_path)
        return valid


    def get_type(self) -> str:
        return self.__mailbox_config.get('account', 'type')

    def get_location(self) -> str:
        return os.path.expanduser(self.__mailbox_config.get('account', 'location'))

    def is_valid(self) -> bool:
        rule_file_path = None
        
        valid = os.path.exists(self.__configuration_dir)
        # testing that the specified path exists
        if valid is False:
            Logger.write().error('Unable to initialize; could not find configuration directory "%s"' % self.__configuration_dir)
        else:
            valid = self.load_mailbox_config()
        # testing that the "init" file in the configuration dir exists and is valid
        if valid is False:
            Logger.write().error('Unable to initialize; could not find the "init" configuration file in directory "%s"' % self.__configuration_dir)
        
        return valid
