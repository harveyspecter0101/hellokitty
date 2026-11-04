#include <bits/stdc++.h>
using namespace std;

// Deterministic Quick Sort
int partition(vector<int>& arr, int s, int e) {
    int pivot = arr[s];
    int cnt = 0;

    for (int i = s + 1; i <= e; i++)
        if (arr[i] < pivot) cnt++;

    int pivot_idx = s + cnt;
    swap(arr[s], arr[pivot_idx]);

    int i = s, j = e;

    while (i < pivot_idx && j > pivot_idx) {
        while (i < pivot_idx && arr[i] < pivot) i++;
        while (j > pivot_idx && arr[j] > pivot) j--;

        if (i < pivot_idx && j > pivot_idx) {
            swap(arr[i], arr[j]);
            i++;
            j--;
        }
    }

    return pivot_idx;
}

void quick_sort(vector<int>& arr, int s, int e) {
    if (s >= e) return;

    int idx = partition(arr, s, e);
    quick_sort(arr, s, idx - 1);
    quick_sort(arr, idx + 1, e);
}

// Randomized Quick Sort
int partition2(vector<int>& arr, int s, int e) {
    int random_idx = s + rand() % (e - s + 1);
    swap(arr[s], arr[random_idx]);

    int pivot = arr[s];
    int cnt = 0;

    for (int i = s + 1; i <= e; i++)
        if (arr[i] < pivot) cnt++;

    int pivot_idx = s + cnt;
    swap(arr[s], arr[pivot_idx]);

    int i = s, j = e;

    while (i < pivot_idx && j > pivot_idx) {
        while (i < pivot_idx && arr[i] < pivot) i++;
        while (j > pivot_idx && arr[j] > pivot) j--;

        if (i < pivot_idx && j > pivot_idx) {
            swap(arr[i], arr[j]);
            i++;
            j--;
        }
    }

    return pivot_idx;
}

void quick_sort2(vector<int>& arr, int s, int e) {
    if (s >= e) return;

    int idx = partition2(arr, s, e);
    quick_sort2(arr, s, idx - 1);
    quick_sort2(arr, idx + 1, e);
}

int main() {
    srand(time(0));

    vector<int> arr1 = {5, 4, 3, 2, 1};
    vector<int> arr2 = arr1;

    quick_sort(arr1, 0, (int)arr1.size() - 1);
    cout << "Deterministic: ";
    for (int x : arr1) cout << x << " ";
    cout << '\n';

    quick_sort2(arr2, 0, (int)arr2.size() - 1);
    cout << "Randomized:    ";
    for (int x : arr2) cout << x << " ";
    cout << '\n';

    return 0;
}