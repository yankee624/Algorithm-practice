#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
int num[10];
int arr[10];

void print_seq(int idx, int selected) {
	if (selected == M) {
		for (int i = 0; i < M; i++) {
			cout << arr[i];
			if (i != M - 1) cout << ' ';
		}
		cout << '\n';
		return;
	}
	if (idx == N) return;
	
	arr[selected] = num[idx];
	print_seq(idx + 1, selected + 1);
	print_seq(idx + 1, selected);

}

int main() {
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> num[i];
	}
	sort(num, num + N);

	print_seq(0, 0);


	return 0;
}