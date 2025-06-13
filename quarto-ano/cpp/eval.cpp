#include<iostream>
#include<string>

constexpr int sum(int i){
    return i + 2;
}

//for c++ 20
consteval int sum2(int i){
    return i + 2;
}

int main(int argc, char** argv)
{
    if(argc < 2){
        std::cout << "INVALID ARGUMENTS\n";
        return 1;
    }
    
    int val = std::stoi(argv[1]);
    
    std::cout << "value from args: " << val << std::endl;
    std::cout << "sum: " << sum(val) << std::endl;
    std::cout << "sum2: " << sum2(val) << std::endl;

    return 0;
}
