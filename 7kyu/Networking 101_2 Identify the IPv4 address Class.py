def ipv4_address_class(ipv4_addr):
    x, *_ = map(int, ipv4_addr.split('.'))
    if x > 239:
        return 'E'
    if x > 223:
        return 'D'
    if x > 191:
        return 'C'
    if x > 127:
        return 'B'
    return 'A'


print(ipv4_address_class("172.66.43.71"))
