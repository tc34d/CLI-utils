#include <stdio.h>
int main(){
    //vars
    float x;
    char selection;
    //selections
    printf("select the starting measurement and temp\n");
    scanf("%c ",&selection);
    scanf("%f",&x);
    //convertions
    switch (selection) {
    case 'c':
    printf("f=%f\n",(x*1.8)+32);
    printf("k=%f\n",273.15+x);
    break;
    case 'f':
    printf("c=%f\n",(x-32)/1.8);
    printf("k=%f\n",273.15+((x-32)/1.8));
    break;
    case 'k':
    if (x < 0){
        break;
    }
    printf("c=%f\n",x-273.15);
    printf("f=%f\n",((x-273.15)*1.8)+32);
    break;
    default:
    printf("select the letter c,k, or f\n");
    break;
    }
    
}