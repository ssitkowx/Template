#include "gmock/gmock.h"
#include "gtest/gtest.h"

int main (int v_argc, char ** v_argv)
{
    ::testing::InitGoogleMock (&v_argc, v_argv);
    return RUN_ALL_TESTS ();
}