from conans import ConanFile, CMake, tools
import os

class HelloConan(ConanFile):
    name = "packageTemplate"
    version = "0.1"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Hello here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "src/*"
    
    def source(self):
        self.run("git clone git@github.com:ssitkowx/Packages.git")
        #self.run("cd Packages/PackageTemplate")
        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
        #tools.replace_in_file("Packages/PackageTemplate/CMakeLists.txt", "PROJECT (PackageTemplate)",
        #   '''PROJECT(PackageTemplate)
        #      include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
        #      conan_basic_setup()''')

    def build (self):
        #trunkPath = os.getcwd().replace("\conan",'')
        trunkPath = os.getcwd()
        cmakePath = trunkPath + "/Packages/Template"
        buildPath = cmakePath + "/build"
        cmake     = CMake(self)
        cmake.configure(source_dir=cmakePath, build_dir=buildPath)
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    #def package_info(self):
        #self.cpp_info.libs = ["hello"]
