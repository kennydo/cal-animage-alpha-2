from setuptools import setup

setup(name='cal-animage-alpha',
      description='The Django project that powers the website of Cal Animag e Alpha, UC Berkeley\'s anime club',
      author='Kenny Do',
      author_email='kedo@ocf.berkeley.edu',
      packages=['caa',
                'caa.officers',
                'caa.schedules',
                'caa.marathons'],
      data_files=[],
      version='2.0.0',
      long_description="""
                       The Django project that powers the website of Cal Animage Alpha, UC Berkeley's anime club
                       """,
      url='http://www.calanimagealpha.com',
      classifiers=['Programming Language :: Python'],
      )
