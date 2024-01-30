import hashlib 
def crack_sha1_hash(hash, use_salts=False):
  pass_dict={}
  passwords=[]
  
  readfile_and_addarray("top-10000-passwords.txt", passwords)
  if use_salts:
    top_salts=[]
    bpassword_dict={}
    readfile_and_addarray("known-salts.txt", top_salts)
    for salt in top_salts:
      for bpassword in passwords:
        appended=hashlib.sha1(bpassword.encode("utf-8")+salt.encode("utf-8")).hexdigest()
        prepended=hashlib.sha1(salt.encode("utf-8")+bpassword.encode("utf-8")).hexdigest()
        bpassword_dict[appended]=bpassword
        bpassword_dict[prepended]=bpassword
    if(hash in bpassword_dict):
      return bpassword_dict[hash]
    return "PASSWORD NOT IN DATABASE"  
        
        
  for password in passwords:
    hashline=hashlib.sha1(password.encode("utf-8")).hexdigest()
    pass_dict[hashline]=password
  if hash in pass_dict:
    return pass_dict[hash]
  else :
    return "PASSWORD NOT IN DATABASE"
def readfile_and_addarray(filename,arr):
  with open(filename, "rb") as file:
    line=file.readline().strip()
    while line:
      arr.append(line.decode("utf-8"))
      line=file.readline().strip()
'''l=crack_sha1_hash("da5a4e8cf89539e66097acd2f8af128acae2f8ae",True)
print(l)'''
