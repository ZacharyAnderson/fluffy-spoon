import os
import hashlib

def find_duplicate_files(starting_dir):
    fileDict = {}
    stack = [starting_dir]
    # This duplicate List will return a list of tuples (dup_file, Original_file)
    dupList = []
    
    while len(stack):
        current_path= stack.pop()
        
        # If path isDir
        if os.path.isdir(current_path):
            for path in os.listdir(current_path):
                full_path=os.path.join(current_path, path)
                stack.append(full_path)
         
        # If a file       
        else:
            
            file_hash = sample_hash_file(current_path)
            current_last_edited_time = os.path.getmtime(current_path)
           
            
            if file_hash in fileDict:
                existing_last_edited_time, existing_path = fileDict[file_hash]
                if current_last_edited_time > existing_last_edited_time:
                    dupList.append((current_path, existing_path))
                else:
                    # This means the old file is the duplicate
                    dupList.append((existing_path, current_path))
                    fileDict[file_hash] = (current_last_edited_time, current_path)
                    
            else:
                fileDict[file_hash] = (current_last_edited_time, current_path)
                
    return dupList
    
    def sample_hash_file(path):
        num_bytes_to_read_per_sample = 4000
        total_bytes = os.path.getsize(path)
        hasher = hashlib.sha512()

        with open(path, 'rb') as file:
        # If the file is too short to take 3 samples, hash the entire file
            if total_bytes < num_bytes_to_read_per_sample * 3:
                hasher.update(file.read())
            else:
                num_bytes_between_samples = (
                    (total_bytes - num_bytes_to_read_per_sample * 3) / 2
                )
    
                # Read first, middle, and last bytes
                for offset_multiplier in xrange(3):
                    start_of_sample = (
                        offset_multiplier
                        * (num_bytes_to_read_per_sample + num_bytes_between_samples)
                    )
                    file.seek(start_of_sample)
                    sample = file.read(num_bytes_to_read_per_sample)
                    hasher.update(sample)
    
        return hasher.hexdigest()