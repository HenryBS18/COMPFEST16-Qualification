from pwn import remote

r = remote('nc challenges.ctf.compfest.id', 9015)

r.send