nama_domain = input("masukan nama domain")

index = nama_domain.index(".")
# [kata1 : kata2]
nama = nama_domain[:index]
domain = nama_domain[index:]

print(f"nama anda adalah = {nama}")
print(f"domain anda adalah = {domain}")