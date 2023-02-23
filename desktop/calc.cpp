#include <iostream>
#include <cmath>
int main(){
    float y;
    float y2;
    float y3;
    int z;
    while(true){
        std::cout<<"what operation\n";
        std::cout<<"0:add\n1:subtract\n2:multiply\n3:divide\n4:get exponent\n5:roots\n6:exit\n";
        std::cin>>z;
       switch(z){
        case 0:
            std::cin>>y>>y2;
            std::cout<<y+y2<<std::endl;
        break;
        case 1:
            std::cin>>y>>y2;
            std::cout<<y-y2<<std::endl;
        break;
        case 2:
            std::cin>>y>>y2;
            std::cout<<y*y2<<std::endl;
        break;
        case 3:
            std::cin>>y>>y2;
            std::cout<<y/y2<<std::endl;
        break;
        case 4:
            std::cin>>y>>y2;
            std::cout<<pow(y,y2)<<std::endl;
        break;
        case 5:
            std::cin>>y>>y3;
            while(std::pow(y2,y3)!=y){
                y2++;
            }
            std::cout<<y2<<std::endl;
        break;
        case 6:
            return 0;
        break;
        default:
            std::cout<<"invalid input\n";
        }
    }
}