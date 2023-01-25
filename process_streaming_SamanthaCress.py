import csv

# Create variable for Lizard input file
input_file_name = "Lizards.csv"

# Declare a variable for output file
output_file_name = "Out9.txt"

# Create a file object for input (r = read access)
input_file = open(input_file_name, "r")

# Create a file object for output (w = write access)
# we'll get an extra line after each record, this what you need for each record to be on seperate line!!
output_file = open(output_file_name, "w", newline='')

import csv
import socket
import time

host = "localhost"
port = 9999
address_tuple = (host, port)

# use an enumerated type to set the address family to (IPV4) for internet
socket_family = socket.AF_INET 

# use an enumerated type to set the socket type to UDP (datagram)
socket_type = socket.SOCK_DGRAM 

# use the socket constructor to create a socket object we'll call sock
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# read from Lizard CSV file
input_file = open("Lizards.csv", "r")

# use the built0in sorted() function to get them in chronological order
reversed = sorted(input_file)

# create a csv reader for our comma delimited data
reader = csv.reader(reversed, delimiter=",")

for row in reader:
    # read a row from the file
    Species, Aquatic, Herbivorous, Nocturnal, Scansorial, Fossorial, Large, Terrestrial, Archetype  = row

    # use an fstring to create a message from our data
    fstring_message = f"[{Species}, {Aquatic}, {Herbivorous}, {Nocturnal}, {Scansorial}, {Fossorial}, {Large}, {Terrestrial}, {Archetype}]"
    
    # prepare a binary (1s and 0s) message to stream
    MESSAGE = fstring_message.encode()

    # use the socket sendto() method to send the message
    sock.sendto(MESSAGE, address_tuple)

    print(f"Sent: {MESSAGE} on port {port}.", file=open('out9.txt', 'a'))
    time.sleep(3)
   
output_file.close()
input_file.close()
