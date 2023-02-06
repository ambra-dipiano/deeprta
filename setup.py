# *****************************************************************************
# Copyright (C) 2023 INAF
# This software is distributed under the terms of the BSD-3-Clause license
#
# Authors:
# Ambra Di Piano <ambra.dipiano@inaf.it>
# *****************************************************************************

import os
from setuptools import setup, find_packages

entry_points = {'console_scripts': [
    'hello = deeprta.hello.hello:main',
    ]
} 

scripts_path = "deeprta"
scripts = [scripts_path+file for file in os.listdir(scripts_path)]
for script in scripts:
     print(script)

setup( 
    name='deeprta',
    author='Ambra Di Piano <ambra.dipiano@inaf.it>',
    package_dir={'deeprta': 'deeprta'},
    packages=find_packages(),
    include_package_data=True,
    license='BSD-3-Clause',
	#entry_points=entry_points
)
