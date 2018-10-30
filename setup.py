from setuptools import setup

setup(name='clovaTTS',
      version='0.1',
      description='A TTS Wrapper for Naver Clova Speech Synthesis API',
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
      ],
      keywords='tts naver clova',
      url='https://github.com/zebehn/clovaTTS',
      author='Minsu Jang',
      author_email='minsu@etri.re.kr',
      license='MIT',
      packages=['clovaTTS'],
      install_requires=[
      ],
      include_package_data=True,
      zip_safe=False)