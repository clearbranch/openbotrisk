# IP addresses and network origin

## Plain explanation

An IP address is the network address that lets computers send data to each other over the Internet.

When your browser requests a web page, the website receives a request from an IP address. That address is not the same thing as your name, your device, or your account. It is closer to a return address for network traffic.

In practice, an IP address can tell a website things like:

- which network the request came from
- roughly where the network is located
- whether the address belongs to a home broadband provider, mobile network, cloud provider, VPN, proxy, company network, or hosting provider
- whether similar addresses have been seen doing suspicious things before

## Why IP addresses can be grouped

IP addresses are allocated in blocks. Those blocks are often associated with organisations such as internet service providers, mobile networks, universities, companies, cloud providers, or hosting firms.

That means a website or security provider can group traffic by:

- exact IP address
- IP range or subnet
- organisation or network owner
- autonomous system number (ASN)
- country or region
- residential, mobile, datacentre, VPN, proxy, or hosting network
- previous reputation of that IP or network

## Why IP alone is weak evidence

An IP address does not reliably identify one person.

Several people can share one public IP address because of household routers, workplaces, universities, public Wi-Fi, mobile networks, or network address translation. One person can also appear from many IP addresses because they move between home broadband, mobile data, work, VPNs, proxies, or cloud services.

So IP is useful, but it should be treated as one signal, not proof.

## Why this matters for bot detection

Bot detection systems often use IP-related signals because many abusive requests come from known hosting networks, proxy networks, VPNs, or reused infrastructure.

But defenders cannot rely only on IP. A bad bot can use residential proxies or rotate addresses. A real user can appear from a suspicious network. So IP signals are usually combined with cookies, headers, browser fingerprints, account history, and behaviour.

## Project use

Use this note before discussing:

- IP reputation
- datacentre versus residential proxies
- VPNs
- mobile carrier NAT
- ASN blocking
- residential proxy abuse
- rate limiting by IP
- why “same IP” does not always mean “same person”

## Sources

- Wikipedia, “IP address”: https://en.wikipedia.org/wiki/IP_address
- Wikipedia, “Network address translation”: https://en.wikipedia.org/wiki/Network_address_translation
- Wikipedia, “Autonomous system (Internet)”: https://en.wikipedia.org/wiki/Autonomous_system_(Internet)
