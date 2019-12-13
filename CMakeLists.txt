PROJECT (Template)
cmake_minimum_required (VERSION 2.8.12)
if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17")
endif()

set (CurrentPath ${CMAKE_CURRENT_SOURCE_DIR})
set (BuildPath ${CurrentPath}/Build)

if (EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    file (COPY ${CurrentPath}/conan/conanbuildinfo.cmake DESTINATION ${BuildPath})
	include (${BuildPath}/conanbuildinfo.cmake)
	conan_basic_setup ()
endif()

set  (ProjectIncludePath                  ${CurrentPath}/Project)
FILE (GLOB_RECURSE ProjectFilesInclude    ${ProjectIncludePath}/*.h ${ProjectIncludePath}/*.hxx)
FILE (GLOB_RECURSE ProjectFilesAndFolders ${ProjectIncludePath}/*)

set  (TestIncludePath                     ${CurrentPath}/Test)
FILE (GLOB_RECURSE TestFilesInclude       ${TestIncludePath}/*.h ${TestIncludePath}/*.hxx)
FILE (GLOB_RECURSE TestFilesAndFolders    ${TestIncludePath}/*)

MACRO(GET_SUBDIRECTORIES_PATHS_LISTS main_subdirectory_path subdirectories_paths_lists)
    SET(directoryPathsLists "")
    FOREACH(subdirectoryPath ${main_subdirectory_path})
        GET_FILENAME_COMPONENT(directoryPath ${subdirectoryPath} PATH)
        SET(directoryPathsLists ${directoryPathsLists} ${directoryPath})
    ENDFOREACH()
    LIST(REMOVE_DUPLICATES directoryPathsLists)
    SET(${subdirectories_paths_lists} ${directoryPathsLists})
ENDMACRO()

set(ProjectSubdirectoriesPathsLists "")
GET_SUBDIRECTORIES_PATHS_LISTS("${ProjectFilesAndFolders}" ProjectSubdirectoriesPathsLists)

set(TestSubdirectoriesPathsLists "")
GET_SUBDIRECTORIES_PATHS_LISTS("${TestFilesAndFolders}" TestSubdirectoriesPathsLists)

MACRO(REMOVE_FILES directory)
	File (GLOB removeLists ${directory}/*)
	foreach (file ${removeLists})
		if (EXISTS ${file})
			file(REMOVE ${file})
		endif()
	endforeach(file)
ENDMACRO()

REMOVE_FILES("${BuildPath}")

source_group               (TREE ${ProjectIncludePath} PREFIX "" FILES ${ProjectFilesAndFolders})
add_executable             (Project ${ProjectFilesAndFolders})
target_include_directories (Project PUBLIC ${ProjectSubdirectoriesPathsLists})
target_link_libraries      (Project ${CONAN_LIBS})
target_compile_features    (Project PUBLIC cxx_std_17)

source_group               (TREE ${TestIncludePath} PREFIX "" FILES ${TestFilesAndFolders})
link_directories           (Test ${BuildPath}/lib)
add_executable             (Test ${TestFilesAndFolders})
target_include_directories (Test PUBLIC ${ProjectSubdirectoriesPathsLists} ${TestSubdirectoriesPathsLists})
target_link_libraries      (Test ProjectLib ${CONAN_LIBS})
target_compile_features    (Test PUBLIC cxx_std_17)

add_library                (ProjectLib STATIC ${ProjectFilesAndFolders})
target_include_directories (ProjectLib PUBLIC ${ProjectSubdirectoriesPathsLists})
target_compile_features    (ProjectLib PUBLIC cxx_std_17)





