# ping

> Send ICMP ECHO_REQUEST packets to network hosts.

- Ping host:

`ping {{host}}`

- Ping a host only a specific number of times (4 by default):

`ping -n {{count}} {{host}}`

- Ping the specified host until you force it to stop using Ctrl-C.:

`ping -t {{host}}`
