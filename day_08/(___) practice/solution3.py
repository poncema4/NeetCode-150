def solution(paragraphs, width):
    result = []
    
    # Add top border
    result.append("*" * (width + 2))
    
    # Process each paragraph
    for paragraph in paragraphs:
        if not paragraph:
            continue
            
        i = 0
        n = len(paragraph)
        
        while i < n:
            j = i
            line_len = 0
            
            # Find how many words fit on this line
            while j < n and line_len + len(paragraph[j]) + (j - i) <= width:
                line_len += len(paragraph[j])
                j += 1
            
            # Build the line with center justification
            line = ''
            for k in range(i, j):
                line += paragraph[k]
                if k != j - 1:  # Add space between words (except after last word)
                    line += ' '
            
            # Center align the line
            leftover = width - len(line)
            left_pad = leftover // 2
            right_pad = leftover - left_pad
            
            # Add borders and padding
            result.append("*" + " " * left_pad + line + " " * right_pad + "*")
            
            i = j
    
    # Add bottom border
    result.append("*" * (width + 2))
    
    return result