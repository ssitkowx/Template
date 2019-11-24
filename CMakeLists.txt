PROJECT (PackageTemplate)
cmake_minimum_required (VERSION 2.8.12)
if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17")
endif()

add_definitions ("-std=c++11")

set  (currentPath ${CMAKE_CURRENT_SOURCE_DIR})
set  (buildPath ${currentPath}/build)
file (COPY ${currentPath}/conan/conanbuildinfo.cmake DESTINATION ${buildPath})

include (${buildPath}/conanbuildinfo.cmake)
conan_basic_setup()

set  (projectIncludePath                  ${currentPath}/Project)
FILE (GLOB_RECURSE projectFilesInclude    ${projectIncludePath}/*.h ${projectIncludePath}/*.hxx)
FILE (GLOB_RECURSE projectFilesAndFolders ${projectIncludePath}/*)

set  (testIncludePath                     ${currentPath}/Test)
FILE (GLOB_RECURSE testFilesInclude       ${testIncludePath}/*.h ${testIncludePath}/*.hxx)
FILE (GLOB_RECURSE testFilesAndFolders    ${testIncludePath}/*)

file (GLOB buildFiles ${buildPath}/*)
foreach (file ${buildFiles})
	if (EXISTS ${file})
		file(REMOVE ${file})
	endif()
endforeach(file)

source_group               (TREE ${projectIncludePath} PREFIX "" FILES ${projectFilesAndFolders})
add_executable             (Project ${projectFilesAndFolders})
target_include_directories (Project PUBLIC ${projectFilesInclude})
target_link_libraries      (Project ${CONAN_LIBS})
set_property               (TARGET Project PROPERTY CXX_STANDARD 17)

source_group               (TREE ${testIncludePath} PREFIX "" FILES ${testFilesAndFolders})
link_directories           (Test ${buildPath}/lib)
add_executable             (Test ${testFilesAndFolders})
target_include_directories (Test PUBLIC ${testFilesInclude})
target_link_libraries      (Test ProjectLib ${CONAN_LIBS})
set_property               (TARGET Test PROPERTY CXX_STANDARD 17)

add_library                (ProjectLib ${projectFilesAndFolders})
set_property               (TARGET ProjectLib PROPERTY CXX_STANDARD 17)






