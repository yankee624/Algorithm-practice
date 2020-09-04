#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N;

bool next_permutation(vector<int> &arr) {
	// find last non-decreasing (i-1, i) pair
	int i = N - 1;
	while (i - 1 >= 0 && arr[i - 1] >= arr[i]) {
		i--;
	}
	// if the whole array is non-increasing, that is the last permutation
	if (i == 0) return false;

	
	int j = N - 1;
	while (arr[j] <= arr[i-1]) j--;
	swap(arr[i - 1], arr[j]);

	j = N - 1;
	while (i < j) {
		swap(arr[i], arr[j]);
		i++;
		j--;
	}
	return true;

}

int main() {
	cin >> N;
	vector<int> arr(N);
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}

	if (next_permutation(arr)) {
		for (int i = 0; i < N; i++) {
			cout << arr[i] << ' ';
		}
	}
	else {
		cout << -1;
	}

	return 0;
}