import sys
import chilkat

crypt = chilkat.CkCrypt2()

success = crypt.UnlockComponent("Anything for 30-day trial")
if (success != True):
    print "Crypt component unlock failed"
    sys.exit()

crypt.put_CryptAlgorithm("aes")
crypt.put_CipherMode("cbc")
crypt.put_KeyLength(128)

#  16 bytes of key for 128-bit encryption.
key = "1234567890123456"

#  The IV is equal to the block size of the encryption algorithm.

iv = "1234567890123456"

#  Set the key.
crypt.SetEncodedKey(key,"ascii")

#  Set the IV
crypt.SetEncodedIV(iv,"ascii")

#  AES Encrypt the file (the file may be any size because it will
#  stream the file in/out.
success = crypt.CkEncryptFile("ecdctry.txt","aesEncrypted.txt")
if (success != True):
    print crypt.lastErrorText()
    sys.exit()

#  AES Decrypt the file (the file may be any size because it will
#  stream the file in/out.
success = crypt.CkDecryptFile("aesEncrypted.txt","ecdctry_aes.txt")
if (success != True):
    print crypt.lastErrorText()
    sys.exit()

print "AES File Encryption Success."

#  Now do 3DES file encryption:

#  To use Triple-DES, set the algorithm = "des",
#  and the key length = 168.
#  To use DES, set the key length = 56 bits.
crypt.put_CryptAlgorithm("des")
crypt.put_CipherMode("cbc")
crypt.put_KeyLength(168)

#  3DES Encrypt the file
success = crypt.CkEncryptFile("ecdctry.txt","tripleDesEncrypted.txt")
if (success != True):
    print crypt.lastErrorText()
    sys.exit()

#  3DES Decrypt the file
success = crypt.CkDecryptFile("tripleDesEncrypted.txt","ecdctry_des.txt")
if (success != True):
    print crypt.lastErrorText()
    sys.exit()

print "3DES File Encryption Success."

#  Do Blowfish file encryption:

#  To use Blowfish, set the algorithm = "blowfish2".
#  The original Chilkat "blowfish" implementation outputs
#  4321 swapped bytes.  "blowfish2" output is in the correct
#  byte order.
crypt.put_CryptAlgorithm("blowfish2")
crypt.put_CipherMode("cbc")
crypt.put_KeyLength(128)

#  Blowfish Encrypt the file
success = crypt.CkEncryptFile("ecdctry.txt","blowfishEncrypted.txt")
if (success != True):
    print crypt.lastErrorText()
    sys.exit()

#  Blowfish Decrypt the file
success = crypt.CkDecryptFile("blowfishEncrypted.txt","ecdctry_blowfish.txt")
if (success != True):
    print crypt.lastErrorText()
    sys.exit()

print "Blowfish File Encryption Success."

#  Do RC2 file encryption:

#  To use RC2, set the algorithm = "rc2".
#  Also, set the Rc2EffectiveKeyLength property.
#crypt.put_CryptAlgorithm("rc2")
#crypt.put_CipherMode("cbc")
#  Key length and effective key length should range
#  from 8 to 1024 bits.
#crypt.put_KeyLength(128)
#crypt.put_Rc2EffectiveKeyLength(128)

#  RC2 Encrypt the file
#success = crypt.CkEncryptFile("hamlet.xml","rc2Encrypted.txt")
#if (success != True):
 #   print crypt.lastErrorText()
  #  sys.exit()

#  RC2 Decrypt the file
#success = crypt.CkDecryptFile("rc2Encrypted.txt","hamlet_rc2.xml")
#if (success != True):
 #   print crypt.lastErrorText()
  #  sys.exit()

#print "RC2 File Encryption Success.""""

#  Do ARC4 file encryption:

#  To use ARC4, set the algorithm = "arc4".
crypt.put_CryptAlgorithm("arc4")
crypt.put_KeyLength(128)

#  ARC4 Encrypt the file
success = crypt.CkEncryptFile("ecdctry.txt","arc4Encrypted.txt")
if (success != True):
    print crypt.lastErrorText()
    sys.exit()

#  ARC4 Decrypt the file
success = crypt.CkDecryptFile("arc4Encrypted.txt","ecdctry._arc4.txt")
if (success != True):
    print crypt.lastErrorText()
    sys.exit()

print "ARC4 File Encryption Success."
