PROJECT (Template)
cmake_minimum_required (VERSION 3.16)

set                    (ProjectName Template)
set                    (LibraryName TemplateLib)
set                    (PackagesLibsNames "")
set                    (PackagesLibsPaths "")
#${CONAN_LIBS}

set                    (ConanLibraryPath "C:/Users/sitko/.conan/data")
set                    (CONAN_LIBS ${CONAN_LIBS} Proj1 Proj2 Proj3)

MACRO(GET_LIBRARIES_PATHS_LISTS libraries_paths_lists)
    SET(libraryPathsLists "")
    FOREACH(library ${CONAN_LIBS})
        SET(libraryPathsLists ${libraryPathsLists} ${ConanLibraryPath}/${library})
    ENDFOREACH()
    SET(${libraries_paths_lists} ${libraryPathsLists})
ENDMACRO()

set(LibrariesPathsLists "")
GET_LIBRARIES_PATHS_LISTS(LibrariesPathsLists)
message("this is mine")
message(${LibrariesPathsLists})

set                    (CurrentPath ${CMAKE_CURRENT_SOURCE_DIR})
get_filename_component (ParentPath  ${CurrentPath} PATH)

if (EXISTS ${ParentPath}/conanbuildinfo.cmake)
	include (${ParentPath}/conanbuildinfo.cmake)
else()
	include (${CurrentPath}/Conan/conanbuildinfo.cmake)
endif()

conan_basic_setup ()

set  (ProjectIncludePath                  ${CurrentPath}/${ProjectName})
FILE (GLOB_RECURSE ProjectFilesInclude    ${ProjectIncludePath}/*.h ${ProjectIncludePath}/*.hxx)
FILE (GLOB_RECURSE ProjectFilesAndFolders ${ProjectIncludePath}/*)

set  (TestIncludePath                     ${CurrentPath}/Tests)
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

set (BuildPath ${CurrentPath}/Build)
REMOVE_FILES("${BuildPath}")

source_group               (TREE                       		   ${ProjectIncludePath} PREFIX "" FILES ${ProjectFilesAndFolders})
add_executable             (${ProjectName}                     ${ProjectFilesAndFolders})
target_include_directories (${ProjectName}  PUBLIC             ${ProjectSubdirectoriesPathsLists})
target_link_libraries      (${ProjectName}                     ${PackagesLibsNames})
target_compile_features    (${ProjectName}  PUBLIC cxx_std_17)

source_group               (TREE                       		   ${TestIncludePath} PREFIX "" FILES ${TestFilesAndFolders})
link_directories           (Tests                       	   ${BuildPath}/lib)
add_executable             (Tests                       	   ${TestFilesAndFolders})
target_include_directories (Tests    	    PUBLIC             ${ProjectSubdirectoriesPathsLists} ${TestSubdirectoriesPathsLists})
target_link_libraries      (Tests    		                   ${LibraryName} ${PackagesLibsNames})
target_compile_features    (Tests    		PUBLIC cxx_std_17)

add_library                (${LibraryName}  STATIC             ${ProjectFilesAndFolders})
target_include_directories (${LibraryName}  PUBLIC             ${ProjectSubdirectoriesPathsLists})
target_compile_features    (${LibraryName}  PUBLIC cxx_std_17)





