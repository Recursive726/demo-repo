def file_read(fname):
        with open(fname) as f:
                #Content_list is the list that contains the read lines. 
                # this is my udpdated line 
                content_list = f.readlines()
                print(content_list)

file_read("test.txt")



