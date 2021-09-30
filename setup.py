from setuptools import setup, find_packages

"""
#|##########################|#
#|### Development stages ###|#
#|##########################|#
#|#1 - Planning            #|#
#|#2 - Pre-Alpha           #|#
#|#3 - Alpha               #|#
#|#4 - Beta                #|#
#|#5 - Production/ Stable  #|#
#|#6 - Mature              #|#
#|#7 - Inactive            #|#
#|##########################|#
"""

setup(
    name='amc',
    version='2.0.0.3',
    python_requires='>=3.9',
    install_requires=['net-tools', 'network-manager', 'macchanger', 'pyinstaller'],
    find_packages='pkg',
    include_package_data=True,
    url='https://github.com/hexdee606/AMC2.0',
    license='CC0 1.0 Universal',
    description='Automatic MAC Spoofing Tool',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: CC0 1.0 Universal',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.9',
        'Topic :: Security',
    ],
    keywords='Automatic Media Access Control [MAC] Address Spoofing Tool',
    entry_points={
        'console_scripts': [
            'amc = amc:amc_main',
        ],
    },
)
