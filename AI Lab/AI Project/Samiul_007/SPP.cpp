#include<bits/stdc++.h>
#include <time.h>
#include <boost/algorithm/string.hpp>
#include <fstream>
#include <string>
#include <iostream>
#include<cstdlib>

using namespace std;

#define MAXN 1005
struct edge
{
    int u, v, w;
    bool operator<(const edge& p) const
    {
        return w < p.w;
    }
};
int pr[MAXN];
vector<edge> e, sedge;

int find(int r)
{
    return (pr[r] == r) ? r : find(pr[r]);
}
int mst(int n)
{
    sort(e.begin(), e.end());

    for (int i = 1; i <= n; i++)
    {
        pr[i] = i;
        if((i+1)%2==0)
        {
            pr[i] = i+1;

        }
    }


    int count = n/2, s = 0;
    // printf("Added edges\n");
    for (int i = 0; i < (int)e.size(); i++)
    {
        int u = find(e[i].u);
        int v = find(e[i].v);
        if (u != v)
        {
            //   printf("%d -- %d = %d\n",e[i].u,e[i].v, e[i].w);
            sedge.push_back(e[i]);
            pr[u] = v;
            count++;
            s += e[i].w;
            if (count == n - 1)
                break;
        }
    }
    return s;
}



int main(int argc, char** argv)
{
//    freopen("input.txt", "r", stdin);
    int total_edges = 0;
    int total_cost = 0;
    srand(time(0));
    int n = atoi(argv[1]);
    int cnt[n+1];
    int adj[1005][1005];
    //printf("All edges\n");
    for (int i=1; i<=n; i++)
    {
        cnt[i] = 0;
        for (int j=i+1; j<=n; j++)
        {
            int random;
            srand(time(0));
            random = rand() % 2 + 10;
            edge get;
            get.u = i;
            get.v = j;
            get.w = random;
            if(i%2==1 && j==i+1)
            {
                get.w = 2;
                sedge.push_back(get);
            }
            //   printf("%d %d - %d\n", i,j,random);
            e.push_back(get);
            adj[i][j] = random;
        }
    }

    total_cost += mst(n);
//   printf("Mst cost = %d\n", total_cost);
    total_edges += n-1 - (n/2);
    // printf("MST edges\n");
    for (int i = 0; i < (int)sedge.size(); i++)
    {
        //  printf("%d %d -- %d\n", sedge[i].u,sedge[i].v,sedge[i].w);
        cnt[sedge[i].u]++;
        cnt[sedge[i].v]++;
    }

    int cc = 0;
    int mx = -99;
    vector<int> blossom;
    for (int i=1; i<=n; i++)
    {
        if(cnt[i]%2==1)
        {
            mx = i;
            cc++;
            blossom.push_back(i);
            //printf("node %d -- degree %d\n", i, cnt[i]);
        }

    }
    int fwd[(int)blossom.size()];
    int bkd[mx+1];
    for (int i = 0; i < (int)blossom.size(); i++)
    {
        fwd[i] = blossom[i];
        bkd[blossom[i]] = i;
    }

    ofstream myfile ("blossom.txt");
    myfile<<cc<<endl;
    myfile<<(cc * (cc-1))/2 <<endl;
    for (int i = 0; i < (int)blossom.size(); i++)
    {
        for (int j = i+1; j < (int)blossom.size(); j++)
        {
            //printf("%d %d = %d\n", blossom[i],blossom[j],adj[blossom[i]][blossom[j]]);
            myfile<<bkd[blossom[i]]<<" "<<bkd[blossom[j]]<<" "<<adj[blossom[i]][blossom[j]]<<endl;

        }
    }
//    printf("Running Blossom\n");
    system(" ./example -f blossom.txt --minweight > blossom_output.txt");

    ifstream bfile("blossom_output.txt");
    string line;

    if (bfile.is_open())
    {
        while ( getline (bfile,line) )
        {
            vector<string> result;
            boost::split(result, line, boost::is_any_of(" "));
            int a, b;
            a = atoi(result[0].c_str());
            b = atoi(result[1].c_str());
            total_cost += adj[fwd[a]][fwd[b]];
            total_edges += 1;
            //printf("%d %d = %d\n", fwd[a],fwd[b],adj[fwd[a]][fwd[b]]);
        }
        bfile.close();
    }

    printf("%d,%d,%d\n",n, total_edges, total_cost);
    return 0;
}
