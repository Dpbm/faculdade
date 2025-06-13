#include <iostream>
#include <vector>

void show(std::vector<int> vec){
    for(auto v: vec){
        std::cout << v << " ";
    }
    std::cout << "\n";
}

int main(){

    const int outside = 6;
    auto a = [outside](int c) -> int {
        return (3 * c) + outside;
    };
    
    
    std::vector<int> d = {1,2,3};
    auto sum_vec = [&](std::vector<int>& vec){
      for(size_t i = 0; i < vec.size(); i++) vec.at(i) += d.at(i);
    };

    std::cout << "eta: " << a(3) << std::endl; 
    
    std::vector<int> b = {2,3,4};
   
    sum_vec(b);
    
    show(std::move(b));
    show(b);
}