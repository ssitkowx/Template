from conans import ConanFile, CMake
import os

class Template (ConanFile):
   name            = "PackageTemplate"
   settings        = {"os", "compiler", "build_type", "arch"}
   version         = "1.0"
   #requires        = "Poco/1.7.8p3@pocoproject/stable"
   generators      = "cmake", "gcc", "txt"
   default_options = "Poco:shared=True", "OpenSSL:shared=True"
   trunkPath       = os.getcwd().replace("\conan",'')

   def configure (self):
      print ("operating system")
      print (self.settings.os)
      #if self.settings.os == "Windows":
      #   self.settings['build_type'] = 'Release'
      #else:
      #   raise Exception ("Invalid operating system")

   def build (self):
      cmakePath = self.trunkPath
      buildPath = os.path.join(self.trunkPath, "build")
      cmake     = CMake(self)
      cmake.configure(source_dir=cmakePath, build_dir=buildPath)
      cmake.build()

   def package (self):
      includePath = os.path.join(self.trunkPath, "Project/include")
      binPath     = os.path.join(self.trunkPath, "build/bin")
      libPath     = os.path.join(self.trunkPath, "build/lib")
      self.copy ("*.h",     dst="include", src=includePath, keep_path=False)
      self.copy ("*.hxx",   dst="include", src=includePath, keep_path=False)
      self.copy ("*.lib",   dst="lib",     src=libPath,     keep_path=False)
      self.copy ("*.dll",   dst="bin",     src=binPath,     keep_path=False)
      self.copy ("*.so",    dst="lib",     src=libPath,     keep_path=False)
      self.copy ("*.dylib", dst="lib",     src=libPath,     keep_path=False)
      self.copy ("*.a",     dst="lib",     src=libPath,     keep_path=False)
