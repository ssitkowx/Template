from conans import ConanFile, CMake, tools
import os

class Conan(ConanFile):
    name            = "Template"
    version         = "1.0"
    license         = "freeware"
    repoUrl         = "https://github.com/ssitkowx"
    url             = repoUrl + '/' + name + '.git'
    downloadsPath   = "C:/Users/sitko/.conan/download"
    description     = "Template for projects and packages"
    settings        = "os", "compiler", "build_type", "arch"
    options         = {"shared": [True, False]}
    default_options = "shared=False"
    generators      = "cmake"
    author          = "sylsit"
    #requires        = "ProjectOrPackageName/1.0@ssitkowx/testing"
    
    def source(self):
        cloneCmd = 'git clone ' + self.url
        self.run(cloneCmd)

    def build(self):
        currentPath = os.getcwd();
        projectPath = os.getcwd().replace('\Conan','')
        if not os.path.exists(projectPath + '\\CMakeLists.txt'):
            projectPath = os.getcwd() + '\\' + self.name

        self.buildPath = projectPath + '\\Build'
        
        if self.settings.os == 'Windows' and self.settings.compiler == 'Visual Studio':
            cmake = CMake(self)
            cmake.configure(source_dir=projectPath, build_dir=self.buildPath)
            cmake.build()
        else:
            raise Exception('Unsupported os in build')
            
        tools.replace_in_file(projectPath + "\\CMakeLists.txt", "Template", self.name, False)
        
    def package(self):     
        currentPath = os.getcwd();
        projectPath = os.getcwd().replace('\Conan','')
        if not os.path.exists(projectPath + '\\CMakeLists.txt'):
            projectPath = self.buildPath.replace('Build','')
    
        self.copy('*.h'     , dst='include', src= projectPath + '\\' + self.name, keep_path=False)
        self.copy('*.hxx'   , dst='include', src= projectPath + '\\' + self.name, keep_path=False)
        self.copy('*.lib'   , dst='lib'    , src= projectPath + '\Build\lib'    , keep_path=False)
        self.copy('*.dll'   , dst='bin'    , src= projectPath + '\Build\bin'    , keep_path=False)
        self.copy('*.dylib*', dst='lib'    , src= projectPath + '\Build\lib'    , keep_path=False)
        self.copy('*.so'    , dst='lib'    , src= projectPath + '\Build\lib'    , keep_path=False)
        self.copy('*.a'     , dst='lib'    , src= projectPath + '\Build\lib'    , keep_path=False)

    def package_info(self):
        self.cpp_info.libs = [self.name]
