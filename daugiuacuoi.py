s1 = input()
s2 = input()

# Lấy ký tự đầu
f_s1 = s1[0]
f_s2 = s2[0]
# Lấy ký tự giữa
if(len(s1) % 2 == 0):
  m_s1 = s1[int(len(s1)/2)]
else:
  m_s1 = s1[int((len(s1)-1)/2)]

if(len(s2) % 2 == 0):
  m_s2 = s2[int(len(s2)/2)]
else:
  m_s2 = s2[int((len(s2)-1)/2)]

# Lấy ký tự cuối
l_s1 = s1[-1]
l_s2 = s2[-1]
# Gộp vào một ký tự
merge = f_s1 + f_s2 + m_s1 + m_s2 + l_s1 + l_s2
print(merge)