import os
import shutil

import aenea.config


def reload_aenea_configuration():
    for name in os.listdir('%s\\grammars_enabled' % aenea.config.PROJECT_ROOT):
        if name.endswith('.py'):
            with open('%s\\grammars_enabled\\%s' % (aenea.config.PROJECT_ROOT, name)) as infd:
                with open('C:\\NatLink\\NatLink\\MacroSystem\\_%s' % name, 'w') as outfd:
                    outfd.write(infd.read())
        elif os.path.isdir('%s\\grammars_enabled\\%s' % (aenea.config.PROJECT_ROOT, name)):
            shutil.rmtree('C:\\NatLink\\NatLink\\MacroSystem\\%s' % name, ignore_errors=True)
            shutil.copytree('%s\\grammars_enabled\\%s' % (aenea.config.PROJECT_ROOT, name), 'C:\\NatLink\\NatLink\\MacroSystem\\%s' % name)
    for name in os.listdir('%s\\util' % aenea.config.PROJECT_ROOT):
        if name == 'config.py' and aenea.config.DONT_UPDATE_CONFIG:
            continue

        if name.endswith('.py') or name.endswith('.txt'):
            with open('%s\\util\\%s' % (aenea.config.PROJECT_ROOT, name)) as infd:
                with open('C:\\NatLink\\NatLink\\MacroSystem\\%s' % name, 'w') as outfd:
                    outfd.write(infd.read())

if __name__ == '__main__':
    reload_aenea_configuration()
