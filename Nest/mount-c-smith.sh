#!/bin/bash

PWD=`pwd`

mkdir -p $PWD/smb-shares/Data
mkdir -p $PWD/smb-shares/Users
mkdir -p $PWD/smb-shares/Secure
mkdir -p $PWD/smb-shares/Admin

sudo mount -t cifs -o username=C.Smith //10.10.10.178/Data $PWD/smb-shares/Data
sudo mount -t cifs -o username=C.Smith //10.10.10.178/Users $PWD/smb-shares/Users
sudo mount -t cifs -o username=C.Smith //10.10.10.178/Secure$ $PWD/smb-shares/Secure
sudo mount -t cifs -o username=C.Smith //10.10.10.178/ADMIN$ $PWD/smb-shares/Admin 
