def solve():
    A, B, C = map(int, input().split())
    
    angles = sorted([A, B, C])
    
    for p in [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]:
        h_angle = angles[p[0]]
        m_angle = angles[p[1]]
        s_angle = angles[p[2]]

        for rot in range(360):
            h_angle_rot = (h_angle - rot) % (360 * 12 * (10**10))
            m_angle_rot = (m_angle - rot) % (360 * 12 * (10**10))
            s_angle_rot = (s_angle - rot) % (360 * 12 * (10**10))

            h = h_angle_rot // (360 * 10**10)
            m = (m_angle_rot // (360 * 10**8)) % 60
            s = (s_angle_rot // (360 * 10**6)) % 60
            n = (s_angle_rot // (360)) % (10**9)

            if 0 <= h < 12 and 0 <= m < 60 and 0 <= s < 60 and 0 <= n < (10**9):
              total_seconds = h * 3600 + m * 60 + s
              total_nanoseconds = total_seconds * 10**9 + n
              h_check = (total_nanoseconds // (3600 * 10**9)) % 12
              m_check = (total_nanoseconds // (60 * 10**9)) % 60
              s_check = (total_nanoseconds // (10**9)) % 60
              n_check = total_nanoseconds % 10**9
              
              h_angle_check = h_check * (360 * 10**10) // 12
              m_angle_check = m_check * (360 * 10**8) //1
              s_angle_check = s_check * (360 * 10**6) //1

              if h_angle_check == h_angle_rot and m_angle_check == m_angle_rot and s_angle_check == s_angle_rot:
                  return f"{h} {m} {s} {n}"
    return "No solution found"

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")