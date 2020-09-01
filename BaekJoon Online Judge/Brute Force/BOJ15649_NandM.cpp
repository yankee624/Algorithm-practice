#include <iostream>
using namespace std;

int N, M;
int arr[10];
bool used[10];


void print_permutation(int idx) {
	if (idx == M) {
		for (int i = 0; i < idx; i++) {
			cout << arr[i];
			if (i != idx - 1) cout << ' ';
		}
		cout << '\n';
	}
	else {
		for (int i = 1; i <= N; i++) {
			if (!used[i]) {
				arr[idx] = i;
				used[i] = true;
				print_permutation(idx + 1);
				used[i] = false;
			}
		}
	}
}

int main() {
	cin >> N >> M;
	print_permutation(0);
	return 0;

}