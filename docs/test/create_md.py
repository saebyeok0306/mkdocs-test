import random

for i in range(100):
    with open(f"c:/Users/open/prviatespace/docs/docs/test/test{i:03d}.md", "w", encoding="utf-8") as f:
        f.write(f"# offset {hex(random.randint(0, 0xFFFFFFFF))}\n\n테스트 페이지\n")