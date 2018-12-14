import setuptools

setuptools.setup(name='custom_env',
      version='0.0.2',
      install_requires=['gym'],
      packages=setuptools.find_packages())
# Note: Alternatively instead of find_packages(), we could do ["custom_env", "custom_env.envs"]
