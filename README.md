# Custom OpenAI Gym environments

At the moment just Acrobot-v2.

To compile:
`python setup.py bdist_wheel`

To install:
`pip install dist/*`

Or to compile and install certainly:
`rm -rf build custom_env.egg-info dist && python setup.py bdist_wheel && pip uninstall custom-env &&  pip install dist/*.whl`
