# thu thập thông tin DNS server
import dns.resolver
 
hosts = ["actvn.edu.vn", "yahoo.com", "google.com", "microsoft.com", "cnn.com"]

for host in hosts:
    print(host)
    # ip = dns.resolver.query(host, "A")  # cái này xưa rồi
    ip = dns.resolver.resolve(host, "A")
    #thay A bằng NS, MX, AAAA để có các record khác nhau
    # A : IPv4 , MX : mail servers, NS : name servers, 4A : IPv6
    for i in ip:
        print(i)