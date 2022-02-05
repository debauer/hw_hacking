import telnetlib

HOST = "192.168.1.126"
user = "root"
password = "xmhdipc"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")

tn.read_until(b"Welcome to Monitor Tech.")
tn.write(b"ls\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))