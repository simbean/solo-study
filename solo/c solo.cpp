#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int a[10];
int len = sizeof(a) / sizeof(int);
class A {
public:
	string key;
	int Value;
	A(string key, int Value) :key(key), Value(Value) {}
};
int print(int* V) {
	int i = 0;
	for (i = 0; i < len; i++) {
		cout << V[i] << ' ';
	}
	cout << endl;
	return 0;
}
bool compare(A a, A b) {
	return a.key > b.key;
	
}
void print(vector<A> V) {
	int i = 0;
	for (i = 0; i < V.size(); i++) {
		cout << V[i].key << ' '<<V[i].Value<<' ';
		cout << endl;
	}
}
void main() {
	int i = 0;
	int b;
	string Va;
	int Vb;
	vector<A> v;
	for (i = 0; i < len;i++) {
		cin >> b;
		a[i] = b;
	}
	sort(a, a + len);
	print(a);
	sort(a, a + len, greater<int>());
	print(a);
	for (i = 0; i < 5; i++) {
		cin >> Va;
		cin >> Vb;
		v.push_back(A(Va, Vb));
	}
	print(v);
	sort(v.begin(), v.end(), compare);
	print(v);
}
