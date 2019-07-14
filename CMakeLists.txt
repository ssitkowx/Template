PROJECT (PackageTemplate)
cmake_minimum_required (VERSION 2.8.12)

add_definitions ("-std=c++11")

set  (cmakePath ../${CMAKE_CURRENT_SOURCE_DIR})
#set  (conanPath ${cmakePath}/conan)
set  (buildPath ${cmakePath}/PackageTemplate/build)
#file (COPY ${conanPath}/conanbuildinfo.cmake DESTINATION ${cmakePath}/build)
file (COPY ${cmakePath}/conanbuildinfo.cmake DESTINATION ${cmakePath}/PackageTemplate/build)

include (${buildPath}/conanbuildinfo.cmake)
conan_basic_setup()

set  (projectIncludePaths       ${cmakePath}/Project/include)
set  (projectSourcePaths        ${cmakePath}/Project/source)
file (GLOB projectFilesInclude  ${projectIncludePaths}/*.h  ${projectIncludePaths}/*.hxx)
file (GLOB projectFilesSource   ${projectSourcePaths}/*.cpp ${projectSourcePaths}/*.cxx)

set  (testIncludePaths       ${cmakePath}/Test/include)
set  (testSourcePaths        ${cmakePath}/Test/source)
file (GLOB testFilesInclude  ${testIncludePaths}/*.h  ${testIncludePaths}/*.hxx)
file (GLOB testFilesSource   ${testSourcePaths}/*.cpp ${testSourcePaths}/*.cxx)

file (GLOB buildFiles ${buildPath}/*)
foreach (file ${buildFiles})
   if (EXISTS ${file})
      file(REMOVE ${file})
   endif()
endforeach(file)

add_executable             (Project ${projectFilesInclude} ${projectFilesSource})
target_include_directories (Project PUBLIC ${projectIncludePaths})
target_link_libraries      (Project ${CONAN_LIBS})

add_library                (projectLib ${projectFilesInclude} ${projectFilesSource})

link_directories           (Test ${buildPath}/lib)
add_executable             (Test ${testFilesInclude} ${testFilesSource})
target_include_directories (Test PUBLIC ${projectIncludePaths} ${testIncludePaths})
target_link_libraries      (Test ProjectLib ${CONAN_LIBS})