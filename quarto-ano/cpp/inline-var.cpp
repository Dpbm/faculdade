#include<iostream>
#include<string>


int main(int argc, char** argv)
{
   int val = 20;
   std::string john = "john";
   
   if(const bool is_int = std::is_same<decltype(john), int>::value; is_int){
    std::cout << "teu pai\n";
   }else{
       std::cout << "ops\n";
   }
    
    
    return 0;
}
