import os

base_directory = os.getcwd()
path = []
current_directory = ""


op_string = input("Enter the op strong:")
op_arr = op_string.split(" ")

for op in op_arr:
  
  if op.startswith("d") :
    os.mkdir(op[1:])
    current_directory = op[1:]
    
  elif op.startswith("f") :
    os.system('touch '+op[1:])
   
  elif op.startswith(">") :
  
    if current_directory not in path:
    	path.append(current_directory)
    	
    if (os.getcwd() != os.path.join(base_directory,"/".join(path))):
      os.chdir(os.path.join(base_directory,"/".join(path)))
      
  elif op.startswith("<") :
    path.pop()
    os.chdir(os.pardir)
    
  else :
    print("Unknown Command!")
