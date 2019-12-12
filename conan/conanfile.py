from conans import ConanFile, CMake, tools
import os

class Conan(ConanFile):
    name            = "Template"
    version         = "1.0"
    license         = "freeware"
    url             = "https://github.com/ssitkowx/Template.git"
    description     = "Template for projects and packages"
    settings        = "os", "compiler", "build_type", "arch"
    options         = {"shared": [True, False]}
    default_options = "shared=False"
    generators      = "cmake"
    
    def source(self):
        cloneCmd = 'git clone ' + self.url
        self.run(cloneCmd)

    def build(self):
        currentPath = os.getcwd();
        projectPath = ''
        if os.path.exists(currentPath + '\\conanfile.py'):
            projectPath = os.getcwd().replace('\Conan','')
        elif os.path.exists(currentPath + '\\conanbuildinfo.cmake'):
            projectPath = os.getcwd() + '\\' + self.name
        else:
            print('Unknown path in build')
        
        buildPath   = projectPath + '\\Build'
        cmake       = CMake(self)
        cmake.configure(source_dir=projectPath, build_dir=buildPath)
        cmake.build()
        
    def package(self):
        self.copy('*.h'     , dst='include', src='../Project'  , keep_path=False)
        self.copy('*.hxx'   , dst='include', src='../Project'  , keep_path=False)
        self.copy('*.lib'   , dst='lib'    , src='../build/lib', keep_path=False)
        self.copy('*.dll'   , dst='bin'    , src='../build/bin', keep_path=False)
        self.copy('*.dylib*', dst='lib'    , src='../build/lib', keep_path=False)
        self.copy('*.so'    , dst='lib'    , src='../build/lib', keep_path=False)
        self.copy('*.a'     , dst='lib'    , src='../build/lib', keep_path=False)

    def package_info(self):
        self.cpp_info.libs = [self.name]
