from coal import CoalFile
from util import download, unzip, default_cmake_build, cp, pkg_config, abspath, glob
from os import path

class NanovgFile(CoalFile):
    url = "https://github.com/memononen/nanovg.git"
    exports = ["include", "src"]

    def prepare(self):
        git_clone(self.url, 'master', 'repo')
    def package(self):
        cp('repo/src/*.h', 'include/')
        cp('repo/src/*.c', 'src/')
    def info(self, generator):
        generator.add_include_dir('include/')
        generator.add_source_files(*glob('src/*'))
