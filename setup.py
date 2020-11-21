import setuptools

"""
目前还未完善，不能用， 当前入口是manage.py
https://packaging.python.org/tutorials/packaging-projects/
"""
setuptools.setup(
    name="Competition",  # Replace with your own username
    version="0.0.1",
    author="FelixFang",
    author_email="unthinkfull@gmail.com or unthinkfull@sina.com",
    description="",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://cn.bing.com/",
    include_package_data=True,  # 告诉 setuptools 要 搜索一个 MANIFEST.in 文件，把文件内容所匹配的所有条目作为包数据安装
    zip_safe=False,  # 用于强制或防止创建 zip 压缩包。通常你不会想要把包安装为 zip 压缩文件，因为一些工具不支持压缩文件，而且压缩文件比较难以调试。
    install_requires=['Flask'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows :: Windows 10"
    ],  # https://pypi.org/classifiers/
    python_requires='>=3.6',
)
