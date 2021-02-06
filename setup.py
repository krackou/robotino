import setuptools

with open("./README.md", "r", encoding="utf-8") as rdm:
    long_description = rdm.read()

setuptools.setup(
    name="robotino",
    version="0.0.1",
    author="anarchist_university_discord",
    description="""
    projet d'édition collaborative d'un robot
    adapté au réseau discord, et servant des
    initiatives anarchistes.
    """,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/krackou/robotino",
    packages=setuptools.find_packages(),
    install_requires=[
        'discord.py==1.6.0',
        'praw==7.1.3',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: CC0 :: 1.0 :: Universal",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5.3',
)
