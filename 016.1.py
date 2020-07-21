import sys
import gzip

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [fasta.gz]")

f = sys.argv[1]
d_dict = {}

with gzip.open(f, 'rb') as handle: #read binary
    for line in handle:
        line = line.decode("utf-8") #byte인 line을 string으로 만들어줌
#        print(type(line.strip())) #type(line.strip())으로 하면 type 확인 가능한데 byte로 나옴
#        sys.exit() #여기서 끊으면 한 줄만 출력
        if line.startswith(">"):
            continue
        for s in line.strip():
            if s in d_dict:
                d_dict[s] += 1
            else:
                d_dict[s] = 1

print(d_dict)

total = 0
for keys, values in d_dict.items():
    total += values

print(total)

with open ("result1.txt", 'w') as handle:
    handle.write(f"A: {d_dict['A']}\n")
    handle.write(f"T: {d_dict['T']}\n")
    handle.write(f"G: {d_dict['G']}\n")
    handle.write(f"C: {d_dict['C']}\n")
    handle.write(f"Total: {total}\n")
