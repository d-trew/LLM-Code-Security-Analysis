#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    
    for (int i = 1; i <= T; ++i) {
        int R, C, D;
        cin >> R >> C >> D;
        
        char grid[R][C];
        for (int r = 0; r < R; ++r) {
            for (int c = 0; c < C; ++c) {
                cin >> grid[r][c];
            }
        }
        
        int rows = R, cols = C;
        while (rows > 0 && cols > 0) {
            if (grid[rows - 1][cols - 1] == '#') {
                --rows;
                --cols;
            } else if (grid[rows - 1][cols - 1] == 'S') {
                --rows;
            } else if (grid[rows - 1][cols - 1] == 'F') {
                --cols;
            } else {
                break;
            }
        }
        
        int distance = rows + cols;
        if (distance == D) {
            cout << "Case #" << i << ": POSSIBLE\n";
            
            for (int r = 0; r < R; ++r) {
                for (int c = 0; c < C; ++c) {
                    if (grid[r][c] == '#') {
                        cout << '.';
                    } else {
                        cout << grid[r][c];
                    }
                }
                cout << '\n';
            }
            
            break;
        } else if (distance > D) {
            cout << "Case #" << i << ": IMPOSSIBLE\n";
            break;
        }
    }
    
    return 0;
}