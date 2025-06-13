#include <iostream>

int main(){

    auto a = [](int c) -> int {
        return 3*c;
    }

    std::cout << "eta: " << a(3) << std::endl; 
    

}