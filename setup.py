from setuptools import setup


setup(
    name= 'taskaty',
    version= '0.1.0',
    description= "Simple command-Line Task-app written in Python",
    author= 'Touil Saif Yassine',
    install_requires = ['tabulate'],
    entry_points = {
        'console_scripts' : [
            'taskaty = taskaty:main',
        ]
    }
    

)