/**
 * @author na6x Narayanaa
 */
#include<bits/stdc++.h>
#define mod 1000000007
#define inf 1e18
#define PI 3.141592653589
#define fi first
#define se second
#define sv(v) sort(all(v));reverse(all(v))
#define all(v) v.begin(),v.end()
#define rep(i,a,b) for(ll i=a;i<b;i++)
#define repr(i,a,b) for(ll i=a;i>b;i--)
#define pb push_back
#define mk make_pair
#define en '\n'
#define ios ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define upper(s) s.begin(), s.end(), s.begin(), ::toupper
#define lower(s) s.begin(), s.end(), s.begin(), ::tolower
using namespace std;
typedef long long int ll;
typedef pair<ll,ll> pll;
typedef long double ld;
typedef vector<ll> V;

int fastMod(ll base, ll exp, ll m){
    if(exp == 0) return 1;
    if(!(exp & 1)){
        ll temp= bigMod(base, exp/2, m)%m;
        return (temp*temp)%m;
    }
    else return ((base%m)*(bigMod(base, exp-1, m))%m)%m;
}
 
 
int main()
{   
    ios;
    ll t;
    cin >> t;
    while(t--) {


    }
	return 0;
}
