from setuptools import setup, find_packages
from __ida_setup__ import IdaPluginInstallCommand


setup(

    # Usual pip package informations
    name = YOUR_PLUGIN_NAME,
    version = YOUR_PLUGIN_VERSION,
    description = YOUR_PLUGIN_DESCRIPTION,
    long_description = YOUR_PLUGIN_BIOGRAPHY,
    author = YOURSELF_I_HOPE,
    author_email = WHERE_LINKED_RECRUITERS_CAN_SPAM_YOU,
    url = YOUR_FANTASTIC_WEBSITE,
    
    # Declare dependencies as you would for traditional python packages
    # there will be pip installed in your IDA plugins folder
    # Fortunately, some ida plugins libraries are present on pypi
    install_requires = [
        # 'ida-netnode' : fireeye's netnode idapython library
    ],

    # Either explicitely declare packages, or rely on setuptools.find_packages
    packages = find_packages(),

    # necessary files that are not part of a package
    # __ida_setup__ must absolutely be a part of it
    py_modules = ['__ida_setup__', 'my_2$_plugin_t'], 

    # __ida_setup__ rely on 'ida_plugins' key to install
    # plugin entries at the '$IDA_DIR\plugins' root level
    package_data={
        # Add any ida python plugin here
        'ida_plugins': ['idarop_plugin_t.py'],
    },
    
    # monkey patch install script for IDA plugin custom install
    cmdclass={'install': IdaPluginInstallCommand}
)