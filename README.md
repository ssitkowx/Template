# Template
Description:
Template for projects and packages.

Structure:
The project has been divided into three main parts:
    Project:
	    - With header files and source code.
    Project lib:
	    - With project library.
	Tests:
	    - Using the project library and gtest and/or gmock technology.

Configuration:
1. Currently used:
- Python 2.7.16,
- CMake version 3.17.0-rc2,
- Visual Studio 2019.

2. GTest and GMock tooked from:
   https://bintray.com/bincrafters/public-conan/gtest%3Abincrafters/1.8.1%3Astable#

3. You need update your remotes:
   Conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan
   
4. Edit conanfile.py. For example:
  - name     = "Template"                                          -> Display
  - Packages = ["packageName/version@owner/channel", next package] -> ["Logger/1.0@ssitkowx/stable", "Utils/2.3@ssitkowx/testing"] 

Builidng:
1. Go to 'Conan' folder,
2. Open git bash console,
3. Type 'conan source .'
4. Type 'conan install .'
5. Type 'conan build .'
6. Got to 'Build' folder and open Visual Project.

Tips:
- It is unacceptable if the package calls the package (recursion),
- The first time you start the program python packages can be missing. Please follow the python suggestion to install them,
- The first time you start the program after entering 'conan build .' CMakeLists is updated with current project name and packages names. 
  Remove Build folder and try again with updated CMakeLists.txt,
- To install gtest and gmock packages for specified options and settings type 'conan install . --build gtest'.