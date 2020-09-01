#include <iostream>
using namespace std;

int N, M;
int arr[10];

void print_combination(int idx, int selected) {
	// If selected M numbers, done
	if (selected == M) {
		for (int i = 0; i < M; i++) {
			cout << arr[i];
			if (i != M - 1) cout << ' ';
		}
		cout << '\n';
		return;
	}
	if (idx > N) return;

	// Select "idx"
	arr[selected] = idx;
	print_combination(idx + 1, selected + 1);
	// Don't select "idx"
	print_combination(idx + 1, selected);
	
}

// For numbers 1 ~ N, select or don't select (2^n)
int main() {
	cin >> N >> M;
	print_combination(1, 0);


	return 0;
}