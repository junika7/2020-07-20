import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [fasta]")
    sys.exit()

f = sys.argv[1] #이렇게 지정하고 파일명 자리에 f 입력하면
d = {}#count 위한 딕셔너리 설정

with open(f, 'r') as handle: #이렇게 사용하면 python 016.py [파일명] 해서 유연하게 사용 가능
    for line in handle:
        if line.startswith(">"): #FASTA 형식에서 header 제외하는 것
            continue
        for s in line.strip(): #ACGTACTAAAA
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
print(d)

total = 0
for key, value in d.items():
    total += value
print(total) #전체 염기 개수를 더해서 NCBI에 나온 것과 일치하는지 확인

with open("result.txt", 'w') as handle:
    handle.write(f"A: {d['A']}\n")
    handle.write(f"C: {d['C']}\n")
    handle.write(f"G: {d['G']}\n")
    handle.write(f"T: {d['T']}\n")

