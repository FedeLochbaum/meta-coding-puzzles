#include <bits/stdc++.h>
using namespace std;

class Solver {
private:
  vector<int> pageDepth;
  vector<int> L;

  pair<int, int> recordPageDepth(int page, int depth) {
    if (pageDepth[page] > 0) return {INT_MAX, pageDepth[page]};

    if (pageDepth[page] != 0) return {(pageDepth[page] * -1), depth - (pageDepth[page] * -1)};

    pageDepth[page] = -1 * depth;

    pair<int, int> depthInfo = recordPageDepth(L[page] - 1, depth + 1);

    pageDepth[page] = depthInfo.first <= depth ? depthInfo.second : depthInfo.second + 1;

    return {depthInfo.first, pageDepth[page]};
  }

public:
  int getMaxVisitableWebpages(int N, vector<int> &L) {
    pageDepth = vector<int>(N, 0);
    this->L = L;
    int _max = 0;
    for (int i = 0; i < N; i++)
      if (pageDepth[i] <= 0)
        _max = max(_max, recordPageDepth(i, 1).second);

    return _max;
  }
}

int getMaxVisitableWebpages(int N, vector<int> L) {
  return (new Solver())->getMaxVisitableWebpages(N, L);
}