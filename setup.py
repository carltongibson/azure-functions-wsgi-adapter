from setuptools import setup

from wsgi_adapter import DESCRIPTION, VERSION

setup(name='azure_functions_wsgi_adapter',
      version=VERSION,
      description=DESCRIPTION,
      url='https://github.com/carltongibson/azure-functions-wsgi-adapter',
      author='Carlton Gibson',
      author_email='carlton.gibson@noumenal.es',
      license='MIT',
      packages=['wsgi_adapter'],
      zip_safe=False)

