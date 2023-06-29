#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  map<pair<int, double>, double> memo;
  vector<int> V;
  int C;
  double percent;

  double findMaxProfit(int i, double sum) {
    if (i >= V.size()) return 0;

    pair<int, double> k = pair<int, double>(i, sum);

    if (memo.find(k) != memo.end()) return memo[k];

    double ifPick = sum + V[i] - C;
    double ifNPick = (sum + V[i]) * percent;

    if (ifPick >= ifNPick) return memo[k] = ifPick + findMaxProfit(i + 1, 0);

    return memo[k] = max(
      ifPick + findMaxProfit(i + 1, 0),
      findMaxProfit(i + 1, ifNPick));
  }

  double getMaxExpectedProfit(vector<int> &V, int C, double S) {
    this->V = V;
    percent = 1 - S;
    this->C = C;

    return percent == 1 ? accumulate(V.begin(), V.end(), -C) : findMaxProfit(0, 0);
  }
}

double getMaxExpectedProfit(int N, vector<int> V, int C, double S) {
  return (new Solution())->getMaxExpectedProfit(V, C, S);
}
