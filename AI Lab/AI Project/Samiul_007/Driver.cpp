#include<bits/stdc++.h>
using namespace std;

int main()
{
    for(int i = 10; i<1000; i+=40)

    {
		printf("%d\n", i);
        string command = "./SPP ";
        string app = to_string(i);
        command.append(app);
        string tofile = " >> results.txt";
        command.append(tofile);
        system(command.c_str());
    }
}
