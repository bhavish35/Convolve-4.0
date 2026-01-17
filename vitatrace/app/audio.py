#include <bits/stdc++.h>
using namespace std;
#define int long long
#define pb push_back
typedef vector<int> vi;
#define all(v) v.begin(), v.end()
#define take(arr, idx, size) vi arr(size); for (int idx = 0; idx < size; idx++) cin >> arr[idx];
#define rep(i, start, end) for (int i = start; i < end; i++)
#define rrep(i, end, start) for (int i = end; i >= start; i--)
#define printv(a) for(int i=0 ; i<a.size() ; i++) cout << a[i] << ' ';
typedef pair<int, int> pii;
const int MOD =  998244353;


long long fastpow(long long n, long long x, long long m){
    long long ret = 1;
    n %= m;
    while (x) {
        if (x & 1) (ret *= n) %= m;
        x >>= 1;
        (n *= n) %= m;
    }
    return ret;
}

long long modInverse(long long n, long long m){
    return fastpow(n, m - 2, m);
}

long long ncrMod(int n, int r, int m){
    if (n < r) return 0;
    if (r == 0) return 1;

    vector<long long> fac(n + 1);
    fac[0] = 1;
    for (int i = 1; i <= n; i++)
        fac[i] = (fac[i - 1] * i) % m;

    return (fac[n] * modInverse(fac[r], m) % m
            * modInverse(fac[n - r], m) % m)
           % m;
}

typedef int item;
// struct item{
//   int op,cl,bl;
// };
 
struct segtree{
    int size;
    vector<item> values;
 
    item NEUTRAL_ELEMENT = 0;
 
    void init(int n){
        size = 1;
        while(size < n) size*=2;
        values.resize(2*size);
    }
    
    item merge(item a , item b ){
      
    }
    
    item single(item v){
      return v;
    }
    
    void set(int i, item v , int x , int lx , int rx){
        if(rx - lx == 1) {
          values[x] = v;
          return;
        }
        int m = (lx + rx) / 2;
        if( i < m ) set(i,v,2*x+1,lx,m);
        else set(i,v,2*x+2,m,rx);
 
        values[x] = merge(values[2*x+1],values[2*x+2]);
    }
 
    void set(int i,item v){
      set(i,v,0,0,size);
    }
    
    void build(vector<item> &a,int x, int lx , int rx){
        if(rx - lx == 1){
            if(lx  < a.size()){
                values[x] = single(a[lx]);
            }
            return;
        }
 
        int m = (lx + rx)/2;
        build(a , 2*x+1 , lx , m);
        build(a , 2*x+2 , m , rx );
        values[x] = merge(values[2*x+1],values[2*x+2]);
    }
 
    void build(vector<item > &a){
        build(a,0,0,size);
    }
 
    item calc(int l, int r , int x , int lx , int rx){
        if(lx >= r || l >= rx) return NEUTRAL_ELEMENT;
        if(lx >= l && rx <= r) return values[x];
 
        int m = (lx + rx) / 2;
        item a = calc(l , r , 2*x+1 , lx , m);
        item b = calc(l , r , 2*x+2 , m , rx);
        return merge(a,b);
    }
 
    item calc(int l,int r){
        return calc(l,r,0,0,size);
    }
    
    item get_ans(){
      return values[0];
    }
    
};

//***********Solution starts here************


//some observations


/**/

void solve(){
    int n;
    string s;
    cin >> n >> s;
    vector<vector<vi>> dp1(n+3 , vector<vi> (n+1, vi(4,0))), dp2(n+1,vector<vi> (n+1, vi(4,0)));
    dp1[0][0][0] = 1;

    rep(i,1,n+1) {
        dp1[i] = dp1[i-1];
        dp2[i] = dp2[i-1];
        rep(j,0,n+1){
            rep(k,0,4){
                if (dp1[i-1][j][k] == 0) continue;

                int add = dp2[i-1][j][k];
                int nj,nk;
                if (s[i-1] == '(') {
                    nj = j + 1;
                    nk = k;
                    if (k == 1) nk = 2;
                    else if(k == 2 || k==3 )nk = 3;
                    dp1[i][nj][nk] = (dp1[i][nj][nk] + dp1[i-1][j][k]) % MOD;
                    dp2[i][nj][nk] = (dp2[i][nj][nk] + add + dp1[i-1][j][k]) % MOD;
                } 
                else {
                    if (j == 0) continue;
                    nj = j - 1; nk = (k == 0 ? 1 : k);
                    dp1[i][nj][nk] = (dp1[i][nj][nk] + dp1[i-1][j][k]) % MOD;
                    dp2[i][nj][nk] = (dp2[i][nj][nk] + add + dp1[i-1][j][k]) % MOD;
                }
            }
        }
    }

    int ans = (dp2[n][0][3] - (2LL * dp1[n][0][3]) + MOD) % MOD;
    ans +=MOD;
    cout << ans%MOD << '\n';
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t = 1;
    cin >> t;
    //pre_calc();
    while (t--) {
        solve();
    }
    return 0;
}