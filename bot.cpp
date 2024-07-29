#include <filesystem>
#include <iostream>
#include <fstream>
#include <string>
#define RED "\033[0:31m"
#define GREEN "\033[0:32m"

int main(){
    while(true){
    std::ifstream last("v/last.txt");
    std::string value;
    std::getline(last,value);
    std::cout<<value<<std::endl;
    };
};