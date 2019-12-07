from conans import ConanFile, CMake, tools
import os

class HelloConan(ConanFile):
    name            = "packageTemplate"
    version         = "0.1"
    license         = "freeware"
    url             = "https://github.com/ssitkowx/PackageTemplate"
    description     = "Package template"
    settings        = "os", "compiler", "build_type", "arch"
    options         = {"shared": [True, False]}
    default_options = "shared=False"
    generators      = "cmake"
    
    def source(self):
        cloneCmd = 'git clone ' + self.url + '.git'
        self.run(cloneCmd)

    def build(self):
        currentPath = os.getcwd();
        projectPath = ''
        if os.path.exists(currentPath + '\\conanfile.py'):
            projectPath = os.getcwd().replace('\conan','')
        elif os.path.exists(currentPath + '\\conanbuildinfo.cmake'):
            projectPath = os.getcwd() + '\\PackageTemplate'
        else:
            print('Unknown path in build')
        
        buildPath   = projectPath + '\\build'
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
        self.cpp_info.libs = ["PackageTemplate"]
