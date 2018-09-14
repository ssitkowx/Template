project (Template)
cmake_minimum_required (VERSION 2.8.12)

add_definitions ("-std=c++11")

set  (trunkPath ${CMAKE_CURRENT_SOURCE_DIR})
set  (conanPath ${trunkPath}/conan)
set  (buildPath ${trunkPath}/build)
file (COPY ${conanPath}/conanbuildinfo.cmake DESTINATION ${trunkPath}/build)

include (${buildPath}/conanbuildinfo.cmake)
conan_basic_setup()

set  (projectIncludePaths       ${trunkPath}/Project/include)
set  (projectSourcePaths        ${trunkPath}/Project/source)
file (GLOB projectFilesInclude  ${projectIncludePaths}/*.h  ${projectIncludePaths}/*.hxx)
file (GLOB projectFilesSource   ${projectSourcePaths}/*.cpp ${projectSourcePaths}/*.cxx)

set  (testIncludePaths       ${trunkPath}/Test/include)
set  (testSourcePaths        ${trunkPath}/Test/source)
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

add_library                (projectLib ${projectFilesInclude} ${projectFilesSource} ${CONAN_LIBS})

link_directories           (Test ${buildPath}/lib)
add_executable             (Test ${testFilesInclude} ${testFilesSource})
target_include_directories (Test PUBLIC ${projectIncludePaths} ${testIncludePaths})
target_link_libraries      (Test ProjectLib ${CONAN_LIBS})