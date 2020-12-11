cmake_minimum_required(VERSION 3.17)
project(myside C)

set(CMAKE_C_STANDARD 11)

add_executable(myside main.c chat1002.h chatbot.c knowledge.c)