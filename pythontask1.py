class task1():
    # Read a String statement from the command line
    while True:
        ip_str = input("Enter a string: ")
        if ip_str:
            print(f"you enter : {ip_str}")
            break
        else:
            print("Input cannot be empty. Please enter a string.")
    ip_str = ip_str.lower()
    
    # Findout total number of characters present in the statement.
    def ttl_num_char(self):
        ip_str = self.ip_str
        temp = []  
        total_char = 0
        for i in ip_str:
            total_char +=1
            if i not in temp and i != " ":
                temp.append(i)
                count_char = ip_str.count(i)
                print(f"{i} : {count_char}")
        print(f"total number of characters : {total_char}")

  
    # Findout total number of duplicate Characters in the statement
    def ttl_num_dup(self):
        self.ttl_num_char()
        ip_str = self.ip_str
        unique_val =[]
        duplicate_val = []
        for i in ip_str:
            if i not in unique_val:
                unique_val.append(i)
            else:
                duplicate_val.append(i)

        print(f"duplicate values : {duplicate_val}")


    # Findout total number of words present in the statement
    def ttl_num_words(self):
        self.ttl_num_dup()
        ip_str = self.ip_str
        count_val = 0
        for i in ip_str:
            if i != " ":
                count_val += 1
        print(f"total number of words : {count_val}")

    # Findout total number of duplicate words in the statement
    def ttl_num_dup_words(self):
        ip_str = self.ip_str
        self.ttl_num_words()
        # temp = []
        # for i in ip_str.split(" "):
        #     if ip_str.count(i)>1 and i not in temp:
        #         temp.append(i)
        #         print(f"duplicate words present in string {i} : {ip_str.count(i)}")
        for i in ip_str.split(" "):
            if ip_str.count(i)>1:
                print(f"{i} : {ip_str.count(i)}")
    # Reverse the characters present in the statement.
    def reverse_str(self):
        ip_str = self.ip_str
        self.ttl_num_dup_words()
        print(ip_str[::-1])

    # Reverse the words present in the statement.
    def reverse_word(self):
        ip_str = self.ip_str
        self.reverse_str()
        split_word = ip_str.split(" ")
        print(split_word[::-1])

        # Form a new statement from the reversed words.
        print(" ".join(map(str,split_word[::-1])))

    # Remove the duplicate characters from the latest statement.
    def rm_dup(self):
        ip_str = self.ip_str
        self.reverse_word()
        uniq_values =[]
        for i in ip_str:
            if i not in uniq_values:
                uniq_values.append(i)
        print(uniq_values)
        latest_str = "".join(map(str, uniq_values))
        print(f"after remove the duplicate : {latest_str}")
        new_str = "".join(set(ip_str))
        print(new_str)

        # Print final latest String statement.
        print(new_str)
        print(f"latest string values : {latest_str}")

obj1= task1()
obj1.rm_dup()
