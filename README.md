idasetup : a custom setup.py file for IDA plugins
=========

`__ida_setup__.py` add the support of custom IDA plugins directories for the `setup.py` install command.

Supported options :

```
--ida                                force custom ida install script.
--ida-version                        specify ida version.
--ida-install-deps                   install ida plugin dependencies.
```


## Install

Just type :
	
```C:\Python27\python.exe setup.py install $plugin --ida```

`__ida_setup__.py` is meant to be backward compatible, so you can install it as a "normal" package if you don't provide
the `--ida` switch.

You can specify the ida version if you have several IDA install on your machine :

```C:\Python27\python.exe setup.py install $plugin --ida --ida-version=6.9```

Currently supported versions : 6.8, 6.9, 7.0 (beta).

You can also tell Python to download and install any declared dependency by using the `--ida-install-deps`.


if the plugin is on Pypi, so you can `pip` from it and injecting ida switches using `"--install-option"`.
(NB : `--ida-install-deps` is useless here since `pip` have it's own `--no-deps` install switch )

On Windows:
`C:\Python27\Scripts\pip2.7.exe install $plugin --install-option="--ida"`
`C:\Python27\Scripts\pip2.7.exe install $plugin --install-option="--ida --ida_version="6.9""`

Ida is installed in %Program_Files%, so you need to run the install command (whether from a `setup.py` or `pip`) with Administrator rights.

On Mac:

On Linux:


## Building 

`C:\Python27\python.exe .\setup.py build sdist`
`C:\Python27\Scripts\twine.exe upload .\dist\$plugin-$plugin_version.tar.gz --repository-url https://test.pypi.org/legacy/ -u $username -p $password`

`C:\Python27\Scripts\pip.exe install -i https://testpypi.python.org/pypi --verbose --no-deps $plugin --install-option="--ida"`