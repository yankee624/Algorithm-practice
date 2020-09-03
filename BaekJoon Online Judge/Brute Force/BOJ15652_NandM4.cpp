#include <iostream>
using namespace std;

int N, M;
int arr[10];

void print_seq(int idx) {
	if (idx == M) {
		for (int i = 0; i < M; i++) {
			cout << arr[i];
			if (i != M - 1) cout << ' ';
		}
		cout << '\n';
		return;
	}
	int start = idx == 0 ? 1 : arr[idx - 1];
	for (int i = start; i <= N; i++) {
		arr[idx] = i;
		print_seq(idx + 1);
	}

}

int main() {
	cin >> N >> M;
	print_seq(0);
	
	return 0;
}