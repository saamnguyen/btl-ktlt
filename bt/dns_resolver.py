import dns.resolver
 
hosts = ["oreilly.com", "yahoo.com", "google.com", "microsoft.com", "cnn.com"]

for host in hosts:
    print(host)
    ip = dns.resolver.query(host, "A")  #thay A bằng NS, MX để có các record khác nhau
    for i in ip:
        print(i)