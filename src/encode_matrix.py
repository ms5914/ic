def solution(key):
    # Prepare the standard alphabet without 'J'
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    # List to store the unique characters in order
    result_chars = []
    # Set to keep track of seen characters for O(1) lookups
    seen = set()
    
    # 1. Process the input key
    # Convert to uppercase and replace J with I immediately
    processed_key = key.upper().replace("J", "I")
    
    for char in processed_key:
        # We only care about valid letters A-Z
        if "A" <= char <= "Z":
            if char not in seen:
                seen.add(char)
                result_chars.append(char)
                
    # 2. Fill the rest with the remaining alphabet
    for char in alphabet:
        if char not in seen:
            seen.add(char)
            result_chars.append(char)
            
    # 3. Construct the 5x5 matrix
    matrix = []
    for i in range(0, 25, 5):
        matrix.append(result_chars[i : i + 5])
        
    return matrix
