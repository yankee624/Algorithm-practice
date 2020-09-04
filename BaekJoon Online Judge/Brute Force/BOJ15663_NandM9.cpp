#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
int num[10];
int arr[10];
int used[10];

void print_seq(int idx) {
	if (idx == M) {
		for (int i = 0; i < M; i++) {
			cout << arr[i];
			if (i != M - 1) cout << ' ';
		}
		cout << '\n';
		return;
	}

	int last_used = -1;
	for (int i = 0; i < N; i++) {
		if (!used[i] && last_used != num[i]) {
			last_used = num[i];
			used[i] = true;
			arr[idx] = num[i];
			print_seq(idx + 1);
			used[i] = false;
		}
	}

}

int main() {
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> num[i];
	}
	sort(num, num + N);

	print_seq(0);


	return 0;
}