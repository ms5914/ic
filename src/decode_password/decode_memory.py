import sys
from collections import deque

class StreamPasswordDecoder:
    def __init__(self, filepath):
        self.filepath = filepath
        self.cached_line = None  # To hold the line that triggers a new block

    def _iter_lines(self):
        """Generator to handle reading lines and managing the lookahead cache."""
        with open(self.filepath, 'r') as f:
            for line in f:
                yield line.strip()

    def solve(self):
        """
        Solves Part 3 (First complete password) using stream processing.
        Logic applies to Part 1 and 2 automatically.
        """
        found_indices = {} # Stores {index: char}
        
        line_iter = self._iter_lines()
        
        # We need a loop that can handle the state transitions
        current_line = self.cached_line if self.cached_line else next(line_iter, None)
        
        while current_line is not None:
            # 1. Parse Index (Optional)
            block_index = None
            if current_line.isdigit():
                block_index = int(current_line)
                current_line = next(line_iter, None)
                if current_line is None: break

            # 2. Parse Coordinates [x, y]
            if current_line.startswith('['):
                # Simple parsing without heavy regex for speed
                content = current_line.strip('[]')
                x_str, y_str = content.split(',')
                x, y = int(x_str), int(y_str)
            else:
                # Malformed block or empty line, skip
                current_line = next(line_iter, None)
                continue

            # 3. Process Grid (Stream Mode)
            # We need a buffer of size y + 1 to find the y-th item from the bottom
            # We only store the relevant CHARACTERS, not the whole rows.
            char_buffer = deque(maxlen=y + 1)
            
            while True:
                # Get next line
                next_line = next(line_iter, None)
                
                # CHECK: Is this line the start of a NEW block?
                if next_line is None or next_line.isdigit() or next_line.startswith('['):
                    # We hit the end of the current grid block.
                    # Cache this line so it's processed in the next main loop iteration
                    self.cached_line = next_line
                    break
                
                # It's a grid row. Extract ONLY the char we care about (at x)
                if x < len(next_line):
                    char_buffer.append(next_line[x])
                else:
                    # If x is out of bounds for this row, append a placeholder (or ignore)
                    char_buffer.append(None)

            # 4. Resolve the Character
            # The target is at logical index 'y' from the bottom.
            # In our buffer of size y+1, this is always index 0.
            target_char = None
            if len(char_buffer) == y + 1:
                target_char = char_buffer[0]
            
            # 5. Logic for Part 3 (Stop at duplication)
            if target_char and block_index is not None:
                if block_index in found_indices:
                    # Collision detected! Stop immediately.
                    break
                found_indices[block_index] = target_char
            
            # Update loop variable (self.cached_line was updated in the inner loop)
            current_line = self.cached_line

        # Construct result
        sorted_indices = sorted(found_indices.keys())
        return "".join([found_indices[i] for i in sorted_indices])

# --- Usage ---
# decoder = StreamPasswordDecoder('large_password.txt')
# print(decoder.solve())
