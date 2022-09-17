import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["00FFFF", "00FF66"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "임금")
write("description", "각리중")
write("button", "버튼")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "나이": "16",
  "생년월일": "20071030",
  "좋아하는 것": "음악",
  "싫어하는 것": "치즈가 들어간 거의 모든 음식"
}
information(informations)
