# dhcpwn

> Испытывает на устойчивость к DHCP IP exhaustion атаке; подслушивает локальный трафик DHCP.

- Наводняет сеть IP-запросами:

`dhcpwn --interface {{network_interface}} flood --count {{number_of_requests}}`

- Подслушивает локальный трафик DHCP:

`dhcpwn --interface {{network_interface}} sniff`
